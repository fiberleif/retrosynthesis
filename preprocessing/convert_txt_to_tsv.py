FOLD="train" # "val"

raw_src_txt_path=f"/home/guoqingliu/retro_blob/projects/reaction_prediction/data/raw/uspto_50k_rsmiles_augmented_versions/uspto_50k_PtoR_aug20/{FOLD}/src-{FOLD}.txt"
raw_tgt_txt_path=f"/home/guoqingliu/retro_blob/projects/reaction_prediction/data/raw/uspto_50k_rsmiles_augmented_versions/uspto_50k_PtoR_aug20/{FOLD}/tgt-{FOLD}.txt"

save_tsv_path=f"/home/guoqingliu/nlm_blob/guoqing/SFM_inst_tune_dataset/uspto50k/uspto50k_PtoR_rsmiles_aug20_{FOLD}.tsv"

with open(raw_src_txt_path, "r") as src_txt_handle:
    src_txt_lines = src_txt_handle.readlines()
with open(raw_tgt_txt_path, "r") as tgt_txt_handle:
    tgt_txt_lines = tgt_txt_handle.readlines()

assert len(src_txt_lines) == len(tgt_txt_lines)

with open(save_tsv_path, "w") as save_tsv_handle:
    for src_txt_line, tgt_txt_line in zip(src_txt_lines, tgt_txt_lines):
        src_txt_line = src_txt_line.strip().replace(" ", "")
        src_txt_line = "<mol>" + src_txt_line + "</mol>"
        tgt_txt_line = tgt_txt_line.strip().replace(" ", "")
        tgt_txt_line = "<mol>" + tgt_txt_line + "</mol>"
        print(f"{src_txt_line}\t{tgt_txt_line}")
        save_tsv_handle.write(f"{src_txt_line}\t{tgt_txt_line}\n")
print(f"Saved to {save_tsv_path}")
print("len(save_tsv_lines):", len(src_txt_lines))

