from apeer_dev_kit import adk
from coregistration import register_images

"""
This script performs image coregistration.
Functions:
    main: The main function that gets inputs, performs image coregistration, and finalizes the output.
Usage:
    Run this script as the main module to perform image coregistration. The inputs are obtained from the apeer_dev_kit,
    and the coregistration is performed using the register_images function from the coregistration module.
Inputs:
    input_image1 (str): Path to the first input image.
    input_image2 (str): Path to the second input image.
    reference_channel_index (int): Index of the reference channel for coregistration.
Outputs:
    output_folder (str): Path to the folder containing the coregistration results.
"""

if __name__ == "__main__":
    # get the inputs from the module
    inputs = adk.get_inputs()

    # show the inputs
    print(inputs)

    imagefile1: str = inputs["input_image1"]
    imagefile2: str = inputs["input_image2"]
    reference_channel_index: int = inputs["reference_channel_index"]

    outputs = register_images(imagefile1, imagefile2, reference_channel_index)

    # finalize the output
    # adk.set_file_output("result_folder", outputs["output_image"])
    adk.finalize()
