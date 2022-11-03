from process_json import run_details_df
from process_json import part_info_df
import pandas as pd
import numpy as np

def filter(load_num = False, equipment = False, recipe = False, start = False, durationMin = False, durationMax = False, operator = False):
    
    filtered_df = run_details_df.copy().astype({'RunStart': 'datetime64[s]', 'RunDuration': 'float'})

    if load_num != False:
        filtered_df = filtered_df[filtered_df['LoadNumber'] == load_num]
    
    if equipment != False:
        filtered_df = filtered_df[filtered_df['Equipment'] == equipment]

    if recipe != False:
        filtered_df = filtered_df[filtered_df['RunRecipe'] == recipe]

    if start != False:
        filtered_df = filtered_df[filtered_df['RunStart'] >= start]

    if durationMin != False or durationMax != False:
        filtered_df = filtered_df[(filtered_df['RunDuration'] >= durationMin) & (filtered_df['RunDuration'] <= durationMax)]
        False

    if operator != False:
        filtered_df = filtered_df[filtered_df['OperatorName'] == operator]

    return filtered_df

