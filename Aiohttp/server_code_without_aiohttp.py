import requests


r = 2

url = "http://localhost:8080/{}"
for i in range(r):
    response = requests.get(url.format(i))
    delay = response.headers.get("DELAY")
    date = response.headers.get("DATE")
    print("{}:{} delay {}".format(date, response.url, delay))