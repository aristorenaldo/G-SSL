# G-SSL
**Gated Self-Supervised Learning**

[[Arxiv]]()

This is an official implementation for "Mixture of Self-Supervised Learning". This implementations only provide Tiny-Imagenet classification, imbalanced classification and adversarial perturbations.

This is the diagram of the transformation from our proposed method. 
![Transformation](/imgs/transformations.png)

This is the architecture of the model from our proposed method.
![architecture](/imgs/gating-network.png)

**Dataset**
- Tiny-Imagenet [link](http://cs231n.stanford.edu/tiny-imagenet-200.zip)
- CIFAR [link](https://www.cs.toronto.edu/~kriz/cifar.html)

**Requirements**
- Python 3.10
- Pytorch 2.x
- Pyyaml
- Tensorboard
- Matplotlib
