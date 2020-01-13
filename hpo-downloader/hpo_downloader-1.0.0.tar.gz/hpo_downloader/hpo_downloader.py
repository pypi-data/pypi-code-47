import pandas as pd
from .utils import load_urls, format_uniprot_mapping_request, load_columns
from typing import List
import urllib
import warnings
from tqdm.auto import tqdm

def get_phenotype_annotations()->pd.DataFrame:
    """Return dataframe containing phenotype HPO annotations."""
    urls = load_urls()
    df = pd.read_csv(urls["phenotype_annotation"], sep="\t")
    df.columns = load_columns()
    return df

def map_geneid_to_uniprot(gene_ids:List)->pd.DataFrame:
    urls = load_urls()
    url = urls["uniprot_uploadlists"]
    
    data = urllib.parse.urlencode(format_uniprot_mapping_request(gene_ids))
    data = data.encode("utf-8")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as f:
        df = pd.read_csv(f, sep="\t")

    unmapped_genes = set(gene_ids) - set(df["From"])

    if unmapped_genes:
        warnings.warn("Unable to map {number} gene_ids to uniprot!".format(
            number=len(unmapped_genes)
        ))

    df.columns = [
        "entrez-gene-id",
        "uniprot"
    ]
    return df

def map_geneid_to_phenotype()->pd.DataFrame:
    urls = load_urls()
    df = pd.read_csv(urls["gene_to_phenotype"], sep="\t")
    columns = df.columns[0].split(": ")[-1].split("<tab>")
    df = df.reset_index()
    df.columns = columns
    return df

def map_phenotype_to_uniprot()->pd.DataFrame:
    """Return dataframe containing mapping from phenotype to uniprot."""
    hpo = map_geneid_to_phenotype()
    uniprot = map_geneid_to_uniprot(hpo["entrez-gene-id"].unique())
    mapping = {}
    for gene_id, group in tqdm(uniprot.groupby("entrez-gene-id"), desc="Mapping Uniprot Ids to phenotypes"):
        for uniprot_id in group.uniprot:
            mapping[uniprot_id] = mapping.get(uniprot_id, []) + [
                hpo_id
                for hpo_id in hpo[hpo["entrez-gene-id"] == gene_id]["HPO-Term-ID"].values
            ]

    return pd.DataFrame(
        [
            (key, value)
            for key, values in mapping.items()
            for value in values
        ],
        columns=[
            "Uniprot_ID",
            "HPO-Term-ID"
        ]
    )