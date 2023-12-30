import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC3f70d5a3f77e70ea0bbb82f0167abf09"
auth_token = os.environ.get("AUTH_TOKEN")


parameters = {
"lat": 53.023633,
"lon": 18.613249,
"appid": api_key,
"cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_=os.environ.get("MY_NUMBER"),
        to="+48513732434"
    )
    print(message.status)


