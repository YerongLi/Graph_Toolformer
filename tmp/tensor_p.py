import transformers
import tensor_parallel as tp
model_name_or_path = '/scratch/yerong/.cache/pyllama/hf/7B'
# tokenizer = transformers.AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name_or_path)
# model = transformers.AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-2.7B")  # use opt-125m for testing
model = transformers.AutoModelForCausalLM.from_pretrained(model_name_or_path)  # use opt-125m for testing

model = tp.tensor_parallel(model, ["cuda:0", "cuda:1","cuda:2", "cuda:3"])  # <- each GPU has half the weights

print('model')
inputs = tokenizer("A cat sat", return_tensors="pt")["input_ids"].to("cuda:0")

outputs = model.generate(inputs, num_beams=5)

print(tokenizer.decode(outputs[0])) # A cat sat on my lap for a few minutes ...

model(input_ids=inputs, labels=inputs).loss.backward()  # training works as usual