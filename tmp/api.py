from gradio_client import Client

client = Client("https://umiuni-harry-potter.hf.space/")
result = client.predict(
				"Hi, what's your name!",	# str  in 'parameter_6' Textbox component
				"data.json",	# str (filepath to JSON file) in 'parameter_2' Chatbot component
				0,	# int | float (numeric value between 0 and 4096) in 'Maximum length' Slider component
				0,	# int | float (numeric value between 0 and 1) in 'Top P' Slider component
				0,	# int | float (numeric value between 0 and 1) in 'Temperature' Slider component
				fn_index=0
)
print(result)