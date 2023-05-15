import requests
import csv
import datetime

# Dataset codes and URL
gas_prices = "NRG_PC_202"
elec_prices = "NRG_PC_204"
hh_energy = "NRG_D_HHQ"
format = "SDMX-CSV"
host_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

# Select dataset to download and filter
dataset_code = elec_prices
currency = "EUR"
unit = "KWH"

"https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/NRG_PC_202/"

# Create query URL
query = f"{host_url}/{dataset_code}?{format}"

# Send API request
r = requests.get(query)

# Check if request was successful
if r.status_code != 200:
    raise Exception(f"API unsuccessful with status code of {r.status_code}.")

# Parse CSV data from response content
csv_data = csv.reader(r.content.decode('utf-8').splitlines())

# Save CSV file
today = datetime.datetime.today().strftime('%Y-%m-%d')
filename = f"eurostat_electricity_prices_{today}.csv"
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in csv_data:
        writer.writerow(row)
