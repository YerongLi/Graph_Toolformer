import requests

data = requests.post(
    url="https://hf.space/embed/versae/gradio-blocks-rest-api/+/api/predict/", json={"data": ["Jessie"], "fn_index": 0}
).json()
print(data)
requests.post(
    url="https://hf.space/embed/versae/gradio-blocks-rest-api/+/api/predict/", json={"data": ["Jessie"], "fn_index": 1}
).json()