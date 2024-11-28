from wsireg import WsiReg2D
import sys
import os
from pathlib import Path
from czitools.metadata_tools.scaling import CziScaling
from czitools.metadata_tools.channel import CziChannelInfo


# fixed_image_path = r"F:\Testdata_Zeiss\Pfizer\Pfizer_Multiplex\single_scenes\2019_01_15__0014_S1.czi"
# moving_image_path = r"F:\Testdata_Zeiss\Pfizer\Pfizer_Multiplex\single_scenes\2019_01_17__0033_S1.czi"

# fixed_image_path = r"F:\Github\wsireg\data\round1_S=1_CH=1_sm.czi"
# moving_image_path = r"F:\Github\wsireg\data\round2_S=1_CH=1_sm.czi"

# fixed_image_path = (
#     r"F:\Testdata_Zeiss\Co-Registration\valisdocker\spot_round1.czi"
# )
# moving_image_path = (
#     r"F:\Testdata_Zeiss\Co-Registration\valisdocker\spot_round2.czi"
# )


def register_images(
    fixed_image_path: str,
    moving_image_path: str,
    reference_channel_index: int = 0,
) -> os.PathLike:

    directory = Path(os.getcwd())
    print(f"Working Diretcory: {directory}")

    result_path = Path(fixed_image_path).parent / "output"
    modalities = ["R1", "R2"]

    if Path(fixed_image_path).exists():
        pass
    else:
        print(f"The file {fixed_image_path} does not exist.")
        sys.exit()

    # Check if the file exists
    if Path(moving_image_path).exists():
        pass
    else:
        print(f"The file {moving_image_path} does not exist.")
        sys.exit()

    # Check if the folder exists
    if Path(result_path).exists() and Path(result_path).is_dir():
        pass
    else:
        # Create the folder if it does not exist
        Path(result_path).mkdir(parents=True, exist_ok=True)

    czi_scale1 = CziScaling(fixed_image_path)
    czi_scale2 = CziScaling(moving_image_path)
    czi_ch1 = CziChannelInfo(fixed_image_path)
    czi_ch2 = CziChannelInfo(moving_image_path)

    # Adding the suffix "_reg" to each item in the list
    czi_ch2.names = [s + '_reg' for s in czi_ch2.names]

    # Check if the file exists
    if Path(fixed_image_path).exists():
        pass
    else:
        print(f"The file {fixed_image_path} does not exist.")
        sys.exit()

    # Check if the file exists
    if Path(moving_image_path).exists():
        pass
    else:
        print(f"The file {moving_image_path} does not exist.")
        sys.exit()

    # Check if the folder exists
    if Path(result_path).exists() and Path(result_path).is_dir():
        pass
    else:
        # Create the folder if it does not exist
        Path(result_path).mkdir(parents=True, exist_ok=True)

    # initialize registration graph
    reg_graph = WsiReg2D("my_reg_project", str(result_path))

    # add registration images (modalities)
    reg_graph.add_modality(
        modalities[0],
        fixed_image_path,
        image_res=czi_scale1.X,
        channel_names=czi_ch1.names,
        # channel_colors=["blue"],  # please check the number of channels !!!
        preprocessing={
            "image_type": "FL",
            "ch_indices": [reference_channel_index],
            "as_uint8": False,
            "contrast_enhance": False,
        },
    )

    reg_graph.add_modality(
        modalities[1],
        moving_image_path,
        image_res=czi_scale2.X,
        channel_names=czi_ch2.names,
        preprocessing={
            "image_type": "FL",
            "as_uint8": False,
            "invert_intensity": False,
        },
    )

    # specify merge_modalities
    reg_graph.add_merge_modalities(
        "merged",
        modalities,
    )

    # we register here the fluorescence modalities
    # using a rigid and affine parameter map
    reg_graph.add_reg_path(
        modalities[1],
        modalities[0],
        thru_modality=None,
        # reg_params=["rigid", "affine"],
        reg_params=["affine"],
    )

    # run the graph
    reg_graph.register_images()

    # save transformation data
    reg_graph.save_transformations()

    # save registered images as ome.tiff writing images and delete the individual registered images
    reg_graph.transform_images(file_writer="ome.tiff", remove_merged=True)

    return {"output_image": str(result_path)}


# Test Code locally
if __name__ == "__main__":

    # get the current working directory
    directory = Path(os.getcwd())
    filename1 = directory / Path(r"input/round1_S=1_CH=1_sm.czi")
    filename2 = directory / Path(r"input/round2_S=1_CH=1_sm.czi")

    # F:\Github\wsireg\input\round1_S=1_CH=1_sm.czi

    # execute the main function of the module
    out = register_images(filename1, filename2, reference_channel_index=0)

    print(out)
