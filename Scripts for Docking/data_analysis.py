import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the combined dataset
combined_df = pd.read_csv('~/Desktop/CtoAnalyze/all_combined_data.csv')

# Example 1: Correlation between binding energy and number of interactions
combined_df['Num_Interactions'] = combined_df.groupby('Name')['Interaction Type'].transform('count')
correlation = combined_df['Binding Energy (kcal/mol)'].corr(combined_df['Num_Interactions'])
print(f"Correlation between binding energy and number of interactions: {correlation}")

# Example 2: Group by interaction type and calculate mean binding energy
interaction_type_group = combined_df.groupby('Interaction Type')['Binding Energy (kcal/mol)'].mean()
print("Mean Binding Energy by Interaction Type:")
print(interaction_type_group)

# Example 3: Residue-specific analysis
residue_group = combined_df.groupby('PROT_residue')['Binding Energy (kcal/mol)'].mean().sort_values()
print("Mean Binding Energy by Residue:")
print(residue_group)

# Example 4: Visualization - Scatter plot of binding energy vs. number of interactions
plt.figure(figsize=(10, 6))
sns.scatterplot(data=combined_df, x='Num_Interactions', y='Binding Energy (kcal/mol)', hue='Interaction Type')
plt.title('Binding Energy vs. Number of Interactions')
plt.show()

# Example 5: Visualization - Box plot of binding energy by interaction type
plt.figure(figsize=(10, 6))
sns.boxplot(data=combined_df, x='Interaction Type', y='Binding Energy (kcal/mol)')
plt.title('Binding Energy Distribution by Interaction Type')
plt.show()
