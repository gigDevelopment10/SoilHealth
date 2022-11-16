import requests
import json

class DecodeJSON(object):
    def __init__(self, data):
	    self.__dict__ = json.loads(data)

class MakeApiCall:

    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def get_user_data(self, api, parameters):
        response = requests.post(f"{api}", params=parameters)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
        # dj = DecodeJSON(text) 
        # print(dj.properties["layers"][0]['depths'][0])
        # print(dj.properties["layers"][0]['depths'][1])
        # print(dj.properties["layers"][0]['depths'][2])
        # print(dj.properties["layers"][0]['depths'][3])

    def __init__(self, api):
        parameters = {
            "username": "kedark"
        }


if __name__ == "__main__":
    # lat = input("Enter Latitude: ")
    # long = input("Enter Longititude: ")

    parameters = {
            "Lat": "22.860485",
            "Long" : "75.691551"
        }
    api_call = MakeApiCall("http://127.0.0.1:5000/")
    api_call.get_user_data("http://127.0.0.1:5000/post", parameters)