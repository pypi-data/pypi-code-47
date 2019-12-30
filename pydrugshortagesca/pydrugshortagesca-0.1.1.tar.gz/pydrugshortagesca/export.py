from .api import Session

import csv

CSV_MAPPINGS = {
    'drug_id' : 'drug.id',
    'drug_code' : 'drug.drug_code',
    'company_id' : 'drug.company.id', 
    'company_name' : 'drug.company.name',
    'company_type' : 'drug.company.company_type',
    'shortage_reason_en' : 'shortage_reason.en_reason',
    'shortage_reason_fr' : 'shortage_reason.fr_reason',
    'shortage_reason_active' : 'shortage_reason.active',
    'discontinuance_reason_en' : 'discontinuance_reason.en_reason',
    'discontinuance_reason_fr' : 'discontinuance_reason.fr_reason',
    'discontinuance_reason_active' : 'discontinuance_reason.active',
    'type' : 'type.label',
}

def _find_csv_mappings(row, mappings):
    newcols = {}
    for field, path in mappings.items():
        newcols[field] = row
        for key in path.split('.'):
            if key not in newcols[field]: 
                del newcols[field]
                break 
            newcols[field] = newcols[field][key]
    return newcols
        
def isearch_flatten(session, shortages=True, _filter=None, mappings=CSV_MAPPINGS, **kwargs):
    """Return a flattened version of the search results"""
    for row in session.isearch(_filter=_filter, **kwargs):
        newrow = {k:v for k,v in row.items() if isinstance(v,(int,float,str,bool))}
        newrow.update(_find_csv_mappings(row, mappings))
        newrow = {k:str(v).replace('\r\n',' ') for k,v in newrow.items()}
        yield newrow

def as_csv(session, csvfile, shortages=True, _filter=None, mappings=CSV_MAPPINGS, **kwargs):
    """Serializes search results as a CSV formatted table.
    
        csvfile is a writable file-like object
        shortages if True then only shortages are returned, otherwise only discontinuations
    """

    first = True
    __filter = lambda x: filter(_filter,x) and (shortages == (x['type']['label'] == 'shortage'))

    for row in isearch_flatten(session, _filter=__filter, **kwargs):
        if first: 
            writer = csv.DictWriter(csvfile, fieldnames=row.keys(), extrasaction='ignore')
            writer.writeheader()
            first = False
        writer.writerow(row)

# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4
