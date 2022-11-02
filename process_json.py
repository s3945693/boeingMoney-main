import pandas as pd
import numpy as np
import json
import os
import glob
#https://stackoverflow.com/questions/57067551/how-to-read-multiple-json-files-into-pandas-dataframe

trial = 'AutoClave/*'
fileList = glob.glob(trial)
print('This was fileList:', fileList)
part_info_df = pd.DataFrame()
run_details_df = pd.DataFrame()
first_run = True


for file in fileList:
    f = open(file)
    data = json.loads(f.read())

    part_info_df_temp = pd.json_normalize(data['PartInformation'])
    #should do data[PartInformation][PartNumber]
    part_info_df_temp['LoadNumber'] = data['RunDetails']['LoadNumber']

    run_details_df_temp = data['RunDetails']



    if first_run == True:
        part_info_df = part_info_df_temp.copy()
        run_details_df = run_details_df_temp.copy()
        first_run == False
    else:
        part_info_df.append(part_info_df_temp, ignore_index=True)
        run_details_df.append(run_details_df_temp, ignore_index=True)


#temp = pd.concat(df, ignore_index=True)
print(run_details_df)

