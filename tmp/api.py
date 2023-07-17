from gradio_client import Client

client = Client("https://0c53c70ee482bf1dc0.gradio.live")
result = client.predict(
				"Yerong",	# str  in 'parameter_3' Textbox component
				fn_index=0
)
print(result)