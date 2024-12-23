import os

for AUG_SIZE in [1, 5, 10, 20, 40, 80]:
    aug_data_dir=f"/home/guoqingliu/retro_blob/projects/reaction_prediction/data/raw/uspto_50k_rsmiles_augmented_versions/uspto_50k_PtoR_aug{AUG_SIZE}/"
    file_name="train/tgt-train.txt"

    # merge dir and file name
    file_path=os.path.join(aug_data_dir,file_name)

    # obtain repeat ratio for each AUG_SIZE lines, and finally the average repeat ratio
    repeat_ratio_list = []
    str_set = set()

    print(f"Calculating repeat ratio for AUG_SIZE={AUG_SIZE}...")
    # print(f"Reading file: {file_path}")
    with open(file_path, "r") as f:
        for i, line in enumerate(f):
            # print(f"line {i}: {line}")
            str_set.add(line)
            if (i + 1) % AUG_SIZE == 0:
                repeat_ratio = len(str_set) / AUG_SIZE
                repeat_ratio_list.append(repeat_ratio)
                str_set.clear()

    # calculate the average repeat ratio
    avg_repeat_ratio = sum(repeat_ratio_list) / len(repeat_ratio_list)
    print(f"Average repeat ratio for AUG_SIZE={AUG_SIZE}: {avg_repeat_ratio}")
