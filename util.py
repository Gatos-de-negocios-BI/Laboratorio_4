import numpy as np
import pandas as pd

file = 'assets/university_admission_train.csv'

df = pd.read_csv(file)
df.dropna(subset=['Admission Points'], inplace=True)
df.to_csv('assets/university_admission_train.csv', index=False)
