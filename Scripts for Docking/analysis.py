import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('~/Desktop/CtoAnalyze/interaction_analysis_summary.csv')

print(df.describe())
print(df['Interaction Type'].value_counts())  # Count occurrences of each interaction type

sns.countplot(x='Interaction Type', data=df)
plt.xticks(rotation=45)
plt.title('Frequency of Interaction Types')
plt.show()

df['Interaction Type'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Proportion of Interaction Types')
plt.ylabel('')
plt.show()

df['Residue'] = df['Data'].apply(lambda x: x.split('|')[1].strip() if len(x.split('|')) > 1 else 'Unknown')
print(df['Residue'].value_counts().head(10))  # Top 10 interacting residues

residue_interaction_matrix = pd.crosstab(df['Residue'], df['Interaction Type'])
sns.heatmap(residue_interaction_matrix, cmap='coolwarm', annot=True, fmt='d')
plt.title('Residue vs Interaction Type')
plt.show()

