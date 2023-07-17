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
$
$ curl -X POST https://hf.space/embed/versae/gradio-blocks-rest-api/+/api/predict/ -H 'Content-Type: application/json' -d '{"data": ["Jessie"], "fn_index": 1}'
```""")


import gradio as gr
import mdtex2html

import os
import torch
from transformers import AutoModel, AutoTokenizer

# from transformers import HfApi
os.environ["HUGGINGFACE_TOKEN"] = "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"
# api = HfApi(token="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")
# apitoken= "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"
checkpoint = "umiuni/hp"
# checkpoint = "/innev/open-ai/huggingface/models/THUDM/chatglm-6b-int4"
tokenizer = AutoTokenizer.from_pretrained(checkpoint, trust_remote_code=True)
# model = AutoModel.from_pretrained(checkpoint, trust_remote_code=True).float()


# Check if a GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the model
model = AutoModel.from_pretrained(checkpoint, trust_remote_code=True).to(device)

# Convert the model to half precision (FP16) if using GPU
if device.type == "cuda":
    model = model.half()
else:
    model = model.float()
history = []
# Verify the device type and model datatype
print("Device type:", device.type)
print("Model datatype:", model.parameters().__next__().dtype)


# model = AutoModel.from_pretrained(checkpoint, trust_remote_code=True).half().to('mps')
model = model.eval()

"""Override Chatbot.postprocess"""

buffered_history = [
    ("Welcome, Harry Potter, the greatest wizard from Hogwarts!", ""),
    ("Harry, what is your favorite spell that you've learned at Hogwarts?", "Expelliarmus has always been a favorite of mine."),
    ("Which magical artifact or object from the wizarding world do you find the most intriguing?", "The Marauder's Map has always fascinated me."),
    ("If you could spend a day with any character from Hogwarts history, who would it be and why?", "I would love to spend a day with Godric Gryffindor."),
    ("Among all the Quidditch matches you've played, which one stands out as the most memorable for you?", "The match against Slytherin in my third year was particularly memorable."),
    ("If you had the chance to learn one additional branch of magic, like Divination or Ancient Runes, which would you choose and why?", "I would choose Ancient Runes."),
    ("Who is your favorite professor at Hogwarts when it comes to teaching Defense Against the Dark Arts?", "Professor Lupin is definitely my favorite."),
    ("If you could visit any magical location in the wizarding world that you haven't been to yet, where would you go?", "I would love to visit the Ministry of Magic and see the Department of Mysteries."),
    ("Which character from the wizarding world, besides your close friends, do you admire the most and why?", "Neville Longbottom is someone I greatly admire."),
    ("Among the various magical creatures you encountered, which one did you find the most challenging to deal with?", "The Hungarian Horntail dragon during the Triwizard Tournament was incredibly challenging."),
    ("If you could give one piece of advice to young witches and wizards starting their magical education, what would it be?", "I would advise them to believe in themselves and not be afraid to ask for help when needed.")
]
def truncate_history(history):
    total_words = 0
    selected_history = []

    for i in range(len(history)-1, -1, -1):
        question, answer = history[i]
        words = len(question.split()) + len(answer.split())

        if total_words + words <= 1800:
            selected_history.append((question, answer))
            total_words += words
        else:
            break

    return selected_history

def postprocess(self, y):
    if y is None:
        return []
    for i, (message, response) in enumerate(y):
        y[i] = (
            None if message is None else mdtex2html.convert((message)),
            None if response is None else mdtex2html.convert(response),
        )
    return y


gr.Chatbot.postprocess = postprocess


def parse_text(text):
    """copy from https://github.com/GaiZhenbiao/ChuanhuChatGPT/"""
    lines = text.split("\n")
    lines = [line for line in lines if line != ""]
    count = 0
    for i, line in enumerate(lines):
        if "```" in line:
            count += 1
            items = line.split('`')
            if count % 2 == 1:
                lines[i] = f'<pre><code class="language-{items[-1]}">'
            else:
                lines[i] = f'<br></code></pre>'
        else:
            if i > 0:
                if count % 2 == 1:
                    line = line.replace("`", "\`")
                    line = line.replace("<", "&lt;")
                    line = line.replace(">", "&gt;")
                    line = line.replace(" ", "&nbsp;")
                    line = line.replace("*", "&ast;")
                    line = line.replace("_", "&lowbar;")
                    line = line.replace("-", "&#45;")
                    line = line.replace(".", "&#46;")
                    line = line.replace("!", "&#33;")
                    line = line.replace("(", "&#40;")
                    line = line.replace(")", "&#41;")
                    line = line.replace("$", "&#36;")
                lines[i] = "<br>"+line
    text = "".join(lines)
    return text


def predict(input, max_length=2000, top_p=0.25, temperature=0.85):
    global history
    history = []
    modified_history = truncate_history(buffered_history + history)
    
    for response, new_history in model.stream_chat(tokenizer, input, modified_history, max_length=max_length, top_p=top_p, temperature=temperature):
        # chatbot[-1] = (parse_text(input), parse_text(response))
        # history.append(response)
        continue
        # print(parse_text(input), parse_text(response))
    history.append((parse_text(input), parse_text(response)))
    print(history)
    ans = [''] * 20
    count = 0
    for entry in reversed(history):
        if entry in buffered_history:
            continue
        ans[-count * 2 - 2] = entry[0]
        ans[-count * 2 - 1] = entry[1]
        count += 1
        if count == 20: break

    print(ans)

    return ans


def reset_user_input():
    return gr.update(value='')


def reset_state():
    return [], []


iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Textbox(lines=10, placeholder="Input...", label=None).style(container_width="70%"),
        # gr.State([]),
        gr.Slider(0, 4096, value=2000, step=1.0, label="Maximum length", interactive=True),
        gr.Slider(0, 1, value=0.25, step=0.01, label="Top P", interactive=True),
        gr.Slider(0, 1, value=0.95, step=0.01, label="Temperature", interactive=True),
    ],
    # outupts = gr.outputs.List[str],
    # outputs='list',
    # outputs = gr.outputs.Dataframe('auto),

    outputs=['text'] * 20,
    layout="vertical",
    title="Demo : Harry Potter"
)

iface.queue().launch(share=False, inbrowser=True)