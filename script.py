import matplotlib.pyplot as plt
from matplotlib import style
import csv
from datetime import datetime
import pandas as pd


style.use("ggplot")

df = pd.read_csv("hso_synopsis_data.csv")

ax = plt.gca()

df["date"] = [datetime.strptime(date, '%d-%m-%Y').date() for date in df["date"]]

df.plot(x='date',y='mean',color='green',ax=ax)
df.plot(x='date',y='std',color='blue',ax=ax)
df.plot(x='date',y='price',color='red',ax=ax)
plt.show()
