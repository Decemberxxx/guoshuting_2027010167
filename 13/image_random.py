import os
import random
import shutil

# 设置随机种子，以确保每次运行时结果一致
random.seed(42)

# 原始图片所在目录的路径
source_dir = r"D:\精英班\机器学习\train\train-image"

# train、test、val子目录的路径
train_dir = r"D:\精英班\机器学习\train\train"
test_dir = r"D:\精英班\机器学习\train\test"
val_dir = r"D:\精英班\机器学习\train\val"

# 创建train、test、val子目录
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# 遍历原始图片目录，获取所有图片文件名
image_files = os.listdir(source_dir)

# 将图片文件名随机打乱
random.shuffle(image_files)

# 计算train、test、val各自的图片数量
num_images = len(image_files)
num_train = int(num_images * 0.8)
num_test = int(num_images * 0.1)
num_val = num_images - num_train - num_test

# 将图片分配到train、test、val子目录中
for i, filename in enumerate(image_files):
    if i < num_train:
        # 分配到train子目录
        shutil.copy(os.path.join(source_dir, filename), os.path.join(train_dir, filename))
    elif i < num_train + num_test:
        # 分配到test子目录
        shutil.copy(os.path.join(source_dir, filename), os.path.join(test_dir, filename))
    else:
        # 分配到val子目录
        shutil.copy(os.path.join(source_dir, filename), os.path.join(val_dir, filename))
print('随机分配完成')
 