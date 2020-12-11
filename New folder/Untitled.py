

import pandas as pd



a = pd.read_excel('int.xlsx')
b = pd.read_excel('roll.xlsx')


# In[5]:


names1 = [i.lower() for i in a["Student Name"]]




names2 = [i.lower() for i in b["Students Name"]]




for i in names1:
    for j in names2:
        if i == j:
            print(i)

