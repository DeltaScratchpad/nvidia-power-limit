#!/usr/bin/env python3

import sys
from pynvml import *

# Define the base power limit (100%) in milliwatts
BASE_POWER_LIMIT_MW = 215000

def set_power_limit(percentage):
    """
    Sets the GPU power limit based on a percentage of the base limit.
    """
    try:
        nvmlInit()
        device = nvmlDeviceGetHandleByIndex(0)

        if not 0 <= percentage <= 100:
            print("Error: Percentage must be between 0 and 100.")
            sys.exit(1)

        new_limit_mw = int((percentage / 100) * BASE_POWER_LIMIT_MW)
        nvmlDeviceSetPowerManagementLimit(device, new_limit_mw)
        print(f"GPU power limit set to {percentage}% ({new_limit_mw} mW).")

    except NVMLError as error:
        print(f"NVML Error: {error}")
        sys.exit(1)
    finally:
        try:
            nvmlShutdown()
        except NVMLError:
            pass

def main():
    """
    Main function to handle command-line arguments.
    """
    if len(sys.argv) > 2:
        print("Usage: gpu-power-limit [percentage]")
        sys.exit(1)

    if len(sys.argv) == 2:
        try:
            percentage = float(sys.argv[1])
            set_power_limit(percentage)
        except ValueError:
            print("Error: Argument must be a number.")
            sys.exit(1)
    else:
        # No argument provided, reset to 100%
        set_power_limit(100)

if __name__ == "__main__":
    main()
