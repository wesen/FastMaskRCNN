dataset_dir = 'data/sampledata/'  # base directory containing layout described in data/README.md
tf_device = '/cpu:0'  # /cpu:0 or /gpu:0
model_file = 'data/pretrained_models/resnet_v1_50.ckpt'  # location of ResNet50, ResNet101, ResNeXtv2 pretrained graph and weights
checkpoint_dir = 'data/training/ckpt/'
logdir = 'output/mask_rcnn/'  # output directory for TensorBoard
train_split_name = 'train2017'
val_split_name = 'val2017'  # name of zip file without the extension val2017, val2014
