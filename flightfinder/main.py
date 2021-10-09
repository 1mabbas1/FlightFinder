#Import required modules and classes

import time
from datetime import datetime, timedelta
import csv
from flight_search import FlightSearch
from notification_manager import NotificationManager

#Create search and notification objects
notification_manager = NotificationManager()
flight_search = FlightSearch()

#retrieve destinations file and set origin city, in this case London
file = "locations.csv"
ORIGIN_CITY_IATA = "LON"

#If the destination cities do not have IATA codes, the following section adds IATA codes in the 3rd column
with open(file,"r") as f:
    reader = csv.reader(f,delimiter=',')
    writer = csv.writer(open('locations_IATA.csv', 'w',newline=""))
    data = []
    for row in reader:
        if row[2] == "":
            row[2] = flight_search.get_destination_code(row[0])
        data.append(row)
    writer.writerows(data)


# Searching for flights between tomorrow and 6 months from today
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


while True:
    with open("locations_IATA.csv", "r") as locations:
        reader = csv.reader(locations,delimiter=',')
        #Check flights for each destination using Teqiula API
        for row in reader:
            flight = flight_search.check_flights(
                ORIGIN_CITY_IATA,
                row[2],
                from_time=tomorrow,
                to_time=six_month_from_today
            )

            #If the flight prices are lower than the users lowest price. Twilio API sends the flight details to the user via sms.
            try:

                if flight.price < float(row[1]):
                    notification_manager.send_sms(
                        message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
                    )
            except AttributeError:
                pass
    #5 minute wait before checking again to prevent sending too many requests to the APIS.
    time.sleep(300)
