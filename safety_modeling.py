import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import statsmodels.api as sm

world_population_data = pd.read_csv("world_population_data_processed.csv")
world_population_data = world_population_data.drop(columns=["Unnamed: 0"])

#Logarithmic Fit
x = world_population_data["education_expenditure_per_inhabitant"]
y = world_population_data["safety"]

fit = np.polyfit(np.log(x), y, 1)
y_fit = fit[1] + fit[0]*np.log(x)

sns.scatterplot(x=x, y=y, color="blue")
sns.lineplot(x=x, y=y_fit, linewidth=2, color="orange")
plt.legend(labels=['Logarithmic Fit', 'Actual Points'])

#Multiple Linear Regression
y = world_population_data["safety"]
x = world_population_data.select_dtypes(include=["int64","float64"]).drop(columns=["safety"])

X = sm.add_constant(x)
lm = sm.OLS(y, X)
model = lm.fit()
model.summary()

#Statistics
world_population_data[["safety"]].describe()
import statsmodels.stats.api as sms
sms.DescrStatsW(world_population_data["safety"]).tconfint_mean() 
