from gradio_client import Client

client = Client("https://d71322c8759610f657.gradio.live/")
result = client.predict(
				"Howdy!",	# str  in 'parameter_3' Textbox component
				fn_index=0
)
print(result)