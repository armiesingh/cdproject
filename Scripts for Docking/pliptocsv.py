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

        # Identify the start of a new interaction type section
        if "**Hydrophobic Interactions**" in line:
            current_type = "Hydrophobic Interaction"
            print("Identified Hydrophobic Interactions Section")
            continue
        elif "**pi-Stacking**" in line:
            current_type = "pi-Stacking"
            print("Identified pi-Stacking Section")
            continue
        elif "**Hydrogen Bonds**" in line:
            current_type = "Hydrogen Bond"
            print("Identified Hydrogen Bonds Section")
            continue
        elif "**Halogen Bonds**" in line:
            current_type = "Halogen Bond"
            print("Identified Halogen Bonds Section")
            continue
        elif "**Water Bridges**" in line:
            current_type = "Water Bridge"
            print("Identified Water Bridges Section")
            continue
        elif "**Salt Bridges**" in line:
            current_type = "Salt Bridge"
            print("Identified Salt Bridges Section")
            continue
        elif "**pi-Cation Interactions**" in line:
            current_type = "pi-Cation Interaction"
            print("Identified pi-Cation Interactions Section")
            continue

        if line.startswith('+') or not line:
            continue

        if current_type:
            print(f"Adding interaction data: {line} as {current_type}")
            interactions.append({"Interaction Type": current_type, "Data": line})  # Associate each line with its type

    return interactions

# Directory containing your text files in subdirectories
root_directory = os.path.expanduser('~/Desktop/ABDocking2/PLIP_Results')

# Iterate over each file in all subdirectories and parse interactions
all_interactions = []
for subdir, dirs, files in os.walk(root_directory):
    for filename in files:
        if filename.endswith('.txt'):
            file_path = os.path.join(subdir, filename)
            print(f"Processing file: {file_path}")  # Debugging output
            interactions = parse_interaction_file(file_path)
            for interaction in interactions:
                interaction['File'] = filename
                interaction['Directory'] = os.path.basename(subdir)
            all_interactions.extend(interactions)

# Convert to DataFrame for analysis
df = pd.DataFrame(all_interactions)
print(df.head())  # Show the DataFrame

# Save to CSV
output_file = os.path.expanduser('~/Desktop/ABDocking2/interaction_analysis_summary.csv')
df.to_csv(output_file, index=False)

print(f"Data analysis complete. Summary saved to '{output_file}'")
