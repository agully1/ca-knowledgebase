#!/usr/bin/env python
# coding: utf-8

# # FDTD Tutorial 1: Simple 2D plate
# 
# ```{warning}
# This section is currently under development. Content may not be complete, links may be broken, etc.
# ```
# 
# In this tutorial, we will use a simple explicit FDTD scheme to simulate wave propagation in two dimensions.
# 
# :::{note}
# You can run this code directly in your browser by clicking on the rocket logo at the top of the page, and clicking 'Binder'. This will open a Jupyter Notebook in a [Binder](https://mybinder.org/) environment which is set up to contain everything you need to run the code. **Don't forget to save a local copy if you make any changes!**
# 
# If you are new to using Jupyter Notebooks, [this guide](https://www.dataquest.io/blog/jupyter-notebook-tutorial/) will help you get started.
# :::
# 
# ## Prequisites
# 
# None.
# 
# 
# ## Setup
# 
# We will use the `numpy` library for convenient handling of arrays, the `matplotlib.pyplot` library for plotting the output, and the `scipy.io.wavfile` library to allow us to write the resulting audio to a wav file.
# 

# In[1]:


import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import numpy as np


# 
# ## Initial example
# 
# The first thing we will do is set up a 2D domain for simulation. We will provide the domain size, as well as the material properties (density and bulk modulus) - in this case, we'll use properties for air. This is a homogeneous simulation: the material properties are the same throughout.
# 

# In[2]:


# Simple example code


# The next thing we need to do is decide upon our temporal and spatial step sizes. Here we meet an important consideration for FDTD (and all explicit, time-stepping) simulations: the Courant-Friedrichs-Lewy condition.

# In[3]:


# More code


# We will now set up arrays to hold velocity and pressure values during the simulation, and define our input signal and input and output (source and reciever) locations.

# In[4]:


# More code


# We are now ready to perform the simulation by looping through every time step:

# In[5]:


# Mode code


# Finally, we can plot the output signal, and save it as a wav file so we can hear it:

# In[6]:


# More code


# 
# ## Adding boundaries
# 
# Add some simple boundaries.
# 

# In[7]:


# And here is some more code


# ## Different types of source
# 
# Info

# In[8]:


# More code


# ## Summary
# 
# _Please include a few summary bullets describing the main take-aways from the tutorial._
# 
# * Bullet 1
# * Bullet 2
# * Bullet 3
