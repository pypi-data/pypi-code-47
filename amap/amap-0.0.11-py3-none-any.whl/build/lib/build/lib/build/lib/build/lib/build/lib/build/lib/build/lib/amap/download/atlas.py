import os

from amap.download.download import download
from amap.tools.system import ensure_directory_exists

default_atlas_name = "brain.nii"


atlas_urls = {
    "allen_2017": "https://gin.g-node.org/cellfinder/atlas/raw/master/allen2017.tar.gz"
}

download_requirements_gb = {"allen_2017": 1.8}

extract_requirements_gb = {"allen_2017": 11.5}


def main(atlas, atlas_dir, download_path):
    if not os.path.exists(os.path.join(atlas_dir, atlas, default_atlas_name)):
        ensure_directory_exists(atlas_dir)

        download(
            download_path,
            atlas_urls[atlas],
            atlas,
            install_path=atlas_dir,
            download_requires=download_requirements_gb[atlas],
            extract_requires=extract_requirements_gb[atlas],
        )

    else:
        print(
            f"Atlas already exists at " f"{atlas_dir}." f" Skipping download"
        )
