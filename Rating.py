#import plotly.express as px
#import plotly.figure_factory as ff
#import pandas as pd 
#import csv

#df=pd.read_csv('data(4).csv')


#fig=ff.create_distplot([df['Avg Rating'].tolist()],['Mobile Brand'] show_hist=False)
#fig.show()

import pandas as pd 
import csv 
import plotly.figure_factory as ff

df=pd.read_csv('data(4).csv')



fig=ff.create_distplot([df['Avg Rating'].tolist()], ['Mobile Brand'])

