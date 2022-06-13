from django.test import Client

client = Client()
response = client.get('http://127.0.0.1:8000/')
print(response.status_code)
