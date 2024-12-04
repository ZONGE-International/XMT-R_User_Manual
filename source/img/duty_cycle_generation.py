import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True

# t = np.linspace(0,31,32)
# ON =  [1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0]
# POL = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
# TX =  [0,0,0,0,1,1,1,1,0,0,0,0,-1,-1,-1,-1,0,0,0,0,1,1,1,1,0,0,0,0,-1,-1,-1,-1]
t =   [0,1,2,3,4,5,6,7]
ON =  [1,1,0,1,0,1,0,1,]
POL = [0,0,1,1,0,0,1,1]
TX =  [0,0,1,0,-1,0,1,0]

fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(8, 4), tight_layout=True)
ax1.step(t,ON, c='red')
ax2.step(t,POL, c='green')
ax3.step(t,TX, c = 'black')

ax1.set_ylabel(r'$\overline{ON}$')
ax2.set_ylabel('POL')
ax3.set_ylabel('TX')
ax3.set_xlabel('Time')

#fig.suptitle('Subplots with shared axis')
plt.show()
