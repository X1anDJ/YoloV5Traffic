# train_yolov5.py

import os

# Paths (Update these paths according to your setup)
# Path to the cloned YOLOv5 repository
yolov5_path = '/Users/dajunxian/文档/NEU/5330 Computer Vision/mini-project-9/yolov5'

# Path to your data.yaml file
data_yaml = '/Users/dajunxian/文档/NEU/5330 Computer Vision/mini-project-9/coco_traffic_sign/data.yaml'

# Path to initial weights
weights = 'yolov5s.pt'

# Training parameters
epochs = 50
batch_size = 64  # Adjust based on your system's capacity
img_size = 512   # Reduced image size for faster training
workers = 8      # Number of data loader workers
cache = 'ram'    # Cache images in RAM for faster training

# Ensure you're in the YOLOv5 directory
os.chdir(yolov5_path)

# Construct the training command
train_command = (
    f"python train.py --device mps --img {img_size} --batch {batch_size} "
    f"--epochs {epochs} --data '{data_yaml}' --weights {weights} "
    f"--workers {workers} --cache {cache}"
)

# Print the training command for verification
print(f"Running training command:\n{train_command}\n")

# Run the training command
os.system(train_command)