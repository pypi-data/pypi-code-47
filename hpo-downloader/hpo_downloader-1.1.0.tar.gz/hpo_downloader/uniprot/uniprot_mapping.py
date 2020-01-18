import pandas as pd
import os


def uniprot_mapping(month: str) -> pd.DataFrame:
    """Return DataFrame containing the mapping between uniprot AC, ID and GeneID for the given month.

    Parameters
    ----------------------
    month:str
        The month whose mapping to be loaded.

    Returns
    ----------------------
    The Dataframe containing the mapping between uniprot AC, ID and GeneID for the given month.
    """
    if month not in ("october", "november", "december"):
        raise ValueError("Given month {month} is not available.".format(
            month=month
        ))
    return pd.read_csv(
        "{pwd}/data/{month}.tsv.gz".format(
            pwd=os.path.dirname(os.path.abspath(__file__)),
            month=month
        ),
        sep="\t"
    )
