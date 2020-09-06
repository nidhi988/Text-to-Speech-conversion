#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gtts import gTTS 
import os


# In[2]:


text = "Global warming is the long-term rise in the average temperature of the Earth’s climate system"


# In[3]:


language = 'en'


# In[4]:


speech = gTTS(text = text, lang = language, slow = False)


# In[5]:


speech.save("text.mp3")


# In[7]:


os.system("start text.mp3")


# In[ ]:




