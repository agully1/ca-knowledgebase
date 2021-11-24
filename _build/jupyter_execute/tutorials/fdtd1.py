#!/usr/bin/env python
# coding: utf-8

# # FDTD Tutorial 1: Simple 2D plate
# 
# ```{warning}
# This section is currently under development. Content may not be complete, links may be broken, etc.
# ```
# 
# :::{note}
# You can run this code directly in your browser by clicking on the rocket logo at the top of the page, and clicking 'Binder'. This will open a Jupyter Notebook in a [Binder](https://mybinder.org/) environment which is set up to contain everything you need to run the code. **Don't forget to save a local copy if you make any changes!**
# 
# If you are new to using Jupyter Notebooks, [this guide](https://www.dataquest.io/blog/jupyter-notebook-tutorial/) will help you get started.
# :::
# 
# ## Prerequisites
# 
# None.
# 
# ## Introduction
# 
# In this tutorial, we will use a simple [explicit](../reference/glossary) finite difference time domain (FDTD) scheme to simulate wave propagation in two dimensions.
# 
# The FDTD scheme breaks a domain down into equally-sized cells. For our simple 2D scheme, we will use square cells. Let us imagine our domain is also square, and 1m x 1m in size. We will discuss how to decide the size of the cells later in this tutorial. For now, all we need to know is that we will split our domain up into multiple cells:
# 
# -- image of domain --
# 
# In this example, we will use FDTD to provide an approximate solution to the scalar wave equation:
# 
# -- equation --
# 
# A finite difference approximation to this equation can be described as follows (see the theory section for how we got here):
# 
# -- fd equation --
# 
# Our aim is to approximate the evolution of the pressure and velocity fields in our domain over some specified duration. As this is a time-domain simulation, we consider the problem one time sample at a time. We will therefore start from some initial state, and follow the relation above to update the pressure and velocity values for each cell at the next time sample, on the basis of their exisiting values.
# 
# One important thing to know about the basic FDTD scheme is that the pressure and velocity fields are _staggered_, with velocity values exisiting at a location halfway between pressure values. Despite this, it is conventional to refer to the velocity components with the same spatial indeces as the pressure values. See the image below for an explanation.
# 
# -- image of a cell ---
# 
# Our simulation, therefore, will start at time sample 0 with the pressure field P at t=0. The values in this pressure field will comprise our initial condition. From here, the velocity components in both dimensions are calculated. We then proceed to the next time step and update the pressure field, then the velocity fields, and so on for every time sample in the simulation. 
# 
# We obtain the output of the simulation by selecting a receiver location (a single point on the mesh) and saving the pressure value at that mesh location every time sample. 
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
# The first thing we will do is set up a 2D domain for simulation. We will provide the domain size, as well as the material properties (density and bulk modulus) - in this case, we'll use properties for air. This is a [homogeneous](../reference/glossary) domain: the material properties are the same throughout.
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
