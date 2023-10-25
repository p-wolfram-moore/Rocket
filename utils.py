import numpy as np
import pandas as pd

def flattened_array_ordering(dimensions : tuple, verbose : bool = True):

    m, n = dimensions


    pixel_id = np.arange(m*n).reshape((m,n))

    out = pd.DataFrame()

    out['row_wise'] = pixel_id.ravel()
    out['col_wise'] = pixel_id.T.ravel()

    diag1 = np.hstack([np.diag(pixel_id, k=k) for k in range(-m,n)])

    pixel_id_flipped = np.flip(pixel_id, axis=0)

    diag2 = np.hstack([np.diag(pixel_id_flipped, k=k) for k in range(-m,n)])

    out['diagonal_1'] = diag1
    out['diagonal_2'] = diag2
    
    return out

def convert_to_numeric_string(df : pd.DataFrame, columns : bool = None) -> pd.DataFrame:

    if columns is None:
        columns = df.columns
    for column_name in columns:
        df[column_name] = df[column_name].apply(lambda x: str(x).zfill(2))

    return df