#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from imutil import paths


# In[3]:


# Import Dataset
PATH = 'C:/Users/nuvin/OneDrive/Desktop/360_Gemstone_Images'


# In[6]:


# Resize the images

# Load the image
image = cv2.imread('example_image.jpg')

# Specify the desired dimensions for the resized image
width = 640
height = 480

# Resize the image using cv2.resize()
resized_image = cv2.resize(image, (width, height))

# Display the original and resized images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




