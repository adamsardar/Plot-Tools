#! /usr/local/bin/sage --python
#Using the sage implementation of python for nice easy access to scilab and matlibplot

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2, 1000)

plt.figure()
plt.plot(x, np.sqrt(x), label = "Skiing: $\sqrt{x}$")
plt.plot(x, x**2, label = "Snowboarding: $x^2$")
plt.title("Learning Curves for Snowboarding and Skiing")
plt.xlabel("Time") ; plt.ylabel("Skill")
plt.legend(loc='upper left')
plt.savefig("./Skiing.png")
