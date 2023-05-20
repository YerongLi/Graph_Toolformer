from transformers import BertTokenizerFast, BertModel
import torch
from torch import nn
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
vectors = tokenizer.tokenize("[CLS] Hello world, how are you?")
print(vectors)
vectors = tokenizer.tokenize("<yerongAPI> Hello world, how are you?</yerongAPI>")
print('original_vector')
print(vectors)
tokenizer.add_tokens(['<yerongAPI>','</yerongAPI>'])
vectors = tokenizer.tokenize("<yerongAPI> Hello world, how are you?</yerongAPI>")
print('vectors after add')
print(vectors)

tokenized = tokenizer("<yerongAPI> Hello world, how are you?</yerongAPI>",add_special_tokens=False, return_tensors="pt")

print(tokenized['input_ids'])

tkn = tokenized['input_ids'][0][0]
print("First token:", tkn)
print("Decoded:", tokenizer.decode(tkn))

print('Special token', tokenizer.decode(101))
print('Special token', tokenizer.decode(102))


print('=' * 17)
model = BertModel.from_pretrained('bert-base-uncased')

print(model.embeddings)