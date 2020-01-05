import numpy as np

item_type_numeric = np.int8
item_type_text = np.dtype(('U', 128))
item_type_date = [
    ('shuffle_index', np.int32),
    ('date', np.int32),
    ('story', item_type_text)
]
item_type_image = [
    ('shuffle_index', np.int32),
    ('file', item_type_text)
]
item_type_name = [
    ('shuffle_index', np.int32),
    ('file', item_type_text),
    ('firstname', item_type_text),
    ('lastname', item_type_text) # Todo?
]
