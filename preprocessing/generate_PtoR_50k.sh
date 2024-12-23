# augumentation 1
# python generate_PtoR_data.py -dataset USPTO_50K -augmentation 1 -processes 24

# augumentation 5
# python generate_PtoR_data.py -dataset USPTO_50K -augmentation 5 -processes 24

# # augumentation 10
# python generate_PtoR_data.py -dataset USPTO_50K -augmentation 10 -processes 24

# # augumentation 20
# python generate_PtoR_data.py -dataset USPTO_50K -augmentation 20 -processes 24

# # augumentation 40
# python generate_PtoR_data.py -dataset USPTO_50K -augmentation 40 -processes 24

# augumentation 80
# python generate_PtoR_data.py -dataset USPTO_50K -augmentation 80 -processes 24

# augumentation 20, randomized smiles for both sides
python generate_PtoR_data.py -dataset USPTO_50K -augmentation 20 -processes 24 -canonical

# augumentation 40, randomized smiles for both sides
python generate_PtoR_data.py -dataset USPTO_50K -augmentation 40 -processes 24 -canonical