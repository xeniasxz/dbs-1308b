#!/usr/bin/env python
# coding: utf-8

# In[16]:


from flask import Flask, render_template,request
# flask 5000
# jupyter 8888


# In[17]:


import joblib


# In[18]:


app = Flask(__name__)
#double underscore XX will be registered by python that you
# are the write and anyone else who take it will not work? 


# In[19]:


@app.route("/", methods=["GET","POST"])
def index():
        if request.method == "POST":
        #"method" vs "methods"
            rates = float(request.form.get("rates"))
            print(rates)
            model1 = joblib.load("regression_DBS")
            pred1 = model1.predict([[rates]])
            model2 = joblib.load("tree_DBS")
            pred2 = joblib.predict([[rates]])
               
            return (render_template("index.html", result1=pred1, result2=pred2))
        else:
            return (render_template("index.html", result1="waiting", result2="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




