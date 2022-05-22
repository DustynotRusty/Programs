import pandas as pd
#cities_url = "C:/Users/gteja/OneDrive\Desktop\cities.csv"
cities_info = pd.read_csv(r'C:\Users\gteja\OneDrive\Desktop\cities.csv')
print(cities_info)
print(cities_info.shape)
print(cities_info.head())
