import numpy
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("EducationDataset.csv")
df=pd.DataFrame(data)
print(df.info())
print(df.head())
