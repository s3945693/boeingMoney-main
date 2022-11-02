import pandas as pd
import numpy as np
import json
import os
import glob
#https://stackoverflow.com/questions/57067551/how-to-read-multiple-json-files-into-pandas-dataframe

trial = 'json/*'


fileList = glob.glob(trial)
print('This was fileList:',fileList)
df = []

for file in fileList:
    f = open(file)
    data = json.loads(f.read())

    part_info_df = pd.json_normalize(data['PartInformation'], meta=data['RunDetails'])
    part_info_df['load_no'] = data['PartInformation']

    df.append(part_info_df)


temp = pd.concat(df, ignore_index=True)
print(temp)

