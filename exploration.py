import pandas as pd
import seaborn as sns

world_population_data = pd.read_csv("world_population_data_processed.csv")

#Correlation matrix
numerical_columns = world_population_data.select_dtypes(include=["float64", "int64"])
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.heatmap(numerical_columns.corr(), cmap= 'coolwarm', vmin=-1, vmax=1, center= 0)

# Safety vs IQ (put any variable here to see its plot)
sns.set(font_scale = 1)
#sns.scatterplot(x = "iq", y = "safety", data = world_population_data).set(title='Safety vs life Expectancy')
sns.regplot(x = "iq", y = "safety", data=world_population_data).set(title='Safety vs IQ')

#Education Expenditure Boxplot
world_population_data.boxplot("education_expenditure_per_inhabitant")

#Distributions (put any variable to see its distibution)
sns.histplot(world_population_data.rights, kde = True).set(title='Number of Countries According to Rights Score')
