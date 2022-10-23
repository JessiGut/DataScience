from plotnine import *
import pandas as pd

df = pd.read_csv("/home/isabel/FEI_projects/DataScience/BigData/Iris.csv")


fig = (ggplot(df, aes('PetalWidthCm', 'PetalLengthCm')) +
  geom_point())

print(fig)