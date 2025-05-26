import pandas as pd
import requests
from datawrapper import Datawrapper
from bs4 import BeautifulSoup

dw = Datawrapper(access_token = "") #todo: add your own datawrapper API token

json_land_sea = "https://data.unhcr.org/population/get/timeseries?widget_id=588956&sv_id=100&population_group=4797,4798,5634&frequency=month&fromDate=2016-01-01"
json_sea = "https://data.unhcr.org/population/get/timeseries?widget_id=588957&sv_id=100&population_group=4797,5634&frequency=month&fromDate=2016-01-01"
json_land = "https://data.unhcr.org/population/get/timeseries?widget_id=588958&sv_id=100&population_group=4798&frequency=month&fromDate=2016-01-01"

#function to read json data into a dataframe
def json_to_dataframe(s_url):
    
    # request data from url
    response = requests.get(s_url)
    
    #retrieve json
    json_data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(json_data['data']['timeseries'])

    return df

#naming individual dataframes
df_land_sea = json_to_dataframe(json_land_sea)
df_sea = json_to_dataframe(json_sea)
df_land = json_to_dataframe(json_land)

#renaming columns to prepare merge
df_land_sea.columns=(['month','year','unix_timestamp','individuals_land+sea'])
df_sea.columns=(['month','year','unix_timestamp','individuals_sea'])
df_land.columns=(['month','year','unix_timestamp','individuals_land'])

#merge all three dataframes togetehr
df_merged = df_land_sea.merge(df_sea, on=['month','year','unix_timestamp'])
df_merged = df_merged.merge(df_land, on=['month','year','unix_timestamp'])

# create a timestamp column to be used in chart
df_merged['timestamp']=df_merged['year'].astype(str)+'-'+df_merged['month'].astype(str)

# keeping only needed columns
df_merged_selected = df_merged[['timestamp','individuals_sea','individuals_land']]

# ## Run for every update

chart_id='' #todo: add your own chart ID here

latest_data_from_month = df_merged_selected.timestamp.max()

PAGE_URL='https://data.unhcr.org/en/situations/europe-sea-arrivals'
response = requests.get(PAGE_URL) # get the date from the page
pagehtml = BeautifulSoup(response.text, "html.parser") # parse the html

date_str = pagehtml.find_all('div', {'class':'popTotalDate'}) # find all divs with this class (inspect page via console)
date_str_tidy = date_str[0].text.strip().replace('Last updated ', '') #pick the first element, tidy it up a bit

latest_year = df_merged.year.max()

total_arrivals_latest_year = df_merged[df_merged['year']==latest_year]['individuals_land+sea'].sum()
total_arrivals_latest_year_formatted = f"{total_arrivals_latest_year:,}"

dw.update_description(
 chart_id,
 intro=f'Total arrivals of individuals since the beginning of this year so far: {total_arrivals_latest_year_formatted}',
 source_name = f'UNHCR, latest data from: {date_str_tidy}',
 source_url = 'https://data.unhcr.org/en/situations/europe-sea-arrivals',
)

dw.add_data(chart_id, df_merged_selected)

dw.publish_chart(chart_id)
