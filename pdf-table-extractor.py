#!/usr/bin/env python
# coding: utf-8

# In[35]:


#import camelot
import camelot
tables = camelot.read_pdf('foo.pdf')

tables.export('foo.csv', f='csv', compress=True) # json, excel, html
tables[0].to_csv('foo.csv') # to_json, to_excel, to_html

tables[0].df # get a pandas DataFrame!











