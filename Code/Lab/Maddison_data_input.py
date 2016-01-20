"""
Maddison project
Long histories of GDP and population 

Links
http://www.ggdc.net/maddison/maddison-project/home.htm
http://www.ggdc.net/maddison/maddison-project/data.htm 

Written by Dave Backus, January 2016 
Created with Python 3.5 
"""
"""
import packages, check versions 
"""
import sys 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

print('\nPython version: ', sys.version) 
print('\nPandas version: ', pd.__version__) 

"""
read data 
"""
url = 'http://www.ggdc.net/maddison/maddison-project/data/mpd_2013-01.xlsx'
mpd = pd.read_excel(url, skiprows=2, index_col=0, na_values=[' ']) 

mpd.shape
list(mpd)

mpd = mpd[['England/GB/UK', 'USA', 'Japan ', 'China ', 'India ', 'Argentina ']].dropna()
mpd = mpd.rename(columns={'England/GB/UK': 'UK'})
mpd = np.log(mpd)/np.log(2)
list(mpd)

#%%
"""
plots
"""
ax = mpd.plot(lw=2)
ax.set_title('GDP per person', fontsize=14, loc='left')
#ax.set_yscale('log')
ax.set_ylabel('GDP Per Capita (1990 USD, log2 scale)')
# legend paramaters: http://matplotlib.org/users/customizing.html  
ax.legend(loc='upper left', fontsize=10, handlelength=2, labelspacing=0.15)
fig = ax.get_figure()
fig.savefig('Maddison-GDP-1870-on.pdf', bbox_inches='tight')
fig.show()
