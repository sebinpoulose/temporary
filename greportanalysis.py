import pandas as pd
data_frame = pd.read_csv("Testset.csv")
list_of_tests = data_frame['TestName'].unique()
print(list_of_tests)
data_frame = pd.read_csv("labresults.csv")
list_of_patient = data_frame['PatientID'].unique()
print(len(list_of_patient))
