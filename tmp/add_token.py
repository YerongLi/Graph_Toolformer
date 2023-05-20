from transformers import BertTokenizerFast, BertModel
import torch
from torch import nn
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
vectors = tokenizer.tokenize("[CLS] Hello world, how are you?")
print(vectors)
vectors = tokenizer.tokenize("<yerongAPI> Hello world, how are you?</yerongAPI>")
print(vectors)
