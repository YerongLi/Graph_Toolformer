import pickle
f = open('./graph_datasets/gpr', 'rb')
dataset = pickle.load(f)
f.close()
print(dataset.keys())
print(dataset['data_profile'])