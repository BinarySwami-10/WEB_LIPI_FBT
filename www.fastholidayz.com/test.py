import requests
import json
import pprint

print = pprint.pprint


def get_flights(**kwargs):
    endpoint = 'http://localhost:8000/api/fs'
    resp = requests.get(endpoint, params=kwargs).json()
    # print(json.dumps(resp, indent=4))
    return resp


def book_flight(booksegment):
    endpoint = 'https://stagingapi.easemytrip.com/Flight.svc/json/AirBookRQ'
    paymentDetail = {
        "PaymentDetails": {
            "BookingAmount": 12445,
            "BookingCurrencyCode": "INR"
            }
        }
    transactionId = {"TransactionId": "65765765", }
    traveler = {
        "Traveller": {
            "AdultTraveller": [
                {
                    "CountryCode": "IN",
                    "DOB": "1970-01-01",
                    "EmailAddress": "rahulradhakrishnan.provab@gmail.com",
                    "FirstName": "Rahul",
                    "FrequentFlierNumber": "",
                    "Gender": 0,
                    "LastName": "Nair",
                    "MiddleName": "",
                    "MobileNumber": "918123992558",
                    "Nationality": "India",
                    "PassportExpiryDate": "1970-01-01",
                    "PassportNo": None,
                    "ResidentCountry": "India",
                    "Title": "Mr"
                    }
                ]
            }
        }
    resp = requests.post(endpoint, params=kwargs).json()
    print(resp)
    return resp


if __name__ == '__main__':
    params = {'src': 'DEL', 'dst': 'HYD', 'fromdate': '2022-06-02'}
    filghtInfo = get_flights(**params)
    booksegment = filghtInfo['Journeys'][0]['Segments'][0]
    book_flight(booksegment)
    print(booksegment)
