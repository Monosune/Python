import requests
import smtplib

my_email = "thiagoassisdecarvalho@gmail.com"
password = "aeznagajenhajsho"

API_KEY = "1QYLEKFC52NO3AJ9"
NEWS_API_KEY = "da3eccacc5544a58bfce529c62328cbc"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

request = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey={API_KEY}")
request.raise_for_status()
stock_data = request.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

yesterday = data_list[0]
yesterday_close = yesterday["4. close"]
after_that = data_list[1]
after_that_close = after_that["4. close"]

final = round(abs(float(yesterday_close) - float(after_that_close)), 2)
print(final)

percentage_difference = round(100 * (final / float(after_that_close)), 2)

print(percentage_difference)


articles = []
brief = []

if percentage_difference > 2:
    print("Get News")
    request_news = requests.get(url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}&qInTitle={COMPANY_NAME}")
    request_news.raise_for_status()
    data_news = request_news.json()["articles"]
    news_articles = data_news[:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_articles]

    print(formatted_articles[0])
    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Changes on stock market by {percentage_difference}!\n\n{article}"
            )

