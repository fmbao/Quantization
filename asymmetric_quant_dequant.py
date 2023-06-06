'''
Author: ccbao 1689940525@qq.com
Date: 2023-06-02 16:49:39
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-06-06 20:52:03
FilePath: /Quantization/quant_dequant.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np


def saturate(x,int_max=None, int_min=None):
    return np.clip(x,-127,127)

def scale_cal(x, int_max=None, int_min=None):
    max_val = np.max(np.abs(x))
    return max_val / 127 

def dequant_data(xq,scale=None):
    x = (xq  * scale).astype('float32')
    return x


def quant_float_data(x,scale=None, int_min=None,int_max=None):
    xq = np.round(x /scale)     
    return saturate(xq)


if __name__ == '__main__':
    np.random.seed(1)
    data_float32 = np.random.rand(3).astype('float32')
    print("data_float32: ",data_float32)
    int_max = 127
    int_min = -128
    
    scale = scale_cal(data_float32,int_max=int_max,int_min=int_min)
    print("scale : ",scale)

    data_int8 = quant_float_data(data_float32, scale=scale,int_min=int_min,int_max=int_max)
    print("data_int8: ",data_int8)
    
    data_dequant_float32 = dequant_data(data_int8, scale=scale)
    print("dequant_data_float32: ",data_dequant_float32)

    print("diff: ",data_float32 - data_dequant_float32)
