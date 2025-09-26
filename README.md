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

## Running on startup

I use a systemd service file to run this on startup.

This assumed the script is saved at `/opt/scripts/gpu-power-limit` so adjust as needed.

1. Create the system service file:
```bash
sudo nano /etc/systemd/system/gpu-power-limit.service
```

Contents:
```toml
[Unit]
Description=Set GPU power limit to 80% on boot
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/opt/scripts/gpu-power-limit 80
User=root

[Install]
WantedBy=multi-user.target
```

2. Enable the service
```bash
sudo systemctl daemon-reload
sudo systemctl enable gpu-power-limit.service
```
