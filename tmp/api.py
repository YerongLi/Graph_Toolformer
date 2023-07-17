# # from gradio_client import Client
# import requests

# response = requests.post("https://368f09ca0c818b44d0.gradio.live/run/predict", json={
#   "data": [
#     "hello world",
# ]}).json()

# print(response)
# data = response["data"]
# print(data)
# print(type(data))

# # client = Client("https://368f09ca0c818b44d0.gradio.live")
# # result = client.predict(
# # 				"Yerong",	# str  in 'parameter_3' Textbox component
# # 				fn_index=0
# # )
# # print(result)
# # print(type(result))
# # import requests

# # response = requests.post("https://tomsoderlund-rest-api-with-gradio.hf.space/run/predict", json={
# #   "data": [
# #     "hello world",
# # ]}).json()

# # data = response["data"]
# # print(data)
# # print(type(data))

import requests

data = requests.post(
    url="https://hf.space/embed/versae/gradio-blocks-rest-api/+/api/predict/", json={"data": ["Jessie"], "fn_index": 0}
).json()
print(data)

data = 
requests.post(
    url="https://hf.space/embed/versae/gradio-blocks-rest-api/+/api/predict/", json={"data": ["Jessie"], "fn_index": 1}
).json()
print(data)
