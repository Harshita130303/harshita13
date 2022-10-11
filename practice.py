import tkinter as tk
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

app=tk.Tk()
app.title("harshita130303")
app.geometry('500x500')


cols=['user_id','movie_id','rating','ts']
df = pd.read_csv('u.data',sep='\t',names=cols).drop('ts',axis=1)
item_cols=['movie_id','title']+[str(i)for i in range(22)]
df1=pd.read_csv('u.item',sep='|',names=item_cols,encoding='ISO-8859-1')
movie=pd.merge(df,df1,on='movie_id')


result = tk.Variable(app)
box = tk.Listbox(app,height=10)
for row,val in movie.itemrows():
    print(val['title'])
box.insert(row+1,val['title'])

box.place(x=10,y=10)

def get_movie():
    pass

tk.Button(app,text='Find Recommendations',font=('Arial',22),command=get_movie).place(x=50,y=50)
tk.label(app,textvariable=result,font=('Arial',22)).place(x=200,y=100)

app.mainloop()