import matplotlib.pyplot as plt
import numpy as np
import math


background = 0.6728 # No.14
all = 1.11 # No.13
array = [
    0.8197,
    1.082,
    0.8201,
    0.7185,
    0.8804,
    0.7891,
    1.025,
    1.041,
    0.7237,
    0.8094,
    0.6702,
    0.6609
    ] # 1~12
na = np.array(array)

na = (na - background)/(all - background)*100

plt.xlabel('Tube number')
plt.ylabel('Percentages of Histamine')
plt.title('Histamine fluorescence')
plt.grid()

plt.bar(x=np.array([i+1 for i in range(len(array))]),height=na)
plt.savefig('bars.png')
