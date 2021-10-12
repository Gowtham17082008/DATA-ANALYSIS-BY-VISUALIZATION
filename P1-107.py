import pandas as pd
import plotly.graph_objects as pg

df=pd.read_csv("data.csv")
studentId=df.loc[df["student_id"]=="TRL_xsl"]
print(studentId.groupby("level")["attempt"].mean())
graph=pg.Figure(pg.Bar(
    x=studentId.groupby("level")["attempt"].mean(),
    y=["level1","level2","level3","level4"],
    orientation="h"
))
graph.show()
