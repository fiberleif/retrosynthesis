import os

AUG_SIZE = 40
aug_data_dir=f"/home/guoqingliu/retro_blob/projects/reaction_prediction/data/raw/uspto_50k_rsmiles_augmented_versions/uspto_50k_PtoR_aug{AUG_SIZE}/"
filtered_aug_data_dir=f"/home/guoqingliu/retro_blob/projects/reaction_prediction/data/raw/uspto_50k_rsmiles_augmented_versions/uspto_50k_PtoR_aug{AUG_SIZE}_unique/"

for FOLD in ["train", "val", "test"]:
    src_file_name=f"{FOLD}/src-{FOLD}.txt"
    tgt_file_name=f"{FOLD}/tgt-{FOLD}.txt"

    src_file_path=os.path.join(aug_data_dir,src_file_name)
    tgt_file_path=os.path.join(aug_data_dir,tgt_file_name)

    filtered_src_file_path=os.path.join(filtered_aug_data_dir,src_file_name)
    filtered_tgt_file_path=os.path.join(filtered_aug_data_dir,tgt_file_name)

    src_file_handle = open(src_file_path, "r")
    tgt_file_handle = open(tgt_file_path, "r")

    # 1. check if src and tgt files have the same number of lines
    src_lines = src_file_handle.readlines()
    tgt_lines = tgt_file_handle.readlines()
    if len(src_lines) != len(tgt_lines):
        raise ValueError(f"src file {src_file_path} and tgt file {tgt_file_path} do not have the same number of lines")
    if len(src_lines) % AUG_SIZE != 0:
        raise ValueError(f"src file {src_file_path} and tgt file {tgt_file_path} do not have the same number of lines")

    # 2. obtain unique src strings for each AUG_SIZE lines
    total_unique_src_tgt_pairs = []
    total_unique_src_lines = []
    for i in range(0, len(src_lines), AUG_SIZE):
        # src_lines[i:i+AUG_SIZE] is a list of AUG_SIZE lines
        # tgt_lines[i:i+AUG_SIZE] is a list of AUG_SIZE lines
        curr_src_lines = src_lines[i:i+AUG_SIZE]
        curr_tgt_lines = tgt_lines[i:i+AUG_SIZE]
        curr_unique_src_tgt_pairs = list(set(zip(curr_src_lines, curr_tgt_lines)))
        curr_unique_src_lines = list(set(curr_src_lines))
        print(f"{len(curr_unique_src_tgt_pairs)} unique src-tgt pairs vs {len(curr_unique_src_lines)} unique src lines")
        total_unique_src_tgt_pairs.extend(curr_unique_src_tgt_pairs)
        total_unique_src_lines.extend(curr_unique_src_lines)

    # 3. write unique src-tgt pairs to a new file
    src_file_handle.close()
    tgt_file_handle.close()
    print("len(total_unique_src_tgt_pairs):", len(total_unique_src_tgt_pairs))
    print("len(total_unique_src_lines):", len(total_unique_src_lines))
    print("len(src_lines):", len(src_lines))

    # 获取目录路径
    filtered_src_dir = os.path.dirname(filtered_src_file_path)
    # 创建目录（如果不存在）
    print(f"Creating directory: {filtered_src_dir}")
    os.makedirs(filtered_src_dir, exist_ok=True)

    with open(filtered_src_file_path, "w") as f:
        for src_line in total_unique_src_lines:
            f.write(src_line)
    with open(filtered_tgt_file_path, "w") as f:
        for src_line, tgt_line in total_unique_src_tgt_pairs:
            f.write(tgt_line)
