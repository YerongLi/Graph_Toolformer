import pickle
# f = open('./graph_datasets/gpr', 'rb')
# dataset = pickle.load(f)
# f.close()
# print(dataset.keys())
# dict_keys(['data_profile', 'graph_set'])

# print(dataset['data_profile'])
# {'name': 'gpr', 'graph_number': 37, 'is_directed': False, 'is_weighted': False}

# print(dataset['graph_set'].keys())
# dict_keys(['dodecahedral_graph', 'desargues_graph', 'icosahedral_graph', 'binomial_tree', 'path_graph', 'house_x_graph', 'complete_graph', 'truncated_tetrahedron_graph', 'heawood_graph', 'bull_graph', 'sedgewick_maze_graph', 'turan_graph', 'hoffman_singleton_graph', 'full_rary_tree', 'circular_ladder_graph', 'star_graph', 'chvatal_graph', 'krackhardt_kite_graph', 'cycle_graph', 'ladder_graph', 'moebius_kantor_graph', 'diamond_graph', 'wheel_graph', 'tetrahedral_graph', 'house_graph', 'truncated_cube_graph', 'balanced_tree', 'tutte_graph', 'frucht_graph', 'lollipop_graph', 'cubical_graph', 'barbell_graph', 'petersen_graph', 'dorogovtsev_goltsev_mendes_graph', 'pappus_graph', 'circulant_graph', 'octahedral_graph'])



# f = open('./graph_datasets/freebase', 'rb')
# dataset = pickle.load(f)
# f.close()
# print(dataset.keys())
# dict_keys(['data_profile', 'nodes', 'links'])
# print(dataset['links'])
# How he can make sure that he can prune anything
# ('/m/0dgpwnk', '/m/0h7x'): {'label': ['/film/film/release_date_s./film/film_regional_release_date/film_release_region']}, ('/m/0f42nz', '/m/03f02ct'): {'label': ['/film/film/starring./film/performance/actor']}, ('/m/047myg9', '/m/01tz6vs'): {'label': ['/film/film/subjects']}, ('/m/02t4yc', '/m/019v9k'): {'label': ['/education/educational_institution/students_graduates./education/education/degree']}, ('/m/0168nq', '/m/08mbj5d'): {'label': ['/common/topic/webpage./common/webpage/category']}, ('/m/020h2v', '/m/016tt2'): {'label': ['/award/award_nominee/award_nominations./award/award_nomination/award_nominee']}, ('/m/04gnbv1', '/m/0gvstc3'): {'label': ['/award/award_winner/awards_won./award/award_honor/ceremony']}, ('/m/082gq', '/m/026qnh6'): {'label': ['/film/film_genre/films_in_this_genre']}, ('/m/05k17c', '/m/02dqdp'): {'label': ['/organization/role/leaders./organization/leadership/organization']}, ('/m/04cj79', '/m/0fvf9q'): {'label': ['/film/film/executive_produced_by']}, ('/m/09tqxt', '/m/0gtsxr4'): {'label': ['/award/award_category/nominees./award/award_nomination/nominated_for']}, ('/m/025sc50', '/m/0277c3'): {'label': ['/music/genre/artists']}, ('/m/01pjr7', '/m/02hrh1q'): {'label': ['/people/person/profession']}, ('/m/0bw20', '/m/09vw2b7'): {'label': ['/film/film/other_crew./film/film_crew_gig/film_crew_role']}, ('/m/01j4ls', '/m/08mbj5d'): {'label': ['/common/topic/webpage./common/webpage/category']}, ('/m/0cmdwwg', '/m/06t2t'): {'label': ['/film/film/release_date_s./film/film_regional_release_date/film_release_region']}, ('/m/0gs6vr', '/m/0gj96ln'): {'label': ['/film/actor/film./film/performance/film']}, ('/m/02lp0w', '/m/015882'): {'label': ['/award/award_category/nominees./award/award_nomination/award_nominee']}, ('/m/034x61', '/m/029sk'): {'label': ['/medicine/notable_person_with_medical_condition/condition']}}

