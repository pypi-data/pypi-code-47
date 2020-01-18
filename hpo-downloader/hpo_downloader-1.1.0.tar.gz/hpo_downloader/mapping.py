import pandas as pd
from .utils import non_unique_mapping, overlap
from .uniprot import uniprot_mapping
from .cafa4 import cafa4_mapping
from .hpo import hpo_mapping


def mapping(
    month: str,
    cafa4_only: bool
) -> pd.DataFrame:
    """Return dataframe containing mapping from phenotype to uniprot.

    Parameters
    --------------------------
    month: str,
        The month of uniprot release.
    cafa4_only: bool = False,
        Whetever to return only mapping whose uniprot ID is contained in CAFA4 annotations.

    Returns
    --------------------------
    Return dataframe containing mapping from phenotype to uniprot.
    """
    uniprot = uniprot_mapping(month)
    hpo = hpo_mapping()
    cafa4 = cafa4_mapping()
    overlap(hpo, "HPO", uniprot, "Uniprod", "gene_id")
    df = non_unique_mapping(hpo, uniprot, "gene_id")
    if cafa4_only:
        overlap(cafa4, "CAFA4", df, "HPO and Uniprod", "uniprot_id")
        df = non_unique_mapping(cafa4, df, "uniprot_id")
    return df
