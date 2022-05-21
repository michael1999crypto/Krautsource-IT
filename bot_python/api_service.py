import json
import requests

# send a post request with json payload


url = "https://localhost:5001/api/datas"

def send_data(data):
    #make it https
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
    print(r.text)

test_data = {
  "typeOfData": "people_in_train_station",
  "value": "12",
  "position": {
    "longitude": 43.000000,
    "latitude": 12.000000
  }
}