import gradio as gr
import inspect
from gradio import routes
from typing import List, Type

# Monkey patch
def get_types(cls_set: List[Type], component: str):
    docset = []
    types = []
    if component == "input":
        for cls in cls_set:
            doc = inspect.getdoc(cls)
            doc_lines = doc.split("\n")
            docset.append(doc_lines[1].split(":")[-1])
            types.append(doc_lines[1].split(")")[0].split("(")[-1])
    else:
        for cls in cls_set:
            doc = inspect.getdoc(cls)
            doc_lines = doc.split("\n")
            docset.append(doc_lines[-1].split(":")[-1])
            types.append(doc_lines[-1].split(")")[0].split("(")[-1])
    return docset, types
routes.get_types = get_types

# App code
def hallo(x):
    return f"Hallo, {x}"

def hadet(x):
    return f"Hadet, {x}"

with gr.Blocks() as blk:
    gr.Markdown("# Gradio Blocks (3.0) with REST API")
    t = gr.Textbox()
    b = gr.Button("Hallo")
    a = gr.Button("Hadet")
    o = gr.Textbox()
    b.click(hallo, inputs=[t], outputs=[o])
    a.click(hadet, inputs=[t], outputs=[o])
    gr.Markdown("""
## API
Can select which function to use by passing in `fn_index`:
```python
import requests

requests.post(
    url="https://hf.space/embed/versae/gradio-blocks-rest-api/+/api/predict/", json={"data": ["Jessie"], "fn_index": 0}
).json()
requests.post(
    url="https://hf.space/embed/versae/gradio-blocks-rest-api/+/api/predict/", json={"data": ["Jessie"], "fn_index": 1}
).json()
```

Or using cURL

```
$ curl -X POST https://hf.space/embed/versae/gradio-blocks-rest-api/+/api/predict/ -H 'Content-Type: application/json' -d '{"data": ["Jessie"], "fn_index": 0}'
$ curl -X POST https://hf.space/embed/versae/gradio-blocks-rest-api/+/api/predict/ -H 'Content-Type: application/json' -d '{"data": ["Jessie"], "fn_index": 1}'
```""")

ifa = gr.Interface(lambda: None, inputs=[t], outputs=[o])

blk.input_components = ifa.input_components
blk.output_components = ifa.output_components
blk.examples = None
blk.predict_durations = []

bapp = blk.launch()