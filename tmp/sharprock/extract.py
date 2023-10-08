import json
import re
from collections import OrderedDict
def extract_ids_from_json_file(filename):
    # Load the JSON file
    with open(filename, 'r') as f:
        data = json.load(f)

    # Extract all the ids into a set
    ids = set()
    for zone in data['zones']:
        for question in zone['questions']:

            if 'alternatives' in question:
                for alternative in question['alternatives']:
                    ids.add(alternative['id'])
            else:
                ids.add(question['id'])

    # Return the set of ids
    return ids
def trim(s):
    start = s.find('(')
    end = s.find(')')
    
    # If both '(' and ')' are found
    if start != -1 and end != -1:
        # Extract the number in between and remove it from the original string
        points = s[start+1:end]
        s = s[:start] + s[end+1:]
        # Check if the number is a valid integer
        # try:
        #     int(points)
        # except ValueError:
        #     # If not, return the original string
        #     return s
    return s
def get_prefix(string):
    last_slash_index = string.rfind('/')
    return string[:last_slash_index]

def get_title(qid):

    if qid.startswith("DynamicSemantics-HoareLogic_inferenceRules-multipleTF"):
        return "13. Hoare Logic, Multiple T/F (Change all the whiles, and add some others)"
    elif qid.startswith("OCaml/lexing/regex_rrg"):
        return "8. Regular expressions and right regular grammars"
    elif qid.startswith("Functional_Programming-basicEnvironments-multipleTF"):
        return "2. Basic Environment Calculation (T/F)"
    elif qid.startswith("OCaml/unification/unification_computation"):
        return "7. Unification algorithm (Computation)"
    elif qid.startswith("OCaml/polymorphic_type_derivations"):
        return "6. Type Derivation Code"    
    else:
        return None

def get_id_prefix_title_maps(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    id_prefix_map = OrderedDict()
    prefix_title_map = OrderedDict()

    for zone in data['zones']:
        for question in zone['questions']:
            qid = question['id']
            prefix = get_prefix(qid)
            title = zone['title']
            id_prefix_map[qid] = prefix
            prefix_title_map[prefix] = trim(title)

    return id_prefix_map, prefix_title_map

def check_ids_in_json(id_set, json_file):
    append_result = OrderedDict()

    id_prefix_map, prefix_title_map = get_id_prefix_title_maps(json_file)
    # print(id_prefix_map['OCaml/cps/cps_transform_to_ocaml/all_positive'])
    # print(prefix_title_map)
    # print('OCaml/dynamic_semantics/natural_semantics/' in prefix_title_map)
    cnt = 0
    for qid in id_set:
        if qid in id_prefix_map:
            append_result[qid] = prefix_title_map[id_prefix_map[qid]]
        else:
            if get_prefix(qid) in prefix_title_map:
                append_result[qid] = prefix_title_map[get_prefix(qid)]
            elif get_title(qid) is not None:
                append_result[qid] = get_title(qid)

            else:
                if cnt < 3:
                    print(f"{qid} is not present in {json_file}")
                cnt+= 1
                pass

    print(cnt)
    return append_result
    # print(prefix_title_map['OCaml/lexing/regex_rrg/'])
# Call the function with the filename as input
final_ids_set = extract_ids_from_json_file('Final.json')
practice_ids_set = extract_ids_from_json_file('Practice.json')

final_map = check_ids_in_json(final_ids_set, 'infoAssessment.json')
practice_map = check_ids_in_json(practice_ids_set, 'infoAssessment.json')

for key in final_map.keys():
    final_map[key] = "|Final|" + final_map[key]
for key in practice_map.keys():
    practice_map[key] = "|Practice|" + practice_map[key]
print(f'{len(final_ids_set)}=={len(final_map)}')
print(f'{len(practice_ids_set)}=={len(practice_map)}')

id_prefix_map, prefix_title_map = get_id_prefix_title_maps('infoAssessment.json')
sr_map = OrderedDict()
for qid in id_prefix_map:
    if qid in final_ids_set or practice_ids_set:
        pass
    sr_map[qid] = prefix_title_map[get_prefix(qid)]

all_map = OrderedDict()

all_map.update(sr_map)
all_map.update(final_map)
all_map.update(practice_map)

def generate_homework_json(ids):
    # Group ids by title
    titles = {}
    for id, title in ids.items():
        if title not in titles:
            titles[title] = []
        titles[title].append(id)
    
    # Create the JSON object
    homework = {
        "uuid": "57be0aa4-ddc3-11ed-b5ea-0242ac120002",
        "type": "Homework",
        "title": "Final Exam",
        "set": "Sharp Rocks",
        "number": "11",
        "zones": []
    }
    
    # Add a zone for each title
    for title, ids in titles.items():
        zone = {
            "title": title,
            "questions": []
        }
        # Add each id to the zone's questions
        for id in ids:
            question = {
                "id": id,
                "points": 10
            }
            zone["questions"].append(question)
        
        homework["zones"].append(zone)
    return homework
    # Write the JSON object to a file


print('OCaml/basic_environment_calculations/VSCodeQuestions/basicEnv0' in all_map)
ans = generate_homework_json(all_map)

def extract_numeric_prefix(strings):
    numeric_prefixes = []
    for string in strings:
        if "|Final|" in string or "|Practice|" in string:
            string = string.split("|")[-1]
        numeric_prefix = int(string.split(".")[0])
        numeric_prefixes.append(numeric_prefix)
    return numeric_prefixes

def extract_zone_titles(json_obj):
    titles = []
    zones = json_obj.get("zones", [])  # get zones list if exists, or empty list if not
    for zone in zones:
        title = zone.get("title")
        if title is not None:
            titles.append(title)
    return titles


def sort_zones(json_data, zone_order):
    zones = json_data['zones']
    zipped = list(zip(zones, zone_order))
    sorted_zones = [x[0] for x in sorted(zipped, key=lambda x: x[1])]
    json_data['zones'] = sorted_zones
    return json.dumps(json_data, indent=4)


zone_list = extract_numeric_prefix(extract_zone_titles(ans))
pr_list = []
for t in extract_zone_titles(ans):
    if t.startswith('|Final|'):
        pr_list.append(0)
    elif t.startswith('|Practice|'):
        pr_list.append(1)
    else:
        pr_list.append(2)
zone_list = [pr_list[i] + zone_list[i]*100 for i in range(len(zone_list))]
sort_zones(ans, zone_list)
# print(zone_list)
with open("result.json", "w") as f:
    json.dump(ans, f, indent=4)
