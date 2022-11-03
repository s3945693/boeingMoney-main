import json
import pandas as pd

file = "C:/Users/frede/OneDrive/Desktop/University/Hackathon/boeingMoney-main/json/AC2-07337-anon.json"

f = open(file)
data = json.loads(f.read())
part_info_df_temp = pd.json_normalize(data['RunDetails'])
part_info_df_temp.to_html(r'templates\display_json_details.html')