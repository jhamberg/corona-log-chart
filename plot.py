#!/usr/bin/env python3.7

import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, NullFormatter

countries = [
    'Finland',
    'France',
    'Germany',
    'Iran',
    'Italy',
    'Korea, South',
    'Spain',
    'Sweden',
    'US',
    'United Kingdom'
]

url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
dskip = 30 # Days to skip
fig = pd.read_csv(url) \
    .drop(columns=["Lat", "Long"]) \
    .query('`Country/Region` == @countries') \
    .groupby("Country/Region", as_index=False) \
    .sum() \
    .set_index("Country/Region") \
    .T \
    .iloc[dskip:] \
    .plot(figsize=(7,7))

plt.xlabel("Date")
plt.ylabel("Total COVID-19 Cases")
plt.yscale("log")
plt.minorticks_off()
plt.gca().yaxis.set_minor_formatter(NullFormatter())
plt.gca().yaxis.set_major_formatter(ScalarFormatter())

timestamp = time.strftime("%Y%m%d")
plt.savefig(f"{timestamp}.png")