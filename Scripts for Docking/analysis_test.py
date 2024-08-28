import os
import pandas as pd

def parse_interaction_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    interactions = []
    current_type = None

    for line in data:
        line = line.strip()
        print(f"Processing line: {line}")  # Debugging output

        if "**Hydrophobic Interactions**" in line:
            current_type = "hydrophobic"
            print("Identified Hydrophobic Interactions Section")
            continue
        elif "**pi-Stacking**" in line:
            current_type = "pi_stack"
            print("Identified Pi-Stacking Section")
            continue
        # Add similar elif statements for other interaction types

        if line.startswith('+') or not line:
            continue

        if current_type:
            print(f"Adding interaction data from line: {line}")
            interactions.append(line)  # Collect the raw line data for now

    return interactions

# Specify the path to the specific file you want to test
test_file = os.path.expanduser('~/Desktop/CtoAnalyze/PLIP_Results/TBM10_Conformation1/report.txt')

# Parse the file and print the collected interactions
interactions = parse_interaction_file(test_file)
print("Parsed interactions:", interactions)

# Convert parsed interactions to a DataFrame
df = pd.DataFrame(interactions, columns=['Interaction Data'])
print(df.head())  # Show the DataFrame

# Save to CSV
output_file = os.path.expanduser('~/Desktop/CtoAnalyze/interaction_test_summary.csv')
df.to_csv(output_file, index=False)
print(f"Data saved to '{output_file}'")
