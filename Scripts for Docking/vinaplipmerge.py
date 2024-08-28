import pandas as pd

# Load the interaction data (includes specific bindings)
interaction_df = pd.read_csv('~/Desktop/CtoAnalyze/output_file.csv')
print(interaction_df.columns)

# Load the Vina data (includes binding energies)
vina_df = pd.read_csv('~/Desktop/CtoAnalyze/vina_results_summary.csv')
print(vina_df.columns)

interaction_df['Directory'] = interaction_df['Directory'].str.lower()
vina_df['Name'] = vina_df['Name'].str.lower()


# Merge the two DataFrames on the common column (e.g., 'directory')
combined_df = pd.merge(interaction_df, vina_df, left_on='Directory', right_on ='Name')


# Optionally, you can reorder the columns or drop any unnecessary columns
combined_df = combined_df[['Name', 'Binding Energy (kcal/mol)', 'RESNR', 'RESTYPE', 'RESCHAIN', 'LIG_atom', 'PROT_atom', 'PROT_residue', 'LIGCOO', 'PROTCOO', 'Interaction Type']]

combined_df = combined_df.sort_values(by='Binding Energy (kcal/mol)', ascending=True)
print(combined_df.head)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('~/Desktop/CtoAnalyze/all_combined_data.csv', index=False)

# Display the first few rows of the combined DataFrame
print(combined_df.head())
