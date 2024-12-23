new files:
 1. scripts
    1.1 generate_PtoR_50k.sh
    1.2 generate_RtoP_50k.sh
    1.3 generate_PtoR_full.sh
 2. python code
    1.1 generate_PtoR_data.py 增加了对不同dataset(e.g., 50k, full)，以及pistachio的支持
    1.2 generate_RtoP_data.py 增加了对不同dataset(e.g., 50k, full)，以及pistachio的支持
    1.3 study_PtoR_data.py 分析了Full dataset的构建问题，train/val/test -> generate_PtoR_full.sh
    1.4 check_aug_repeat_ratio.py 查看augment后的repeat情况
    1.5 filter_repeated_augmentation.py augment后去重，得到unique src-tgt pairs