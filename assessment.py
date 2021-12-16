import pandas as pd

file = pd.read_csv('resultfile.csv')

df = pd.DataFrame(file)
df = df.iloc[: , :-1]
df.dropna(inplace=True)

df['L3.1 (CR)'] = df['L3.1 (CR)'].replace(['P'], 0)
df['L3.1 (CR)'] = df['L3.1 (CR)'].astype('int')

df['L3.2 (AAA))'] = df['L3.2 (AAA))'].replace(['P'], 0)
df['L3.2 (AAA))'] = df['L3.2 (AAA))'].astype('int')

df['L3.3 (AT)'] = df['L3.3 (AT)'].replace(['P'], 0)
df['L3.3 (AT)'] = df['L3.3 (AT)'].astype('int')

df['L3.4 (SCS)'] = df['L3.4 (SCS)'].replace(['P'], 0)
df['L3.4 (SCS)'] = df['L3.4 (SCS)'].astype('int')

df['Total'] = df['L3.1 (CR)']+df['L3.2 (AAA))']+df['L3.3 (AT)']+df['L3.4 (SCS)']

print(df.loc[df['Total'].idxmax()])
print(df.loc[df['L3.1 (CR)'].idxmax()])
print(df.loc[df['L3.2 (AAA))'].idxmax()])
print(df.loc[df['L3.3 (AT)'].idxmax()])
print(df.loc[df['L3.4 (SCS)'].idxmax()])