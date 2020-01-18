import pandas as pd


def hpo_mapping() -> pd.DataFrame:
    """Return dataframe containing phenotype HPO mapping."""
    df = pd.read_csv(
        "http://compbio.charite.de/jenkins/job/hpo.annotations.monthly/lastSuccessfulBuild/artifact/annotation/ALL_SOURCES_ALL_FREQUENCIES_genes_to_phenotype.txt",
        sep="\t"
    )
    columns = df.columns[0].split(": ")[-1].split("<tab>")
    df = df.reset_index()
    df.columns = columns
    df = df.drop(columns=[
        "entrez-gene-symbol",
        "HPO-Term-Name"
    ])
    df = df.rename(columns={
        "entrez-gene-id": "gene_id",
        "HPO-Term-ID": "hpo_id"
    })
    return df
