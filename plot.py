#!/usr/bin/env python3.7

import time
import csv
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, NullFormatter

population = {
    'Finland': 5.513,
    'Germany': 82.790,
    'Iran': 81.160,
    'Italy': 60.480,
    'Japan': 126.800,
    'Korea:  South': 51.470,
    'Spain': 46.660,
    'Sweden': 10.120,
    'US': 327.000,
    'United Kingdom': 66.440
}
countries = list(population.keys())

parser = argparse.ArgumentParser('plot.py')
parser.add_argument('-d', '--data', dest='dataset', default='confirmed', help="dataset (default: confirmed), possible values: confirmed, recovered, deaths")
parser.add_argument('-l', '--linear', dest='linear', action='store_true', help="use linear scale (default: false)")
parser.add_argument('-pc', '--per-capita', dest='per_capita', action='store_true', help="show values per million people (default: false)")
args = parser.parse_args()

url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_{args.dataset}_global.csv'
dskip = 30 # Days to skip
fig = pd.read_csv(url) \
    .drop(columns=["Lat", "Long"]) \
    .query('`Country/Region` == @countries') \
    .groupby("Country/Region", as_index=False) \
    .sum() \
    .set_index("Country/Region") \
    .T \
    .iloc[dskip:]

yscale = "linear" if args.linear else "log"
ylabel = f"{args.dataset.capitalize()}"

if (args.per_capita):
    # Divide values of each country by its population
    df = df.apply(lambda x: x / population[x.name])
    ylabel = ylabel + " (per million)"

df.plot(figsize=(7,7))

plt.xlabel("Date")
plt.ylabel("Total COVID-19 Cases")
plt.yscale("log")
plt.minorticks_off()
plt.gca().yaxis.set_minor_formatter(NullFormatter())
plt.gca().yaxis.set_major_formatter(ScalarFormatter())

timestamp = time.strftime("%Y%m%d")
plt.savefig(f"{timestamp}.png")