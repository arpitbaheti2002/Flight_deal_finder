import requests
import datetime as dt

class DataManager():
    def __init__(self):
        self.SHEETY_API_ENDPOINT = "https://api.sheety.co/943e441392e49c0529e49ced204ab673/flightDeals"
        self.SHEETY_AUTHENTICATION_HEADER = {
            "Authorization": "Bearer FlightDealer"
        }

    def get_sheet_data(self)->dict:
        response = requests.get(f"{self.SHEETY_API_ENDPOINT}/prices", headers=self.SHEETY_AUTHENTICATION_HEADER)
        response.raise_for_status()
        data = response.json()["prices"]
        return data
    
    def put_sheet_data(self, updated_data:dict):
        new_data = {
            "price":{
                "iataCode":updated_data["iataCode"]
            }
        }
        response = requests.put(url=f"{self.SHEETY_API_ENDPOINT}/{updated_data['id']}", json=new_data, headers=self.SHEETY_AUTHENTICATION_HEADER)
        response.raise_for_status()

    def get_dates(self)->tuple:
        date_tomorrow = dt.datetime.now() + dt.timedelta(days=1)
        date_tomorrow = date_tomorrow.strftime('%d/%m/%Y')
        date_six_months = dt.datetime.now() + dt.timedelta(days=6*30)
        date_six_months = date_six_months.strftime('%d/%m/%Y')

        return (date_tomorrow, date_six_months)
    
    def get_emails(self):
        response = requests.get(f"{self.SHEETY_API_ENDPOINT}/users", headers=self.SHEETY_AUTHENTICATION_HEADER)
        response.raise_for_status()
        data = response.json()["users"]
        emails = [row['email'] for row in data]
        return emails