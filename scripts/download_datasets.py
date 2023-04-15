import os
import pathlib
from glob import glob
from urllib.request import urlretrieve
from functools import partial
from dataclasses import dataclass, astuple

DATA_DIR = './data'

@dataclass
class Dataset:
    name: str
    url: str

    def __iter__(self):
        return iter(astuple(self))

d1 = Dataset(
    name = 'jobs_forecast', 
    url = 'https://data.melbourne.vic.gov.au/api/explore/v2.1/catalog/datasets/city-of-melbourne-jobs-forecasts-by-small-area-2020-2040/exports/csv?lang=en&timezone=Europe%2FBerlin&use_labels=true&delimiter=%2C'
)
d2 = Dataset(
    name = 'population_forecast', 
    url = 'https://data.melbourne.vic.gov.au/api/explore/v2.1/catalog/datasets/city-of-melbourne-population-forecasts-by-small-area-2020-2040/exports/csv?lang=en&timezone=Europe%2FBerlin&use_labels=true&delimiter=%2C'
)
d3 = Dataset(
    name = 'dwellings_and_household', 
    url = 'https://data.melbourne.vic.gov.au/api/explore/v2.1/catalog/datasets/city-of-melbourne-dwellings-and-household-forecasts-by-small-area-2020-2040/exports/csv?lang=en&timezone=Europe%2FBerlin&use_labels=true&delimiter=%2C'
)
d4 = Dataset(
    name = 'floor_space', 
    url = 'https://data.melbourne.vic.gov.au/api/explore/v2.1/catalog/datasets/city-of-melbourne-floor-space-forecasts-by-small-area-2020-2040/exports/csv?lang=en&timezone=Europe%2FBerlin&use_labels=true&delimiter=%2C'
)
d5 = Dataset(
    name = 'activity_monitor', 
    url = 'https://data.melbourne.vic.gov.au/api/explore/v2.1/catalog/datasets/development-activity-monitor/exports/csv?lang=en&timezone=Europe%2FBerlin&use_labels=true&delimiter=%2C'
)

for name, url in [d1, d2, d3, d4, d5]:
    urlretrieve(url, os.path.join(DATA_DIR, f"{name}.csv"))