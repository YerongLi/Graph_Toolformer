# # from gradio_client import Client
# Make a request to the Gradio API endpoint
import requests
response = requests.post("http://127.0.0.1:7860/api/predict", json={
    "data": ["hello world", []],
}).json()

print(response)
data = response["data"]
print(data)
print(type(data))

# # response = requests.post("https://tomsoderlund-rest-api-with-gradio.hf.space/run/predict", json={
# #   "data": [
# #     "hello world",
# # ]}).json()

# # data = response["data"]
# # print(data)
# # print(type(data))

# import requests

# data = requests.post(
#     url="https://hf.space/embed/versae/gradio-blocks-rest-api/+/api/predict/", json={"data": ["Jessie"], "fn_index": 0}
# ).json()
# print(data)

# data = requests.post(
#     url="https://hf.space/embed/versae/gradio-blocks-rest-api/+/api/predict/", json={"data": ["Jessie"], "fn_index": 1}
# ).json()
# print(data)
