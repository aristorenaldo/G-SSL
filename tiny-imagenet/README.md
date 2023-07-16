# Training Tiny-Imagenet
This baseline and configuration is based on [OpenMixup-PuzzleMix](https://github.com/Westlake-AI/openmixup/tree/main/configs/classification/tiny_imagenet/)
### Dataset
1.  Download dataset tiny-imagenet [link](http://cs231n.stanford.edu/tiny-imagenet-200.zip)
```
wget http://cs231n.stanford.edu/tiny-imagenet-200.zip
```
2. Extract into `data/` directory
```

### Train
```
python3 train_moe_rev.py -exp_str test_01 -p config/tinyimagenet_default.yaml
```
Note: You can modify the config file. Please use GPU for training.

