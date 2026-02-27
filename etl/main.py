from etl.extract import extract_candidates
from etl.transform import transform_candidates
from etl.load import load_to_dw

FILE_PATH = "data/raw/candidates.csv"

df = extract_candidates(FILE_PATH)
tables = transform_candidates(df)
load_to_dw(tables)