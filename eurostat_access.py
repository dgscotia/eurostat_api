# Uses EUROSTAT API
# For info: https://wikis.ec.europa.eu/display/EUROSTATHELP/API+Statistics+-+data+query
# returns specific values based on filtering

import requests

gas_prices = "NRG_PC_202"
consom_gas = "4141902" # Band 2: 20 GJ - 200 GJ

elec_prices = "NRG_PC_204"
consom_elec = "4161903" # 2500 kWh - 5000 kWh

hh_energy = "NRG_D_HHQ"

# Filtering for parameters
geo = "FR"
time = "2021-S1"
currency = 'EUR'
base_url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"

def send_query(dataset, consom):
    query = f"{base_url}/{dataset}/?geo={geo}&time={time}&consom={consom}&currency={currency}&unit=KWH"
    r = requests.get(query)
    if r.status_code != 200:
        raise Exception(f"API unsuccessful with status code of {r.status_code}.")
    return r.json()

def get_elec_prices():
    data = send_query(elec_prices, consom_elec)
    x_tax = data["value"]['0'] # Excluding taxes and levies
    x_vat = data["value"]['1'] # Excluding VAT and other recoverable taxes and levies
    i_tax = data["value"]['2'] # All taxes and levies included
    levies = x_vat - x_tax
    print(f"Excluding taxes and levies: {x_tax}\nExcluding VAT: {x_vat}\nAll taxes and levies included: {i_tax}\n"
          f"Levies: {levies}")
    return x_tax, x_vat, i_tax, levies


def get_gas_prices():
    data = send_query(gas_prices, consom_gas)
    print(data)
    x_tax = data["value"]['0'] # Excluding taxes and levies
    x_vat = data["value"]['1'] # Excluding VAT and other recoverable taxes and levies
    i_tax = data["value"]['2'] # All taxes and levies included
    levies = x_vat - x_tax
    print(f"Excluding taxes and levies: {x_tax}\nExcluding VAT: {x_vat}\nAll taxes and levies included: {i_tax}\n"
          f"Levies: {levies}")
    return x_tax, x_vat, i_tax, levies

def get_hh_energy():
    pass

# get_elec_prices()
get_gas_prices()