import pandas as pd

# Load the interaction dataset
interactions_df = pd.read_csv('~/Desktop/ABDocking2/interaction_analysis_summary.csv')

# Assuming interactions_df has a column 'Interaction Type'
interaction_types = interactions_df['Interaction Type'].unique()

# Create a dictionary to hold DataFrames for each interaction type
interaction_dfs = {itype: interactions_df[interactions_df['Interaction Type'] == itype] for itype in interaction_types}

def extract_hydrophobic_interaction_data(row):
    parts = row.split('|')
    if len(parts) > 10 and parts[7].strip().replace('.', '', 1).isdigit():  # Ensure the DIST part is numeric
        return pd.Series({
            'RESNR': parts[1].strip(),
            'RESTYPE': parts[2].strip(),
            'RESCHAIN': parts[3].strip(),
            'RESNR_LIG': parts[4].strip(),
            'RESTYPE_LIG': parts[5].strip(),
            'RESCHAIN_LIG': parts[6].strip(),
            'DIST': float(parts[7].strip()),
            'LIGCARBONIDX': parts[8].strip(),
            'PROTCARBONIDX': parts[9].strip(),
            'LIGCOO': parts[10].strip(),
            'PROTCOO': parts[11].strip() if len(parts) > 11 else ''
        })
    else:
        return pd.Series()

# Apply this function to the DataFrame
hydrophobic_df = interaction_dfs['Hydrophobic Interaction']
hydrophobic_details = hydrophobic_df['Data'].apply(extract_hydrophobic_interaction_data)
hydrophobic_df = pd.concat([hydrophobic_df, hydrophobic_details], axis=1)
hydrophobic_df = hydrophobic_df.drop(columns=['Data', 'File'])

print(hydrophobic_df.head())

def extract_pi_stacking_data(row):
    parts = row.split('|')
    if len(parts) > 13 and parts[8].strip().replace('.', '', 1).isdigit():  # Ensure CENTDIST is numeric
        return pd.Series({
            'RESNR': parts[1].strip(),
            'RESTYPE': parts[2].strip(),
            'RESCHAIN': parts[3].strip(),
            'RESNR_LIG': parts[4].strip(),
            'RESTYPE_LIG': parts[5].strip(),
            'RESCHAIN_LIG': parts[6].strip(),
            'PROT_IDX_LIST': parts[7].strip(),  # List of protein atom indices
            'CENTDIST': float(parts[8].strip()),  # Central distance
            'ANGLE': float(parts[9].strip()),     # Angle between the ring planes
            'OFFSET': float(parts[10].strip()),   # Offset between the interacting groups
            'TYPE': parts[11].strip(),            # Stacking type (e.g., Perpendicular or T-Shaped)
            'LIG_IDX_LIST': parts[12].strip(),    # List of ligand atom indices
            'LIGCOO': parts[13].strip(),
            'PROTCOO': parts[14].strip() if len(parts) > 14 else ''
        })
    else:
        return pd.Series()

# Apply the function to the pi-stacking interaction DataFrame
pi_stacking_df = interaction_dfs['pi-Stacking']
pi_stacking_details = pi_stacking_df['Data'].apply(extract_pi_stacking_data)
pi_stacking_df = pd.concat([pi_stacking_df, pi_stacking_details], axis=1)
pi_stacking_df = pi_stacking_df.drop(columns=['Data', 'File'])

print(pi_stacking_df.head())


# Apply the function to the pi-stacking interaction DataFrame
pi_stacking_df = interaction_dfs['pi-Stacking']
pi_stacking_details = pi_stacking_df['Data'].apply(extract_pi_stacking_data)
pi_stacking_df = pd.concat([pi_stacking_df, pi_stacking_details], axis=1)
pi_stacking_df= pi_stacking_df.drop(columns=['Data', 'File'])

print(pi_stacking_df.head())

def extract_hydrogen_bond_data(row):
    parts = row.split('|')
    if len(parts) > 15 and parts[8].strip().replace('.', '', 1).isdigit():  # Ensure DIST_H-A is numeric
        return pd.Series({
            'RESNR': parts[1].strip(),
            'RESTYPE': parts[2].strip(),
            'RESCHAIN': parts[3].strip(),
            'RESNR_LIG': parts[4].strip(),
            'RESTYPE_LIG': parts[5].strip(),
            'RESCHAIN_LIG': parts[6].strip(),
            'SIDECHAIN': parts[7].strip(),
            'DIST_H-A': float(parts[8].strip()),  # Distance between H-Bond hydrogen and acceptor atom
            'DIST_D-A': float(parts[9].strip()),  # Distance between H-Bond donor and acceptor atoms
            'DON_ANGLE': float(parts[10].strip()),  # Angle at the donor
            'PROTISDON': parts[11].strip(),
            'DONORIDX': parts[12].strip(),
            'DONORTYPE': parts[13].strip(),
            'ACCEPTORIDX': parts[14].strip(),
            'ACCEPTORTYPE': parts[15].strip(),
            'LIGCOO': parts[16].strip(),
            'PROTCOO': parts[17].strip() if len(parts) > 17 else ''
        })
    else:
        return pd.Series()

# Apply the function to the hydrogen bond interaction DataFrame
hydrogen_bond_df = interaction_dfs['Hydrogen Bond']
hydrogen_bond_details = hydrogen_bond_df['Data'].apply(extract_hydrogen_bond_data)
hydrogen_bond_df = pd.concat([hydrogen_bond_df, hydrogen_bond_details], axis=1)
hydrogen_bond_df = hydrogen_bond_df.drop(columns=['Data', 'File'])

def extract_halogen_bond_data(row):
    parts = row.split('|')
    if len(parts) > 16:  # Ensure enough parts exist
        try:
            return pd.Series({
                'RESNR': parts[1].strip(),
                'RESTYPE': parts[2].strip(),
                'RESCHAIN': parts[3].strip(),
                'RESNR_LIG': parts[4].strip(),
                'RESTYPE_LIG': parts[5].strip(),
                'RESCHAIN_LIG': parts[6].strip(),
                'SIDECHAIN': parts[7].strip(),
                'DIST': float(parts[8].strip()),  # Distance
                'DON_ANGLE': float(parts[9].strip()),  # Donor angle
                'ACC_ANGLE': float(parts[10].strip()),  # Acceptor angle
                'DON_IDX': parts[11].strip(),
                'DONORTYPE': parts[12].strip(),
                'ACC_IDX': parts[13].strip(),
                'ACCEPTORTYPE': parts[14].strip(),
                'LIGCOO': parts[15].strip(),
                'PROTCOO': parts[16].strip() if len(parts) > 16 else ''
            })
        except ValueError as e:
            print(f"Error processing row: {row}")
            print(f"ValueError: {e}")
            return pd.Series()  # Skip this row if conversion fails
    else:
        return pd.Series()

# Apply the function to the halogen bond interaction DataFrame
halogen_bond_df = interaction_dfs['Halogen Bond']
halogen_bond_details = halogen_bond_df['Data'].apply(extract_halogen_bond_data)
halogen_bond_df = pd.concat([halogen_bond_df, halogen_bond_details], axis=1)
halogen_bond_df = halogen_bond_df.drop(columns=['Data', 'File'])

print(halogen_bond_df.head())



#clean all dfs 
hydrophobic_df = hydrophobic_df.dropna(subset=['RESNR'])
pi_stacking_df = pi_stacking_df.dropna(subset=['RESNR'])
hydrogen_bond_df = hydrogen_bond_df.dropna(subset = ['RESNR'])
halogen_bond_df = halogen_bond_df.dropna(subset = ['RESNR'])


# Export interactions to CSV files
hydrophobic_df.to_csv('~/Desktop/CtoAnalyze/hydrophobic_interactions.csv', index = False)
pi_stacking_df.to_csv('~/Desktop/CtoAnalyze/pi_stacking_interactions.csv', index=False)
hydrogen_bond_df.to_csv('~/Desktop/CtoAnalyze/hydrogen_bond_interactions.csv', index=False)
halogen_bond_df.to_csv('~/Desktop/CtoAnalyze/halogen_bond_interactions.csv', index=False)

print(hydrophobic_df.columns)



# #combining DFs into one for assessing atom interactions

columns_to_keep = [
    'Interaction Type', 'Directory', 'RESNR', 'RESTYPE', 'RESCHAIN', 
    'RESNR_LIG', 'RESTYPE_LIG', 'RESCHAIN_LIG', 'LIGCOO', 'PROTCOO'
]

# Select only the necessary columns from each DataFrame
hydrophobic_df = hydrophobic_df[columns_to_keep]
pi_stacking_df = pi_stacking_df[columns_to_keep]
hydrogen_bond_df = hydrogen_bond_df[columns_to_keep]
halogen_bond_df = halogen_bond_df[columns_to_keep]

# Combine all DataFrames into one
combined_df = pd.concat([hydrophobic_df, pi_stacking_df, hydrogen_bond_df, halogen_bond_df])

# Reset index if necessary
combined_df.reset_index(drop=True, inplace=True)

# Display the combined DataFrame
print(combined_df.head())

combined_df.to_csv('~/Desktop/ABDocking2/combined_results.csv', index=False)






