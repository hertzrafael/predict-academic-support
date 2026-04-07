import pandas as pd
import os


df = pd.read_parquet(os.path.join(os.getcwd(), 'files', 'results', 'data_finished.parquet'))
