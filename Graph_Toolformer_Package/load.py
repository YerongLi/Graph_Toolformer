import pickle
f = open('./graph_datasets/gpr', 'rb')
dataset = pickle.load(f)
f.close()
print(dataset.keys())
# print(dataset['data_profile'])
# {'name': 'gpr', 'graph_number': 37, 'is_directed': False, 'is_weighted': False}
print(dataset['graph_set'].keys())
