import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "YOUR_STOCK_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACC_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_NUMBER = "YOUR_TWILIO_NUMBER"
RECIEVER_NUMBER = "MESSAGE_RECIEVER_NUMBER"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
dates = list(stock_data['Time Series (Daily)'].keys())
first_date = dates[0]
second_date = dates[1]
first_date_data = float(stock_data['Time Series (Daily)'][first_date]["4. close"])
second_date_data = float(stock_data['Time Series (Daily)'][second_date]["4. close"])
stock_difference = round((first_date_data - second_date_data) / second_date_data * 100, 2)
if abs(stock_difference) > 5:
    now = datetime.datetime.now()
    yesterday_date = (now - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_parameters = {
        "q": COMPANY_NAME,
        "from": yesterday_date,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in news_data["articles"][:3]:
        final_message = f"{STOCK}: {stock_difference}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        message = client.messages.create(
            body=final_message,
            from_=TWILIO_NUMBER,
            to=RECIEVER_NUMBER
        )
        print(message.status)