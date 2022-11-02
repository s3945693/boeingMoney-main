import pandas as pd
import numpy as np
import json


f = open("C:/Users/frede/Downloads/AutoClave5 JSON Files/AC2-07337-anon.json")
data = json.loads(f.read())
part_info_df = pd.json_normalize(data['PartInformation'], meta=data['RunDetails'])
part_info_df['load_no'] = data['PartInformation']
print(part_info_df)

#test = pd.json_normalize("C:/Users/frede/Downloads/AutoClave5 JSON Files/AC2-07337-anon.json")
#test.head(10)
#print('what')