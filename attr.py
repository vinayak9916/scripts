import pandas as pd

df = pd.read_excel('abc.xlsx')

design_dict = {}
list1 = []

for index, row in df.iterrows():
    if 'Design ID' not in df.columns:
        continue
    design_id = row['Design ID']

    # Skip rows where Design ID is NaN
    if pd.isnull(design_id):
        continue

    design_id = int(design_id)
    ##list1.append(design_dict)
    attribute_type = row['attribute_type']
    attribute_value = row['attribute_values']

    # Skip rows where attribute_type has no attribute_value
    if pd.isnull(attribute_value):
        continue

    if design_id not in design_dict:
        design_dict[design_id] = []
    design_dict[design_id].append({attribute_type: attribute_value})
        
list1 = []
for key, value in design_dict.items():
    list1.append(key)
print(list1)


#print(design_dict)
# print(len(design_dict))

# attribute_mapping = {
#     'apartment_type': {'id': 1, 'data_type': 'LIST'},
#     'kitchen_shape': {'id': 2, 'data_type': 'LIST'},
#     'style': {'id': 3, 'data_type': 'LIST'},
#     'size': {'id': 4, 'data_type': 'LIST'},
#     'accessories_scope': {'id': 5, 'data_type': 'LIST'},
#     'color': {'id': 6, 'data_type': 'LIST'},
#     'shutter_finish': {'id': 7, 'data_type': 'LIST'},
#     'carcass_material': {'id': 8, 'data_type': 'LIST'},
#     'carcass_color': {'id': 9, 'data_type': 'STRING'},
#     'shutter_color': {'id': 10, 'data_type': 'STRING'},
#     'granite_length': {'id': 11, 'data_type': 'FLOAT'},
#     'granite_width': {'id': 12, 'data_type': 'FLOAT'},
#     'granite_area': {'id': 13, 'data_type': 'FLOAT'},
#     'hob_size': {'id': 14, 'data_type': 'FLOAT'},
#     'chimney_size': {'id': 15, 'data_type': 'FLOAT'},
#     'microwave_size': {'id': 16, 'data_type': 'FLOAT'},
#     'sink_size': {'id': 17, 'data_type': 'FLOAT'},
#     'length': {'id': 18, 'data_type': 'FLOAT'},
#     'width': {'id': 19, 'data_type': 'FLOAT'},
#     'height': {'id': 20, 'data_type': 'FLOAT'},
#     'area': {'id': 21, 'data_type': 'FLOAT'},
#     'property': {'id': 22, 'data_type': 'AUTOSUGGEST'},
#     'wardrobe_type': {'id': 23, 'data_type': 'MULTILIST'},
#     'product_type': {'id': 24, 'data_type': 'MULTILIST'},
#     'storage_unit_type': {'id': 25, 'data_type': 'LIST'},
#     'ws_type': {'id': 37, 'data_type': 'LIST'},
#     'range': {'id': 38, 'data_type': 'MULTILIST'},
#     'budget': {'id': 44, 'data_type': 'FLOAT'},
#     'room_size': {'id': 45, 'data_type': 'FLOAT'},
#     'feature_type': {'id': 48, 'data_type': 'MULTILIST'},
#     'handle': {'id': 49, 'data_type': 'MULTILIST'},
#     'shutter_type': {'id': 52, 'data_type': 'MULTILIST'},
#     }

# print(type(attribute_mapping))

# import requests
# import json
# failed_designs = []

# url = "https://api.livspace.com/livhome-backend/v1/design-attributes/{}"
# headers = {
#   'Authorization': 'Bearer 7VXhh9X3arDn-4WXGLMYX7DcGUK0nidO5iyfKgUDk3A.rDWNimDK5QM5J1G_LkmzBeZPyeiIUrQ0hGs3eVRt9HE',
#   'Content-Type': 'application/json'
# }

# for key, value in design_dict.items():
#     payload_dict = {"attributes": []}
#     print(key)
#     url2 = url.format(key)
#     for dic in value:
#         for key2 in dic:
#             data_type = attribute_mapping[key2]['data_type']
#             print(data_type)
#             attribute_value = ""
#             if data_type == 'LIST':
#                 attribute_value = dic[key2]
#             else:
#                 attribute_value = {dic[key2]:True}

#             payload_dict['attributes'].append({"attribute_id": attribute_mapping[key2]["id"], "data_type":data_type, "attribute_value":attribute_value})
#     payload = json.dumps(payload_dict)
#     print(url2)
#     print(payload)
#     response = requests.request("POST", url2, headers=headers, data=payload)
#     if response.status_code!=200:
#         failed_designs.append(key)

# print(failed_designs)

 


    

# ##print(response.text)

