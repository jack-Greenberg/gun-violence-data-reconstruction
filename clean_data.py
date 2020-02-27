import pandas as pd
import os
from datetime import datetime
import math


df = pd.read_csv('./duplicate.csv')
df['month'] = 0
df['weekday'] = 0
df['Adult 18+'] = 0
df['Teen 12-17'] = 0
df['Child 0-11'] = 0
df['Male'] = 0
df['Female'] = 0
df['Subject-Suspect'] = 0
df['Victim'] = 0
for i in range(len(df['date'])):
    # Parse date
    date = datetime.strptime(df['date'][i], "%Y-%m-%d")
    df.loc[df.index == i, 'month'] = date.month
    df.loc[df.index == i, 'weekday'] = int(datetime.strftime(date, "%w"))

    # Parse age group
    # if not math.isnan(df['participant_age_group'][i]):
    try:
        age_group_list = df['participant_age_group'][i].split('||')

        for j in range(len(age_group_list)):
            try:
                group = age_group_list[j].split("::")[1]
                df.loc[df.index == i, group] += 1
            except IndexError:
                pass
    except AttributeError:
        pass

    # Parse gender
    try:
        gender_list = df['participant_gender'][i].split('||')

        for j in range(len(gender_list)):
            try:
                gender = gender_list[j].split("::")[1]
                df.loc[df.index == i, gender] += 1
            except IndexError:
                pass
    except AttributeError:
        pass


    # Parse participant type
    try:
        participant_list = df['participant_type'][i].split('||')

        for j in range(len(participant_list)):
            try:
                participant_type = participant_list[j].split('::')[1]
                df.loc[df.index == i, participant_type] += 1
            except IndexError:
                pass
    except AttributeError:
        pass

# Drop columns
df.drop(columns=['incident_id','state_senate_district', 'city_or_county', 'address', 'incident_url','source_url','incident_url_fields_missing', 'location_description', 'latitude', 'longitude', 'notes', 'sources', 'incident_characteristics', 'participant_name', 'participant_age', 'participant_relationship', 'gun_stolen', 'gun_type', 'date', 'participant_gender', 'participant_age_group', 'congressional_district', 'state_house_district', 'participant_status', 'participant_type'], inplace=True)

# One hot
df = pd.get_dummies(df, columns=['state', 'month', 'weekday'])

df.to_csv('clean.csv', index=False)
