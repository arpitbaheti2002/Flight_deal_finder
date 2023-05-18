import requests
from flight_data import FlightData

class FlightSearch():
    def __init__(self):
        self.TEQUILA_API = "https://api.tequila.kiwi.com/"
        self.TEQUILA_API_HEADER = {
            "apikey" : "L5N98Nk_x2Iji1l6Y-IU_2mOyYRqbRS7"
        }

    def get_IATA_code(self, city:str)->str:
        location_search_params = {
            "term": city
        }
        response = requests.get(f"{self.TEQUILA_API}locations/query", params=location_search_params, headers=self.TEQUILA_API_HEADER)
        response.raise_for_status()
        data = response.json()['locations'][0]
        city_code = data['code']
        return city_code
    
    def search_flight(self, origin:str, destination:str, from_date:str, to_date:str):
        search_params = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        search_end_point = f"{self.TEQUILA_API}v2/search"
        response = requests.get(url=search_end_point, params=search_params, headers=self.TEQUILA_API_HEADER)
        response.raise_for_status()
        try:
            flight_data = response.json()['data'][0]
            flight_data = FlightData(
                price=flight_data['price'],
                origin_city=flight_data['cityFrom'],
                origin_airport=flight_data['flyFrom'],
                destination_city=flight_data['cityTo'],
                destination_airport=flight_data['flyTo'],
                out_date=flight_data["route"][0]["local_departure"].split("T")[0],
                return_date=flight_data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: Rs.{flight_data.price}")
            return flight_data
        
        except IndexError:
            print(f"{destination} : No flights found")
            return None
        