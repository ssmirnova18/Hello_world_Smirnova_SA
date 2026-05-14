import pandas as pd

df = pd.read_csv('wild_boars.csv')

file = open('average_values.txt', 'w')

file.write(f"age_years: {df['age_years'].mean():.2f}\n")
file.write(f"weight_kg: {df['weight_kg'].mean():.2f}\n")
file.write(f"length_cm: {df['length_cm'].mean():.2f}\n")
file.write(f"shoulder_height_cm: {df['shoulder_height_cm'].mean():.2f}\n")
file.write(f"tusk_length_cm: {df['tusk_length_cm'].mean():.2f}\n")
file.write(f"litter_size: {df['litter_size'].mean():.2f}\n")
file.write(f"health_score: {df['health_score'].mean():.2f}\n")
file.write(f"territory_ha: {df['territory_ha'].mean():.2f}\n")

file.close()

print("Файл создан")
