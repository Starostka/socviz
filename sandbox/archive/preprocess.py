import polars as pl
from datetime import date, time
from polars.dataframe import DataFrame
from rich import print
from pathlib import Path
from typing import Protocol
from dataclasses import dataclass

pl.toggle_string_cache(True)

DATASET1: Path = 'data/Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv'
DATASET2: Path = 'data/Police_Department_Incident_Reports__2018_to_Present.csv'


# @dataclass
# class Dataset(Protocol):
#     PoliceDepartmentID: int
#     IncidentNumber: int
#     IncidentCode: int
#     Category: str
#     Description: str
#     WeekDay: str
#     Date: date
#     Time: time
#     PoliceDepartmentDestrict: str
#     Address: str
#     X: str
#     Y: str
#     Location: str


# preprocessing steps:
# - cast correct types
# - remove null entries
# - rename columns (matching datasets)

# dataset = pl.read_csv(DATASET1, try_parse_dates=True, n_rows=10)
# dataset.schema
# dataset.with_columns([   
#     pl.col('PdId').alias('PoliceDepartmentID'),
#     pl.col('Incident Code').alias('IncidentCode'),
#     pl.col('Time').str.strptime(
#         datatype = pl.Time,
#         fmt='%H:%M'
#     ),
#     pl.col('Category').cast(pl.Categorical())
# ])
# dataset.select([pl.col('PoliceDepartmentID'), pl.col('IncidentCode'), pl.col('Time'), pl.col('Date'), pl.col('Category'), ])

def preprocess_dataset1(n_rows: int = None, print_schema = False, dataset_path: Path = DATASET1) -> DataFrame:
    dataset = pl.read_csv(dataset_path, try_parse_dates=True, n_rows=n_rows)
    if print_schema:
        print(dataset.schema)
    dataset = dataset.drop_nulls()
    dataset = dataset.with_columns(
        [
            pl.col('Time').str.strptime(
                datatype = pl.Time,
                fmt='%H:%M'
            ),
            pl.col('Category').cast(pl.Categorical())
        ]
    )
    # TODO: remove columns not needed and prefixes "DELETE - " 
    return dataset
#ds1 = preprocess_dataset1(DATASET1, print_schema=True)

def preprocess_dataset2(n_rows: int = None, print_schema = False, dataset_path: Path = DATASET2) -> DataFrame:
    dataset = pl.read_csv(dataset_path, try_parse_dates=True, ignore_errors=True, n_rows=n_rows)
    if print_schema:
        print(dataset.schema)
    # dataset = dataset.drop_nulls()
    dataset = dataset.with_columns([
        pl.col('Incident Date').alias('Date'),
        pl.col('Incident Year').alias('Year'),
        pl.col('Incident Time').str.strptime(
            datatype = pl.Time,
            fmt='%H:%M'
        ).alias('Time'),
        # pl.col('Category').cast(pl.Categorical())
    ])
    # TODO: remove columns not needed and prefixes "DELETE - " 
    return dataset
#ds2 = preprocess_dataset2(n_rows = 10, print_schema = True)

# this function combines the two datasets
def combined_dataset():
    ds1 = preprocess_dataset1()
    ds2 = preprocess_dataset2()

    shared_columns = ['ROBBERY','GAMBLING','PROSTITUTION','STOLEN PROPERTY','VANDALISM','LIQUOR LAWS','NON-CRIMINAL','OTHER OFFENSES','DISORDERLY CONDUCT','EMBEZZLEMENT','MISSING PERSON','ARSON','SUSPICIOUS OCC','RECOVERED VEHICLE','FRAUD','BURGLARY','SUICIDE','ASSAULT']

def get_lightweight_dataset():
    return preprocess_dataset1(n_rows=50).to_pandas()

