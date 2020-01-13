from typing import List, Dict

def format_uniprot_mapping_request(gene_ids:List)->Dict:
    return {
        "from": "P_ENTREZGENEID",
        "to": "ID",
        "format": "tab",
        "query": " ".join([
            str(gene_id)
            for gene_id in gene_ids
        ])
    }