import numpy as np, matplotlib.pyplot as plt
x = np.arange(0.001,1, step=0.001)
y = -np.log2(x)
# plt.scatter(x,y)
plt.plot(x,y)
plt.title("self-information")
plt.xlabel("P(x)")
plt.ylabel("I(x)")
# plt.show()
plt.savefig("_dl/self-information_log2.png")
