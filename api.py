
import requests
isbn='1416949658'
response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn).json()

response = response["items"][0]
response = response["volumeInfo"]

title = response["title"]

description = response["description"]

print(f"{title}: {description}")