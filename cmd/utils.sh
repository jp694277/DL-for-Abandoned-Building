# 从一个目录复制到另一个目录
python3 copy_images_by_gt.py \
--gt_file=/mnt/c/Users/wangshuyi/Downloads/relabel_results/relabel_images.xlsx \
--origin_dir=/mnt/c/Users/wangshuyi/43-cities/anshan \
--target_dir=/mnt/c/Users/wangshuyi/Downloads/relabel_results/images

# 从一个目录中删除另一个目录中的文件
python3 delete_files_in_dir.py \
--target_dir=/mnt/c/Users/wangshuyi/Documents/BaiduDisk/new_train_set/new_abbd \
--intersect_dir=/mnt/c/Users/wangshuyi/Downloads/relabel_results/images

python3 filter_gt.py \
--gt_file=/mnt/c/Users/wangshuyi/43-cities/anshan-output/predict_outputs.csv \
--target_dir=/mnt/c/Users/wangshuyi/Downloads/relabel_results/images \
--output=/mnt/c/Users/wangshuyi/Downloads/relabel_results/filtered_gt.csv

python3 rename_with_cityname.py \
--city_name=anshan \
--target_dir=/mnt/c/Users/wangshuyi/Downloads/relabel_results/images

# divide and zip the output images into <batch_num> .zip files
python3 /mnt/c/Users/wangshuyi/Documents/GitHub/big-data-system/my-ssd/utils/divide_and_zip.py --batch_num=6 --target_dir=. --output_dir=/mnt/c/Users/wangshuyi/Downloads

python3 filter_gt.py \
--gt_file=/mnt/c/Users/wangshuyi/43-cities/anshan-output-thres0_75-175k/predict_outputs_abandoned.csv \
--target_dir=/mnt/c/Users/wangshuyi/Downloads/anshan_56 \
--output=/mnt/c/Users/wangshuyi/Downloads/anshan_56_filtered_gt.csv

python3 data_transform.py --image_input_dir=/mnt/c/Users/wangshuyi/Documents/BaiduDisk/new_train_set/new_abbd \
--gt_file=/mnt/c/Users/wangshuyi/Documents/BaiduDisk/new_train_set/new_abbd_gt_xxyy.xlsx \
--image_output_dir=/mnt/c/Users/wangshuyi/Downloads/augmented_data/images \
--gt_output_path=/mnt/c/Users/wangshuyi/Downloads/augmented_data/aug_gt.xls \
--aug_prefix=scale1_3

python3 annotation_change_into_xyxy.py --source=/mnt/c/Users/wangshuyi/Documents/BaiduDisk/new_train_set/new_abbd_ground_truth.xlsx \
--output_path=/mnt/c/Users/wangshuyi/Documents/BaiduDisk/new_train_set/new_abbd_gt_xxyy.xls

python3 copy_images_by_gt.py \
--gt_file=/mnt/c/Users/wangshuyi/Downloads/relabels/mudanjiang/mudanjiang_sum.xlsx \
--origin_dir=/mnt/c/Users/wangshuyi/43-cities/mudanjiang/MDJ \
--target_dir=/mnt/c/Users/wangshuyi/Downloads/relabels/mudanjiang/data_images

# 先rename图片名，再过滤gt，最后再把xywh式的annotations转化为xyxy式的

python3 rename_with_cityname.py \
--city_name=kuancheng \
--target_dir=/mnt/c/Users/wangshuyi/Downloads/relabels/kuancheng/data_images

python3 filter_gt.py \
--gt_file=/mnt/c/Users/wangshuyi/43-cities/kuanchengqu-output-thres0_75-175k/predict_outputs_abandoned.csv \
--target_dir=/mnt/c/Users/wangshuyi/Downloads/relabels/kuancheng/data_images \
--output=/mnt/c/Users/wangshuyi/Downloads/relabels/kuancheng/filtered_gt.csv

python3 data_transform.py --image_input_dir=/mnt/c/Users/wangshuyi/Documents/BaiduDisk/new_train_set/new_abbd \
--gt_file=/mnt/c/Users/wangshuyi/Documents/BaiduDisk/new_train_set/new_abbd_gt_xxyy.xlsx \
--image_output_dir=/mnt/c/Users/wangshuyi/Downloads/augmented_data \
--type_of_aug=rotate20