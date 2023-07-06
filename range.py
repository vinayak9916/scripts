import pandas as pd
import requests
import json

df = pd.read_excel('alpha-range (1).xlsx')
list1 = []

url = "https://api.alpha.staging.livspace.com/livhome-backend/v1/design-attributes/{}"
headers = {
  'Authorization': 'Bearer devYkWGDwh0Opd1Q6zSpajm_xjebT9YUb6LdZJaz3TM.F6XKAAYu5K7kJPiAgooxYu4044VV-wV4mSr4dN3E2X8',
  'Content-Type': 'application/json'
}
failed_get_attr = []
failed_post_attr = []

print(f"Total_count= {len(df.index)}")
count = 1

for index, row in df.iterrows():
    design_id = row['design_id']
    if pd.isnull(design_id):
        continue
    if design_id == "#N/A":
        continue
    else:
        design_id = int(design_id)
        list1.append(design_id)
    is_aarambh = row['Aarambh'] == 'Yes'
    is_everyday = row['Everyday'] == 'Yes'
    is_recom = row['Recommended'] == 'Yes'
    is_infinity = row['Infinity'] == 'Yes'
    response = requests.get(url=url.format(design_id), headers=headers)
    #print(f"design_id = {design_id}, response_code = {response.status_code}")
    #print(response.json())
    payload = {"attributes": []}
    # "attributes": [
    #     {
    #         "attribute_id": 125,
    #         "attribute_value": "2BHK",
    #         "data_type": "LIST"
    #     },

    if response.status_code == 200:
        for i in response.json():
            attr_dict = {}
            if i['attribute_type'] == 'range':
                if 'attribute_value' not in i:
                        i['attribute_value'] = {}
                if is_aarambh or is_everyday:
                    i['attribute_value']['Aarambh'] = True
                    i['attribute_value']['Everyday'] = False
                if is_recom:
                    i['attribute_value']['Recommended By Livspace'] = True
                if is_infinity:
                    i['attribute_value']['Infinity'] = True
                    i['attribute_value']['Aarambh'] = False
                    i['attribute_value']['Everyday'] = False

            if 'attribute_value' not in i:
                continue
            attr_dict['attribute_id'] = i['id']
            attr_dict['attribute_value'] = i['attribute_value']
            attr_dict['data_type'] = i['data_type']
            payload['attributes'].append(attr_dict)
        print({design_id: payload})
        response2 = requests.post(url=url.format(design_id), headers=headers, data=json.dumps(payload))
        if response2.status_code!=200:
            failed_post_attr.append({design_id: response2.status_code})
    else:
        failed_get_attr.append({design_id: response.status_code})
    count = count + 1
    print(f"Total_count= {len(df.index)} || Current Count = {count}")
    

print(failed_get_attr)
print(len(failed_get_attr))
print(failed_post_attr)
print(len(failed_post_attr))

