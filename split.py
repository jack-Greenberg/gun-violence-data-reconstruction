import pandas as pd

df = pd.read_csv('clean.csv')

OG_LENGTH = 239677

print(239677)

df_training = df.tail( OG_LENGTH - 1000 )
df_test = df.head( 1000 )

known = ['n_killed', 'n_injured', 'Victim', 'state_Alabama', 'state_Alaska', 'state_Arizona', 'state_Arkansas', 'state_California', 'state_Colorado', 'state_Connecticut', 'state_Delaware', 'state_District of Columbia', 'state_Florida', 'state_Georgia', 'state_Hawaii', 'state_Idaho', 'state_Illinois', 'state_Indiana', 'state_Iowa', 'state_Kansas', 'state_Kentucky', 'state_Louisiana', 'state_Maine', 'state_Maryland', 'state_Massachusetts', 'state_Michigan', 'state_Minnesota', 'state_Mississippi', 'state_Missouri', 'state_Montana', 'state_Nebraska', 'state_Nevada', 'state_New Hampshire', 'state_New Jersey', 'state_New Mexico', 'state_New York', 'state_North Carolina', 'state_North Dakota', 'state_Ohio', 'state_Oklahoma', 'state_Oregon', 'state_Pennsylvania', 'state_Rhode Island', 'state_South Carolina', 'state_South Dakota', 'state_Tennessee', 'state_Texas', 'state_Utah', 'state_Vermont', 'state_Virginia', 'state_Washington', 'state_West Virginia', 'state_Wisconsin', 'state_Wyoming', 'month_1', 'month_2', 'month_3', 'month_4', 'month_5', 'month_6', 'month_7', 'month_8', 'month_9', 'month_10', 'month_11', 'month_12', 'weekday_0', 'weekday_1', 'weekday_2', 'weekday_3', 'weekday_4', 'weekday_5', 'weekday_6']

unknown = ['n_guns_involved', 'Adult 18+', 'Teen 12-17', 'Child 0-11', 'Male', 'Female', 'Subject-Suspect']

training_known = df_training[known]
training_unknown = df_training[unknown]

test_known = df_test[known]
test_unknown = df_test[unknown]

training_known.to_csv('training_known.csv')
training_unknown.to_csv('training_unknown.csv')
test_known.to_csv('test_known.csv')
test_unknown.to_csv('test_unknown.csv')
