# nvidia-power-limit

Simple python script to set the nvidia power limit on Linux.

Usage:

```bash
pip install nvidia-ml-py

chmod +x ./nvidia-power-limit.py

./nvidia-power-limit.py [Power Limit Percentage]
```

Uses the [nvidia-ml-py](https://pypi.org/project/nvidia-ml-py/) library to interface with the GPU.

Be sure to change the BASE_POWER_LIMIT_MW to your actual GPUs base limit. You can use nvidia-smi to roughly check this.

If you have improvements, feel free to open a PR etc.

Published under MIT licence. 
