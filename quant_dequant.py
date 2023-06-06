'''
Author: ccbao 1689940525@qq.com
Date: 2023-06-02 16:49:39
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-06-06 17:06:11
FilePath: /Quantization/quant_dequant.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np


def saturate(x,int_max=None, int_min=None):
    return np.clip(x,int_min,int_max)

def scale_z_cal(x, int_max=None, int_min=None):
    scale =  (x.max() - x.min()) / (int_max - int_min)
    z = int_max - np.round((x.max() / scale))
    return scale ,z

def dequant_data(xq,scale=None, z=None):
    x = ((xq - z) * scale).astype('float')
    return x


def quant_float_data(x,scale=None,z=None, int_min=None,int_max=None):
    xq = saturate(np.round(x /scale + z),int_min=int_min,int_max=int_max)
    return xq
if __name__ == '__main__':
    np.random.seed(1)
    data_float32 = np.random.rand(3).astype('float32')
    print("data_float32: ",data_float32)
    int_max = 127
    int_min = -128
    
    scale, z = scale_z_cal(data_float32,int_max=int_max,int_min=int_min)
    print("scale, z: ",scale,z)

    data_int8 = quant_float_data(data_float32, scale=scale,z = z,int_min=int_min,int_max=int_max)
    print("data_int8: ",data_int8)
    
    data_dequant_float32 = dequant_data(data_int8, scale=scale,z=z)
    print("dequant_data_float32: ",data_dequant_float32)

    print("diff: ",data_float32 - data_dequant_float32)
