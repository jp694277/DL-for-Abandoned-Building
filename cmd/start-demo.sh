# run for test
python3 demo.py \
--images_dir=/mnt/c/Users/wangshuyi/Downloads/Test1102 \
--output_dir=./images/demo2 \
--ckpt=models/model_072000.pth \
--config-file=configs/abbd_large_iter.yaml \
MODEL.DEVICE cpu


# run for confusion matrix
python3 demo-formatrix.py \
--images_dir=/mnt/c/Users/wangshuyi/Documents/BaiduDisk/new_train_set/data \
--output_dir=/mnt/c/Users/wangshuyi/Documents/BaiduDisk/new_train_set/ \
--ckpt=models/model_072000.pth \
--config-file=configs/abbd_large_iter.yaml \
MODEL.DEVICE cpu

# run for true data
python3 demo.py \
--images_dir=/mnt/c/Users/wangshuyi/43-cities/anshan \
--output_dir=/mnt/c/Users/wangshuyi/43-cities/anshan-output \
--ckpt=models/model_072000.pth \
--config-file=configs/abbd_large_iter.yaml \
MODEL.DEVICE cpu

tensorboard --logdir=tf_logs --bind_all


# run for true data efficient net 160k iter
python3 demo.py \
--images_dir=/mnt/c/Users/wangshuyi/43-cities/anshan \
--output_dir=/mnt/c/Users/wangshuyi/43-cities/anshan-output-effi-newdata \
--ckpt=models/model_new_dataset_efficientnet_160k.pth \
--config-file=configs/abbd_efficient_net_120k.yaml \
MODEL.DEVICE cpu


# run for true data vgg19 120k iter
python3 demo.py \
--images_dir=/mnt/c/Users/wangshuyi/43-cities/anshan \
--output_dir=/mnt/c/Users/wangshuyi/43-cities/anshan-output-vgg-newdata \
--ckpt=models/model_new_dataset_VGG_120k.pth \
--config-file=configs/abbd_large_iter.yaml \
MODEL.DEVICE cpu

# run for true data efficient net 160k iter for relabel
python3 demo_for_relabel.py \
--images_dir=/mnt/c/Users/wangshuyi/43-cities/anshan \
--output_dir=/mnt/c/Users/wangshuyi/43-cities/anshan-output \
--ckpt=models/model_new_dataset_VGG_120k.pth \
--config-file=configs/abbd_large_iter.yaml \
MODEL.DEVICE cpu

# run for true data efficient net 160k iter for relabel
python3 demo_for_relabel.py \
--images_dir=/mnt/c/Users/wangshuyi/43-cities/anshan \
--output_dir=/mnt/c/Users/wangshuyi/43-cities/anshan-out-new \
--ckpt=models/model_pic3600_iter20k.pth \
--config-file=configs/abbd_iter2.yaml \
MODEL.DEVICE cpu

# 用0.75阈值的模型跑鞍山数据
python3 demo_for_relabel.py \
--images_dir=/mnt/c/Users/wangshuyi/43-cities/anshan \
--output_dir=/mnt/c/Users/wangshuyi/43-cities/anshan-output-thres0_75-175k \
--ckpt=models/model_thres0_75__iter175k.pth \
--config-file=configs/abbd_iter2_1.yaml \
MODEL.DEVICE cpu

# 用0.75阈值的模型跑营口数据
python3 demo_for_relabel.py \
--images_dir=/mnt/c/Users/wangshuyi/43-cities/yingkou \
--output_dir=/mnt/c/Users/wangshuyi/43-cities/yingkou-output-thres0_75-175k \
--ckpt=models/model_thres0_75__iter175k.pth \
--config-file=configs/abbd_iter2_1.yaml \
MODEL.DEVICE cpu

# 用最新的28k张图片，0.65阈值训练出的模型跑营口的数据
python3 demo_for_relabel.py \
--images_dir=/mnt/c/Users/wangshuyi/43-cities/yingkou \
--output_dir=/mnt/c/Users/wangshuyi/43-cities/yingkou-output-pics28k-thres0_65-200k \
--ckpt=models/model_pics28k_thres0_65_iter200k.pth \
--config-file=configs/abbd_iter6.yaml \
MODEL.DEVICE cpu

# 用最新的28k张图片，0.75阈值训练出的模型跑营口的数据
python3 demo_for_relabel.py \
--images_dir=/mnt/c/Users/wangshuyi/43-cities/yingkou \
--output_dir=/mnt/c/Users/wangshuyi/43-cities/yingkou-output-pics28k-thres0_75-200k \
--ckpt=models/model_pics28k_thres0_75_iter200k.pth \
--config-file=configs/abbd_iter7.yaml \
MODEL.DEVICE cpu