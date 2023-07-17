# from gradio_client import Client

# client = Client("https://368f09ca0c818b44d0.gradio.live")
# result = client.predict(
# 				"Yerong",	# str  in 'parameter_3' Textbox component
# 				fn_index=0
# )
# print(result)
# print(type(result))
import requests

response = requests.post("https://tomsoderlund-rest-api-with-gradio.hf.space/run/predict", json={
  "data": [
    "hello world",
]}).json()

data = response["data"]