# CycleGAN
N.B.: This script is a modified fork from https://github.com/vanhuyz/CycleGAN-TensorFlow
1. Place your training dataset in data/oracle2bronze/trainA and data/oracle2bronze/trainB and run build_data.py
2. Run train.py to train the model
3. Run export\_graph.py to export the model eg. export\_graph.py --checkpoint\_dir 20180412-1212
4. Run the inference.py to transfer test data
5. Run train.py --load_model (cheackpoing directory to continue to train a model)
