import requests
import os
from datetime import date

USERNAME = os.environ.get("PIX_USERNAME")
TOKEN = os.environ.get("PIX_TOKEN")

GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPHS_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

# C r e a t e   a c c o u n t
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

# C r e a t e   g r a p h
graph_params = {
    "id": GRAPH_ID,
    "name": "Workout Graph",
    "unit": "Min",
    "type": "float",
    "color": "shibafu",
}

# response_graph = requests.post(url=GRAPHS_ENDPOINT, json=graph_params, headers=headers)

# C r e a t e   p i x e l
today = date.today()
today = str(today).replace('-', '')

pixel_params = {
    "date": today,
    "quantity": input("How many minutes did you work out today?"),
}

# response_pixel = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)

# U p d a t e   P i x e l
# response_update_pixel = requests.put(url=f"{PIXEL_ENDPOINT}/{today}", json=pixel_params, headers=headers)

# D e l e t e   P i x e l
# response_delete_pixel = requests.delete(url=f"{PIXEL_ENDPOINT}/{today}", headers=headers)

