import requests
from datetime import datetime

USERNAME = "nest0r171"
TOKEN = "h241hj241hj21bnm"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # Setting up an account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "H",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()

# Creating a pixel on a graph
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)


# # Updating the pixel's quantity
# update_data = {
#     "quantity": "2"
# }
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240103"
# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)


# # Deleting a pixel
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240103"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
