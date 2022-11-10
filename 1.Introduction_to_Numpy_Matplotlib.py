
# Write code to import libraries

import matplotlib.pyplot as plt
import numpy as np

"""Next step is to declare functions you are going to plot"""

# declare functions
def func1(x):
  return x**3
def func2(x):
  return 4*x**2+3*x+2

"""Generate a range of x values which will be used in the plots"""

# Generate range
a=np.arange(-10,+10,0.02)
b=np.arange(-5,+5,0.5)

"""Execute plot commands"""

# execute plot commands
#plotting func1(x)
plt.plot(a,func1(a),'k-')
plt.suptitle("y=f(x)")
plt.show()
#plotting sin(x)
plt.plot(b,np.sin(b),'o',color="green")
plt.suptitle("y=sin(x)")
plt.show()

#plotting func2(x)
plt.plot(a,func2(a),'k-',color="red")
plt.suptitle("y=func2(x)")
plt.show()