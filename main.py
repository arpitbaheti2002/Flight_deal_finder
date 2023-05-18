from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

DEPARTURE_CITY = "New Delhi"
ORIGIN_AIRPORT_CODE = flight_search.get_IATA_code(DEPARTURE_CITY)

sheet_data = data_manager.get_sheet_data()
emails = data_manager.get_emails()


for destination in sheet_data:
    if not destination["iataCode"]:
        destination["iataCode"]=flight_search.get_IATA_code(destination["city"])
        data_manager.put_sheet_data(destination)

dates = data_manager.get_dates()

for destination in sheet_data:
    flight = flight_search.search_flight(ORIGIN_AIRPORT_CODE, destination['iataCode'], str(dates[0]), str(dates[1]))

    if flight and flight.price < destination['lowestPrice']:
        notification_manager.send_sms(
            f"Low price alert! Only Rs{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
        
        message = f"Low price alert! Only Rs{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        
        notification_manager.send_emails(emails, message)
        
        
