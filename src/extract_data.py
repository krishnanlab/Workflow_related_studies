# src/extract_data.py

import gzip
import json
import pandas as pd

# File paths
input_file = 'data/aggregated_metadata.json.gz'
output_desc_file = 'results/refinebio_descriptions_filtered.tsv'
output_ids_file = 'results/IDs.tsv'

# Load and parse the compressed JSON file
with gzip.open(input_file, 'rt', encoding='utf-8') as f:
    data = json.load(f)

# Extract experiments
experiments = data.get('experiments', {})
df = pd.DataFrame.from_dict(experiments, orient='index')

# Filter out entries with no descriptions
no_description_terms = [
    'No description.', 'No description available.', 'N/A', 'Not available',
    'none provided', '', None
]
filtered_df = df[~df['description'].str.strip().isin(no_description_terms)]

# Save descriptions
descriptions = filtered_df['description']
descriptions.to_csv(output_desc_file, sep='\t', index=False, header=False)

# Save accession codes
accession_codes = filtered_df['accession_code']
accession_codes.to_csv(output_ids_file, sep='\t', index=False, header=None)

print(f"Extracted {len(descriptions)} descriptions and saved to {output_desc_file}")
print(f"Saved {len(accession_codes)} accession codes to {output_ids_file}")

