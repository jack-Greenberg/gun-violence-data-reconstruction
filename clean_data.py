import pandas as pd
import os

df = pd.read_csv('./duplicate.csv')
df.drop(columns=['incident_id','state_house_district','state_senate_district', 'city_or_county', 'address', 'incident_url','source_url','incident_url_fields_missing', 'location_description', 'latitude', 'longitude', 'notes', 'sources', 'incident_characteristics', 'participant_name'], inplace=True)
# df = pd.get_dummies(df, columns=['state', 'congressional_district'])
df.to_csv('clean.csv', index=False)

#incident_id,date,state,city_or_county,address,n_killed,n_injured,incident_url,source_url,incident_url_fields_missing,congressional_district,gun_stolen,gun_type,incident_characteristics,latitude,location_description,longitude,n_guns_involved,notes,participant_age,participant_age_group,participant_gender,participant_name,participant_relationship,participant_status,participant_type,sources,state_house_district,state_senate_district
