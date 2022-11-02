import pandas as pd
import numpy as np
import json


f = open("AutoClave/AC2-07337-anon.json")
data = json.loads(f.read())
part_info_df = pd.json_normalize(data['PartInformation'])
part_info_df['LoadNumber'] = data['RunDetails']['LoadNumber']

run_details_df = pd.json_normalize(data['RunDetails'])

print(part_info_df.head())
print(run_details_df.head())


#test = pd.json_normalize("C:/Users/frede/Downloads/AutoClave5 JSON Files/AC2-07337-anon.json")
#test.head(10)
#print('what')