#!/bin/bash
python embedding_lookup_table.py \
    -input /results/processed_refinebio_descriptions_filtered.tsv \
    -out /results/my_custom_embeddings.npz \
    -model biomedbert_abs \
    -batch_size 2000
