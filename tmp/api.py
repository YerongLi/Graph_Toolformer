# from gradio_client import Client

# client = Client("https://umiuni-harry-potter.hf.space/")
# result = client.predict(
# 				"Hi, what's your name!",	# str  in 'parameter_6' Textbox component
# 				'data.json',
# 				2000,	# int | float (numeric value between 0 and 4096) in 'Maximum length' Slider component
# 				0.8,	# int | float (numeric value between 0 and 1) in 'Top P' Slider component
# 				0.1,	# int | float (numeric value between 0 and 1) in 'Temperature' Slider component
# 				fn_index=0
# )
# print(result)
# print(type(result))


from gradio_client import Client

client = Client("https://70f64738fbdcce365d.gradio.live/")
result = client.predict(
				"Howdy!",	# str  in 'input' Textbox component
				0,	# int | float (numeric value between 0 and 4096) in 'Maximum length' Slider component
				0,	# int | float (numeric value between 0 and 1) in 'Top P' Slider component
				0,	# int | float (numeric value between 0 and 1) in 'Temperature' Slider component
				api_name="/predict"
)
print(result)
print(type(result))