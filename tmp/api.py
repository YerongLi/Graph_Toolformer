from gradio_client import Client

# client = Client("https://umiuni-harry-potter.hf.space/")
# result = client.predict(
# 				"Hi, what's your name!",	# str  in 'parameter_6' Textbox component
# 				2000,	# int | float (numeric value between 0 and 4096) in 'Maximum length' Slider component
# 				0.25,	# int | float (numeric value between 0 and 1) in 'Top P' Slider component
# 				0.95,	# int | float (numeric value between 0 and 1) in 'Temperature' Slider component
# 			    api_name="/predict"

# )
# print(result[-1])
# print(type(result))


# from gradio_client import Client

# client = Client("https://3c9ac38701a3cd6744.gradio.live/")
# result = client.predict(
# 				"Howdy!",	# str  in 'input' Textbox component
# 				0,	# int | float (numeric value between 0 and 4096) in 'Maximum length' Slider component
# 				0,	# int | float (numeric value between 0 and 1) in 'Top P' Slider component
# 				0,	# int | float (numeric value between 0 and 1) in 'Temperature' Slider component
# 				api_name="/predict"
# )
# print(result)
# print(type(result))

from gradio_client import Client

from gradio_client import Client

client = Client("https://d712cc3fbf45b36e85.gradio.live/")
print(result)
result = client.predict(
				"Who are you?",	# str  in 'parameter_6' Textbox component
				"data.json",	# str (filepath to JSON file) in 'parameter_2' Chatbot component
				2000.,	# int | float (numeric value between 0 and 4096) in 'Maximum length' Slider component
				0.5,	# int | float (numeric value between 0 and 1) in 'Top P' Slider component
				0.5,	# int | float (numeric value between 0 and 1) in 'Temperature' Slider component
				fn_index=0
)
print(result)