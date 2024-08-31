# Workflow for Public RNA-seq Studies Related to Specific Diseases

This repository contains a  workflow for finding public RNA-seq samples and studies related to specific diseases. 

## Directory Structure

- **bin/**: Contains MONDO model files (`*.pkl`) that are used to make predictions. These models are pretrained and ready to use with the provided data.
-  **data/**: 
  - `aggregated_metadata.json.gz`: Compressed JSON file containing metadata about RNA-seq experiments from refine/bio
  - `true_label__inst_type=study__task=disease.csv.gz`: Compressed CSV file with true labels related to the diseases of interest.
- **src/**: 
  - `extract_data.py`: Script to extract descriptions and accession codes from the compressed JSON metadata file.
  - `preprocess.py`: Script to clean and preprocess the extracted descriptions.
  - `embedding_lookup_table.py`: Script to generate embeddings for preprocessed descriptions.
  - `tfidf_calculator.py`: script to calculate TF-IDF scores for text data.
  - `predict.py`: Script to run predictions using pre-trained MONDO models.

- **results/**: Contains the filtered descriptions and accession codes after preprocessing the metadata.
  - `IDs.tsv`: List of accession codes after filtering out studies with no description.
  - `refinebio_descriptions_filtered.tsv`: Descriptions of the RNA-seq experiments after filtering out entries with no relevant description.
- **run/**: 
  - `run_extraction.sh`: Shell script for extracting and filtering descriptions.
  - `run_embedding_lookup_table.sh`: Shell script to generate embeddings for preprocessed descriptions.
  - `run_preprocess.sh`: Shell script to preprocess the extracted descriptions.
  - `run_predictions.sh`: Shell script to run predictions using the MONDO model files.


  
