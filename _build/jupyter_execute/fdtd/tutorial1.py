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
# _The aim with all our tutorials is to introduce a basic working example as early as possible, so that new users can see the value right away. You can then introduce more details as you go on. See the [FDTD tutorial](../fdtd/tutorial1) for an example._

# In[2]:


# Simple example code


# ## More details
# 
# _Once you have introduced the basic example, you can begin to build upon it howevery you like. Try not to make these sections too long._
# 
# Here's some more details and code relating to a specific aspect.
# 

# In[3]:


# And here is some more code


# ## Embedding code, images, math...
# 
# There's lots of information about how to embed code, images, etc. into Jupyter Notebooks in the [Jupyter Books documentation](https://jupyterbook.org/file-types/notebooks.html). MyST markdown is used in both the `.md` and `.ipynb` files throughout the Jupyter Book. For more information about MyST markdown, check out [the MyST guide in Jupyter Book](https://jupyterbook.org/content/myst.html), or see [the MyST markdown documentation](https://myst-parser.readthedocs.io/en/latest/).
# 
# The most common things you might want to do are embed images, like so:
# 
# ![](https://myst-parser.readthedocs.io/en/latest/_static/logo-wide.svg)
# 
# Or $add_{math}$ and
# 
# $$
# math^{blocks}
# $$
# 
# using LaTeX formatting, like so...
# 
# $$
# \begin{aligned}
# \mbox{mean} la_{tex} \\ \\
# math blocks
# \end{aligned}
# $$
# 
# ## Summary
# 
# _Please include a few summary bullets describing the main take-aways from the tutorial._
# 
# * Bullet 1
# * Bullet 2
# * Bullet 3
