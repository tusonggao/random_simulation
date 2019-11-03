import numpy as np
import random
import matplotlib.pyplot as plt


# 即便随机分配，贫富差距也注定会越来越大

values = [100] * 100
print(np.random.randint(0, 2, 10))

for loop_num in range(1, 500000+1):
    target = np.random.randint(0, 100, 100)
    for i in range(100):
        if values[i]>0:
            values[i] -= 1
            values[target[i]] += 1
    if loop_num%50000==0:
        print('loop_num is ', loop_num)
        plt.figure()
        plt.bar(range(len(values)), values, color='rgby')
        plt.title('loop number: {}'.format(loop_num))
        plt.show()


