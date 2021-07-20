import plotly.express as px
import csv

with open("Part2.csv") as csv_file:
    df = csv.DictReader(csv_file)
   
    fig = px.scatter(df,x="week", y="Coffee in ml")
    fig.show()