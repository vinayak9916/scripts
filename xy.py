list1 = [
{"id":1,"attribute_type":"apartment_type","data_type":"LIST"},
{"id":2,"attribute_type":"kitchen_shape","data_type":"LIST"},
{"id":3,"attribute_type":"style","data_type":"LIST"},
{"id":4,"attribute_type":"size","data_type":"LIST"},
{"id":5,"attribute_type":"accessories_scope","data_type":"LIST"},
{"id":6,"attribute_type":"color","data_type":"LIST"},
{"id":7,"attribute_type":"shutter_finish","data_type":"LIST"},
{"id":8,"attribute_type":"carcass_material","data_type":"LIST"},
{"id":9,"attribute_type":"carcass_color","data_type":"STRING"},
{"id":10,"attribute_type":"shutter_color","data_type":"STRING"},
{"id":11,"attribute_type":"granite_length","data_type":"FLOAT"},
{"id":12,"attribute_type":"granite_width","data_type":"FLOAT"},
{"id":13,"attribute_type":"granite_area","data_type":"FLOAT"},
{"id":14,"attribute_type":"hob_size","data_type":"FLOAT"},
{"id":15,"attribute_type":"chimney_size","data_type":"FLOAT"},
{"id":16,"attribute_type":"microwave_size","data_type":"FLOAT"},
{"id":17,"attribute_type":"sink_size","data_type":"FLOAT"},
{"id":18,"attribute_type":"length","data_type":"FLOAT"},
{"id":19,"attribute_type":"width","data_type":"FLOAT"},
{"id":20,"attribute_type":"height","data_type":"FLOAT"},
{"id":21,"attribute_type":"area","data_type":"FLOAT"},
{"id":22,"attribute_type":"property","data_type":"AUTOSUGGEST"},
{"id":23,"attribute_type":"wardrobe_type","data_type":"MULTILIST"},
{"id":24,"attribute_type":"product_type","data_type":"MULTILIST"},
{"id":25,"attribute_type":"storage_unit_type","data_type":"LIST"},
{"id":26,"attribute_type":"color","data_type":"LIST"},
{"id":27,"attribute_type":"shutter_finish","data_type":"LIST"},
{"id":28,"attribute_type":"carcass_material","data_type":"LIST"},
{"id":29,"attribute_type":"carcass_color","data_type":"STRING"},
{"id":30,"attribute_type":"shutter_color","data_type":"STRING"},
{"id":31,"attribute_type":"length","data_type":"FLOAT"},
{"id":32,"attribute_type":"width","data_type":"FLOAT"},
{"id":33,"attribute_type":"height","data_type":"FLOAT"},
{"id":34,"attribute_type":"area","data_type":"FLOAT"},
{"id":35,"attribute_type":"property","data_type":"AUTOSUGGEST"},
{"id":36,"attribute_type":"style","data_type":"LIST"},
{"id":37,"attribute_type":"ws_type","data_type":"LIST"},
{"id":38,"attribute_type":"range","data_type":"MULTILIST"},
{"id":39,"attribute_type":"range","data_type":"MULTILIST"},
{"id":40,"attribute_type":"apartment_type","data_type":"LIST"},
{"id":41,"attribute_type":"property","data_type":"AUTOSUGGEST"},
{"id":42,"attribute_type":"style","data_type":"LIST"},
{"id":43,"attribute_type":"color","data_type":"LIST"},
{"id":44,"attribute_type":"budget","data_type":"FLOAT"},
{"id":45,"attribute_type":"room_size","data_type":"FLOAT"},
{"id":46,"attribute_type":"budget","data_type":"FLOAT"},
{"id":47,"attribute_type":"room_size","data_type":"FLOAT"},
{"id":48,"attribute_type":"feature_type","data_type":"MULTILIST"},
{"id":49,"attribute_type":"handle","data_type":"MULTILIST"},
{"id":50,"attribute_type":"handle","data_type":"MULTILIST"},
{"id":51,"attribute_type":"apartment_type","data_type":"LIST"},
{"id":52,"attribute_type":"shutter_type","data_type":"MULTILIST"}
]


attribute_data_type_mapping = {}
{"apartment_type": {}}

for i in list1:
    attribute_type = i["attribute_type"]
    if attribute_type not in attribute_data_type_mapping:
        attribute_data_type_mapping[i["attribute_type"]] = {}
        attribute_data_type_mapping[i["attribute_type"]]["id"] = i["id"]
        attribute_data_type_mapping[i["attribute_type"]]["data_type"] = i["data_type"]

print(attribute_data_type_mapping)