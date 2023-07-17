from gradio_client import Client

client = Client("https://gradio-blocks-hello.hf.space/")
result = client.predict(
				"Howdy!",	# str  in 'parameter_2' Textbox component
				fn_index=0
)
print(result)