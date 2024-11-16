import numpy as np
import pandas as pd

# This CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')
print(ds)
import numpy as np
def most_expensive (address, price):
    return "The house with address" + address + "is the most expensive and its price is" + price + "Euros"
ds.sort_values("price")
print(most_expensive(ds.loc[15334, "address"],ds.loc[15334, "price"]))