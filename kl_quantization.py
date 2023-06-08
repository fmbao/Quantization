'''
Author: ccbao 1689940525@qq.com
Date: 2023-06-08 09:41:14
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-06-08 09:57:54
FilePath: /Quantization/kl_quantization.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import matplotlib.pyplot as plt

def cal_kl(p,q):
    KL = 0.
    for i in range(len(p)):
        KL += p[i] * np.log(p[i]/q[i])
    return KL 

def cal_kl_test(x, kl_threshold=0.1):
    y_out = []
    while True:
        y = [np.random.uniform(1, size+1) for i in range(size)]
        y /= np.sum(y)
        kl_result = cal_kl(x, y)
        if kl_result < kl_threshold:
            print(kl_result)
            y_out = y
            plt.plot(x)
            plt.plot(y)
            break
    return y_out
if __name__ == '__main__':
    np.random.seed(1)
    size = 10
    x = [np.random.uniform(1, size + 1) for i in range(size)]
    x = x / np.sum(x)
    y_out = cal_kl_test(x, kl_threshold=0.03)
    plt.show()
    print(x, y_out)