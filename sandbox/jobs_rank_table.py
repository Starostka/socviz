import polars as pl
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import DataTable, TableColumn, Tabs, TabPanel

jobs = pl.read_csv('../data/jobs_forecast.csv', ignore_errors=True, try_parse_dates=True)
jobs.columns
jobs.shape
jobs.describe()

jobs['Category'].unique()
list(jobs['Industry Space Use'].unique())

jobs_industry = jobs.filter(pl.col('Category') == 'Jobs by industry')
q = jobs_industry.filter(pl.col('Geography').is_in(['Melbourne (CBD)', 'Carlton', 'Kensington', 'Parkville', 'South Yarra', 'Southbank']))

finance_ranks = q.filter(pl.col('Industry Space Use') == 'Finance and insurance').filter(pl.col('Year') <= 2025).with_columns(pl.col('Value').rank().alias('Rank')).sort('Rank', descending=True)
finance_ranks[['Geography', 'Year', 'Rank']].limit(3)

healthcare_ranks = q.filter(pl.col('Industry Space Use') == 'Health care and social assistance').filter(pl.col('Year') <= 2025).with_columns(pl.col('Value').rank().alias('Rank')).sort('Rank', descending=True)
healthcare_ranks[['Geography', 'Year', 'Rank']].limit(3)

education_ranks = q.filter(pl.col('Industry Space Use') == 'Education and training').filter(pl.col('Year') <= 2025).with_columns(pl.col('Value').rank().alias('Rank')).sort('Rank', descending=True)

# Create ColumnDataSource for each data frame
finance_source = ColumnDataSource(finance_ranks[['Geography', 'Year', 'Rank']].limit(3).to_df())
healthcare_source = ColumnDataSource(healthcare_ranks[['Geography', 'Year', 'Rank']].limit(3).to_df())
education_source = ColumnDataSource(education_ranks[['Geography', 'Year', 'Rank']].limit(3).to_df())

# Create DataTables for each data frame
finance_table = DataTable(
    source=finance_source,
    columns=[TableColumn(field='Geography', title='Geography'),
             TableColumn(field='Year', title='Year'),
             TableColumn(field='Rank', title='Rank')],
    width=400, height=200,
    index_position=-1  # Hide index column
)

healthcare_table = DataTable(
    source=healthcare_source,
    columns=[TableColumn(field='Geography', title='Geography'),
             TableColumn(field='Year', title='Year'),
             TableColumn(field='Rank', title='Rank')],
    width=400, height=200,
    index_position=-1  # Hide index column
)

education_table = DataTable(
    source=education_source,
    columns=[TableColumn(field='Geography', title='Geography'),
             TableColumn(field='Year', title='Year'),
             TableColumn(field='Rank', title='Rank')],
    width=400, height=200,
    index_position=-1  # Hide index column
)

# Create panels for each table
finance_panel = TabPanel(child=finance_table, title='Finance')
healthcare_panel = TabPanel(child=healthcare_table, title='Healthcare')
education_panel = TabPanel(child=education_table, title='Education')

# Create tabs layout
tabs = Tabs(tabs=[finance_panel, healthcare_panel, education_panel])

