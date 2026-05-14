import pandas as pd

df = pd.read_csv('wild_boars.csv')

male_std = df.groupby('gender')['tusk_length_cm'].std()['Male']
male_mean = df.groupby('gender')['tusk_length_cm'].mean()['Male']
male_cv = male_std / male_mean * 100

female_std = df.groupby('gender')['tusk_length_cm'].std()['Female']
female_mean = df.groupby('gender')['tusk_length_cm'].mean()['Female']
female_cv = female_std / female_mean * 100

file = open('tusk_cv_by_gender.txt', 'w')

file.write(f"Male: {male_cv:.2f}%\n")
file.write(f"Female: {female_cv:.2f}%\n")

file.close()

print("Файл создан")
