import pandas as pd
import os
import shutil
from encodeproject import download


def cafa4_mapping() -> pd.DataFrame:
    """Return DataFrame containing CAFA4 and Uniprot IDs."""
    # List of the paths considered in the function
    paths = [
        "cafa4.tar.gz",
        "CAFA4-export/TargetFiles/sp_species.9606.tfa"
    ]
    if not any(os.path.exists(path) for path in paths):
        # Downloading the url to the given path
        download(
            url="https://www.biofunctionprediction.org/cafa-targets/CAFA4-export.tgz",
            path=paths[0]
        )
        # Extracting the acquire
        shutil.unpack_archive(paths[0], ".")
        # Delete the archived file
        os.remove(paths[0])
    # Parse the file and retrieve the IDs from the fasta file
    f = open(paths[1], "r")
    df = pd.DataFrame(
        (
            line[1:-1].split(" ")
            for line in f.readlines()
            if line.startswith(">")
        ),
        columns=[
            "cafa4_id",
            "uniprot_id"
        ]
    )
    f.close()
    # Return the obtained IDs
    return df
