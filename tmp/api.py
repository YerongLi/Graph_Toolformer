from gradio_client import Client

client = Client("https://368f09ca0c818b44d0.gradio.live")
result = client.predict(
				"Yerong",	# str  in 'parameter_3' Textbox component
				fn_index=0
)
print(result)
print(type(result))