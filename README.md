# Mask RCNN
Mask RCNN in TensorFlow

This repo attempts to reproduce this amazing work by Kaiming He et al. : 
[Mask R-CNN](https://arxiv.org/abs/1703.06870)

## Requirements

- Python 3.6
- Python 3.6 dev headers

- [Tensorflow (>= 1.0.0)](https://www.tensorflow.org/install/install_linux)

More specifically: TensorFlow 1.6.0 or TensorFlow-GPU 1.6.0

-TensorBoard

- [Numpy](https://github.com/numpy/numpy/blob/master/INSTALL.rst.txt)
- [COCO dataset](http://mscoco.org/dataset/#download)
- Using 2017 dataset
- [Resnet50](http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz)

## How-to
0. For now you must configure settings.py and review libs/configs/config_v1.py until things are parameterized and consolidated
1. Go to `./libs/datasets/pycocotools` and run `make`
2. Download [COCO](http://mscoco.org/dataset/#download) dataset, place it into a place outside the project and configure settings.py dataset_dir, then run `python preprocess.py` to build tf-records. It takes a while.
3. Download pretrained resnet50 model, `wget http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz`, unzip it, place it into `./data/pretrained_models/`
4. Go to `./libs` and run `make`
5. run `python train/train.py` for training
6. There are certainly some bugs, please report them back, and let's solve them together.

## TODO:
- [x] ROIAlign
- [x] COCO Data Provider
- [x] Resnet50
- [x] Feature Pyramid Network
- [x] Anchor and ROI layer
- [x] Mask layer
- [x] Speedup anchor layer with cython
- [x] Combining all modules together.
- [x] Testing and debugging (in progress)
- [ ] Training / evaluation on COCO
- [ ] Add image summary to show some results
- [ ] Converting ResneXt
- [ ] Training >2 images

## Call for contributions
- Anything helps this repo, including **discussion**, **testing**, **promotion** and of course **your awesome code**.

## Acknowledgment
This repo borrows tons of code from 
- [TFFRCNN](https://github.com/CharlesShang/TFFRCNN)
- [py-faster-rcnn](https://github.com/rbgirshick/py-faster-rcnn) 
- [faster_rcnn](https://github.com/ShaoqingRen/faster_rcnn)
- [tf-models](https://github.com/tensorflow/models)

## License
See [LICENSE](https://github.com/CharlesShang/FastMaskRCNN/blob/master/LICENSE) for details.

