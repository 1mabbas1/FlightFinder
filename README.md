# FlightFinder
This app uses the Tequila and Twilio APIs to find cheap flights for a list of destinations.

The user inputs a list of locations and the maximum price they are will to pay for each destination. The currency can be altered.

The script then finds the IATA codes for all of the destinations and checks for the cheapest flights to the destination within the next 6 months user Tequila.

If the price is lower than the users maximum price, the Twilio API is used to send the user a text message of the flight details.

One of my favourite personal projects because I love to travel and find myself spending a lot of time looking for cheap ticket.

Parts of this program were part of a tutorial in Angela Yu's 100 Days of Code Python course.

