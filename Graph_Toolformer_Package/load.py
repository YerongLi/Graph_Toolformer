import pickle
# f = open('./graph_datasets/gpr', 'rb')
dataset = pickle.load(f)
f.close()
# print(dataset.keys())
# dict_keys(['data_profile', 'graph_set'])

# print(dataset['data_profile'])
# {'name': 'gpr', 'graph_number': 37, 'is_directed': False, 'is_weighted': False}

# print(dataset['graph_set'].keys())
# dict_keys(['dodecahedral_graph', 'desargues_graph', 'icosahedral_graph', 'binomial_tree', 'path_graph', 'house_x_graph', 'complete_graph', 'truncated_tetrahedron_graph', 'heawood_graph', 'bull_graph', 'sedgewick_maze_graph', 'turan_graph', 'hoffman_singleton_graph', 'full_rary_tree', 'circular_ladder_graph', 'star_graph', 'chvatal_graph', 'krackhardt_kite_graph', 'cycle_graph', 'ladder_graph', 'moebius_kantor_graph', 'diamond_graph', 'wheel_graph', 'tetrahedral_graph', 'house_graph', 'truncated_cube_graph', 'balanced_tree', 'tutte_graph', 'frucht_graph', 'lollipop_graph', 'cubical_graph', 'barbell_graph', 'petersen_graph', 'dorogovtsev_goltsev_mendes_graph', 'pappus_graph', 'circulant_graph', 'octahedral_graph'])



f = open('./graph_datasets/freebase', 'rb')
dataset = pickle.load(f)
f.close()
# print(dataset.keys())