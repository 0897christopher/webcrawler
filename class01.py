import requests

url = "https://www.books.com.tw"
data = requests.get(url)

print(data)

print(data.status_code)

print(data.text)