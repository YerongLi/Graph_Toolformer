# import gradio as gr
# import mdtex2html

# import os
# import torch
# from transformers import AutoModel, AutoTokenizer

# # from transformers import HfApi
# os.environ["HUGGINGFACE_TOKEN"] = "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"
# # api = HfApi(token="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")
# # apitoken= "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"
# checkpoint = "umiuni/hp"
# # checkpoint = "/innev/open-ai/huggingface/models/THUDM/chatglm-6b-int4"
# tokenizer = AutoTokenizer.from_pretrained(checkpoint, trust_remote_code=True)
# # model = AutoModel.from_pretrained(checkpoint, trust_remote_code=True).float()


# # Check if a GPU is available
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# # Load the model
# model = AutoModel.from_pretrained(checkpoint, trust_remote_code=True).to(device)

# # Convert the model to half precision (FP16) if using GPU
# if device.type == "cuda":
#     model = model.half()
# else:
#     model = model.float()

# # Verify the device type and model datatype
# print("Device type:", device.type)
# print("Model datatype:", model.parameters().__next__().dtype)


# # model = AutoModel.from_pretrained(checkpoint, trust_remote_code=True).half().to('mps')
# model = model.eval()

# """Override Chatbot.postprocess"""
# buffered_history = [
#     ("Welcome, Harry Potter, the greatest wizard from Hogwarts!", ""),
#     ("Harry, what is your favorite spell that you've learned at Hogwarts?", "Expelliarmus has always been a favorite of mine."),
#     ("Which magical artifact or object from the wizarding world do you find the most intriguing?", "The Marauder's Map has always fascinated me."),
#     ("If you could spend a day with any character from Hogwarts history, who would it be and why?", "I would love to spend a day with Godric Gryffindor."),
#     ("Among all the Quidditch matches you've played, which one stands out as the most memorable for you?", "The match against Slytherin in my third year was particularly memorable."),
#     ("If you had the chance to learn one additional branch of magic, like Divination or Ancient Runes, which would you choose and why?", "I would choose Ancient Runes."),
#     ("Who is your favorite professor at Hogwarts when it comes to teaching Defense Against the Dark Arts?", "Professor Lupin is definitely my favorite."),
#     ("If you could visit any magical location in the wizarding world that you haven't been to yet, where would you go?", "I would love to visit the Ministry of Magic and see the Department of Mysteries."),
#     ("Which character from the wizarding world, besides your close friends, do you admire the most and why?", "Neville Longbottom is someone I greatly admire."),
#     ("Among the various magical creatures you encountered, which one did you find the most challenging to deal with?", "The Hungarian Horntail dragon during the Triwizard Tournament was incredibly challenging."),
#     ("If you could give one piece of advice to young witches and wizards starting their magical education, what would it be?", "I would advise them to believe in themselves and not be afraid to ask for help when needed.")
# ]

# def truncate_history(history):
#     total_words = 0
#     selected_history = []

#     for i in range(len(history)-1, -1, -1):
#         question, answer = history[i]
#         words = len(question.split()) + len(answer.split())

#         if total_words + words <= 1800:
#             selected_history.append((question, answer))
#             total_words += words
#         else:
#             break

#     return selected_history

# def postprocess(self, y):
#     if y is None:
#         return []
#     for i, (message, response) in enumerate(y):
#         y[i] = (
#             None if message is None else mdtex2html.convert((message)),
#             None if response is None else mdtex2html.convert(response),
#         )
#     return y


# gr.Chatbot.postprocess = postprocess


# def parse_text(text):
#     """copy from https://github.com/GaiZhenbiao/ChuanhuChatGPT/"""
#     lines = text.split("\n")
#     lines = [line for line in lines if line != ""]
#     count = 0
#     for i, line in enumerate(lines):
#         if "```" in line:
#             count += 1
#             items = line.split('`')
#             if count % 2 == 1:
#                 lines[i] = f'<pre><code class="language-{items[-1]}">'
#             else:
#                 lines[i] = f'<br></code></pre>'
#         else:
#             if i > 0:
#                 if count % 2 == 1:
#                     line = line.replace("`", "\`")
#                     line = line.replace("<", "&lt;")
#                     line = line.replace(">", "&gt;")
#                     line = line.replace(" ", "&nbsp;")
#                     line = line.replace("*", "&ast;")
#                     line = line.replace("_", "&lowbar;")
#                     line = line.replace("-", "&#45;")
#                     line = line.replace(".", "&#46;")
#                     line = line.replace("!", "&#33;")
#                     line = line.replace("(", "&#40;")
#                     line = line.replace(")", "&#41;")
#                     line = line.replace("$", "&#36;")
#                 lines[i] = "<br>"+line
#     text = "".join(lines)
#     return text


# def predict(input, chatbot, max_length, top_p, temperature, history):
#     chatbot.append((parse_text(input), ""))
#     modified_history = truncate_history(buffered_history + history)
#     for response, history in model.stream_chat(tokenizer, input, modified_history, max_length=max_length, top_p=top_p,
#                                                temperature=temperature):
#         chatbot[-1] = (parse_text(input), parse_text(response))       

#         yield chatbot, history


# def reset_user_input():
#     return gr.update(value='')


# def reset_state():
#     return [], []


# # with gr.Blocks() as demo:
# #     gr.HTML("""<h1 align="center">Demo : Harry Potter</h1>""")

# #     chatbot = gr.Chatbot()
# #     with gr.Row():
# #         with gr.Column(scale=4):
# #             with gr.Column(scale=12):
# #                 user_input = gr.Textbox(show_label=False, placeholder="Input...", lines=10).style(
# #                     container=False)
# #             with gr.Column(min_width=32, scale=1):
# #                 submitBtn = gr.Button("Submit", variant="primary")
# #         with gr.Column(scale=1):
# #             emptyBtn = gr.Button("Clear History")
# #             max_length = gr.Slider(0, 4096, value=2000, step=1.0, label="Maximum length", interactive=True)
# #             top_p = gr.Slider(0, 1, value=0.2, step=0.01, label="Top P", interactive=True)
# #             temperature = gr.Slider(0, 1, value=0.95, step=0.01, label="Temperature", interactive=True)

# #     history = gr.State([])

# #     submitBtn.click(predict, [user_input, chatbot, max_length, top_p, temperature, history], [chatbot, history],
# #                     show_progress=True)
# #     submitBtn.click(reset_user_input, [], [user_input])

# #     emptyBtn.click(reset_state, outputs=[chatbot, history], show_progress=True)

# demo.queue().launch(share=True, inbrowser=True)
# import gradio as gr


# def welcome(input):
#     query = input['query']
#     # history = gr.State(input['history'])
#     history = input['history']
#     history.append(f"Welcome to Gradio, {query}!")
#     return history

# iface = gr.Interface(fn=welcome, inputs=gr.JSON(), outputs=gr.JSON())

# if __name__ == "__main__":
#     iface.launch()

# import gradio as gr

# def welcome(input, history):
#     query = input['query']
#     history.append(f"Welcome to Gradio, {query}!")
#     return history

# def goodbye(input, history):
#     query = input['query']
#     history.append(f"Goodbye, {query}!")
#     return history

# with gr.blocks.Interface() as iface1, gr.blocks.Interface() as iface2:
#     # Interface 1
#     query_input1 = gr.inputs.Textbox(label="Query")
#     history_input1 = gr.inputs.State(label="History", type=list, initial_value=[])
#     output1 = gr.outputs.State(type=list)

#     iface1.add_input("query", query_input1)
#     iface1.add_input("history", history_input1)
#     iface1.add_output("history", output1)

#     iface1.func(welcome)
    
#     # Interface 2
#     query_input2 = gr.inputs.Textbox(label="Query")
#     history_input2 = gr.inputs.State(label="History", type=list, initial_value=[])
#     output2 = gr.outputs.State(type=list)

#     iface2.add_input("query", query_input2)
#     iface2.add_input("history", history_input2)
#     iface2.add_output("history", output2)

#     iface2.func(goodbye)

#     # Share interfaces and launch
#     iface1_url = iface1.share(share=True)
#     iface2_url = iface2.share(share=True)

#     gr.Interface.launch_multiple([iface1_url, iface2_url])




import gradio as gr
import mdtex2html
def welcome(input):
    query = input
    history = input['history']
    history.append(f"Welcome to Gradio, {query}!")
    return {'history': history}

def reset_state():
    return {'history': []}

def predict(user_input, chatbot, max_length, top_p, temperature, history):
    # Your predict function logic here
    return {}

def reset_user_input(user_input, chatbot, max_length, top_p, temperature, history):
    history.append(user_input)
    return user_input, history

with gr.Blocks() as demo:
    gr.HTML("""<h1 align="center">ChatGLM</h1>""")

    chatbot = gr.Chatbot()

    with gr.Row():
        with gr.Column(scale=4):
            with gr.Column(scale=12):
                user_input = gr.Textbox(show_label=False, placeholder="Input...", lines=10).style(container=False)
            with gr.Column(min_width=32, scale=1):
                submitBtn = gr.Button("Submit", variant="primary")
        with gr.Column(scale=1):
            emptyBtn = gr.Button("Clear History")
            max_length = gr.Slider(0, 4096, value=2048, step=1.0, label="Maximum length", interactive=True)
            top_p = gr.Slider(0, 1, value=0.7, step=0.01, label="Top P", interactive=True)
            temperature = gr.Slider(0, 1, value=0.95, step=0.01, label="Temperature", interactive=True)

    history = gr.State([])

    submitBtn.click(predict, [user_input, chatbot, max_length, top_p, temperature, history], [chatbot, history], show_progress=True)
    submitBtn.click(reset_user_input)
    emptyBtn.click(reset_state, outputs=[chatbot, history], show_progress=True)

# iface = gr.Interface(fn=welcome, inputs='text', outputs=gr.JSON(), blocks=demo)

if __name__ == "__main__":
    demo.launch(share=True)
