#!/bin/bash
for model in bin/MONDO_*.pkl; do
  python src/predict.py -input data/processed_refinebio_descriptions_filtered.tsv -out results/ -id data/IDs.tsv -input_embed data/my_custom_embeddings.npz -train_embed data/disease_desc_embedding.npz -model $model
done
