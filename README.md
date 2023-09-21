# Simple TitaNet

This is TitaNet as [trained and implemented by Alessio Falai](https://github.com/Wadaboa/titanet).
The original paper is [TitaNet: Neural Model for speaker representation with 1D Depth-wise separable convolutions and global context](https://arxiv.org/abs/2110.04410).
I just slightly adapted it for an easy pip install.

## Installation

```
pip install git+https://github.com/MiniXC/simple_titanet.git
```


## Usage

```python
from simple_titanet import TitaNet

model = TitaNet(load_pretrained=True)
```

