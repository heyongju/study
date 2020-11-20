import pandas as pd
kto_201901 = pd.read_excel('./files/kto_201901.xlsx', header=1, usecols='A:G', skipfooter= 4)

kto_201901.head()