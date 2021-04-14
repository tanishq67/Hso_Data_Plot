import matplotlib.pyplot as plt
import csv
import pandas as pd


# style.use("ggplot")

df = pd.read_csv("Book3.csv")

ax = plt.gca()
# df["year"] = [datetime.strptime(date, '%d-%m-%Y').date() for date in df["year"]]
print(df["answer"].mean(), df["answer"].mean() + df["answer"].std() )
# df.plot(x ='Year', y='answer', kind = 'line')
df.plot(x='date',y='mean',color='green',ax=ax)
df.plot(x='date',y='std',color='blue',ax=ax)
df.plot(x='date',y='answer',color='red',ax=ax)
# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt
   
# data = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
#         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
#        }
  
# df = pd.DataFrame(data,columns=['Year','Unemployment_Rate'])
# print(df)
# df.plot(x ='Year', y='Unemployment_Rate', kind = 'line')
plt.show()
