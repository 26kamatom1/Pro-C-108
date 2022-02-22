import random
from unicodedata import name
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
count =[]
diceresult = []
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)
    count.append(i)
import statistics as st
mean=st.mean(diceresult)
median=st.median(diceresult)
mode=st.mode(diceresult)
sd=st.stdev(diceresult)
print(mean)
print(median)
print(mode)

