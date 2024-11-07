from pathlib import Path
import sys

# Define paths to the input images
fixed_image_path = r"./data/round1_S=1_CH_1_sm.czi"
res1 = 0.325
moving_image_path = r"./data/round2_S=1_CH=1_sm.czi"
res2 = 0.325

result_path = r"./data/output"

# Check if the file exists
if Path(fixed_image_path).exists():
    print("The file exists.")
else:
    print("The file does not exist.")

# Check if the folder exists
if Path(result_path).exists() and Path(result_path).is_dir():
    print("The folder exists.")
else:
    print("The folder does not exist.")
