from math import sqrt, hypot
import numpy as np


for i in 1,2,3,4,5:
    print("wait for", i, '*'*i)
    time.sleep(1)
fig = plt.figure()
x = np.linspace(0,10,500)
for i in 1,2,3:
    y = 0.2*np.cumsum(np.random.randn(500))
    plt.plot(x, y+5*i)
    plt.fill_between(x, y+5*i-0.1*y-1, y+5*i+0.1*y+1, alpha=0.2)
plt.show()

# The next figure can be shown while the first is visible

fig = plt.figure()
n, (r0, r1) = 100, np.random.rand(2)
for i in range(n):
    t = np.linspace(i,(i+1),250)
    x = (1 - 0.9*t/n) * np.cos(1.5*2*np.pi*(t+r0))
    y = (1 - 0.9*t/n) * (np.sin(3.008*2*np.pi*t) + np.sin(1.5*np.pi*(t+r1)))
    plt.plot(x, y, color=plt.cm.plasma(float(i)/n), alpha=0.9, lw=0.8)
plt.show()