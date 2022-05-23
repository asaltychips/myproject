import numpy as np 

print('\nZERO ARRAY\n')
zeroarray = np.zeros((3,3,3))

print('zeros array size: ', np.size(zeroarray))
print('zeros array shape: ', np.shape(zeroarray), '\n')
print(zeroarray)

zeroarray.resize((1,27))
print('\nZero array size: ', np.size(zeroarray))
print('zero array shape: ', np.shape(zeroarray))
print(zeroarray)
