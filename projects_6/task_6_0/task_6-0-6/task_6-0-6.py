import pandas as pd

df = pd.read_csv('wild_boars.csv')

male_q1 = df.groupby('gender')['length_cm'].quantile(0.25)['Male']
male_q3 = df.groupby('gender')['length_cm'].quantile(0.75)['Male']

female_q1 = df.groupby('gender')['length_cm'].quantile(0.25)['Female']
female_q3 = df.groupby('gender')['length_cm'].quantile(0.75)['Female']

male_iqr = male_q3 - male_q1
female_iqr = female_q3 - female_q1

file = open('iqr_length_by_gender.txt', 'w')

file.write(f"Male: {male_iqr:.1f}\n")
file.write(f"Female: {female_iqr:.1f}\n")

file.close()

print("Файл создан")
