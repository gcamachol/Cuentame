import os
from datetime import date
from datetime import timedelta
from datetime import datetime
import psycopg2 as psy
import pandas as pd
from gspread_pandas import Spread, Client
import gspread
import numpy as np
from sqlalchemy import create_engine


engine = create_engine('postgresql://admin:danger@localhost:5432/postgres')

with pd.ExcelFile('indicadores_economicos.csv') as csv:
    df=pd.read_excel(csv)
    df.to_sql(name='Cuentame.indicadores_economicos',con=engine,if_exist='append',index=False)