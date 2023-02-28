# import numpy as np
#
# # Create a 2D array
# a = np.array([[1, 2], [3, 4]])
# print(a.shape,'a')
# # Add a new dimension at position 0
# b = np.expand_dims(a, axis=0)
# print(b.shape,'b')  # Output: (1, 2, 2)
#
# # Add a new dimension at position 1
# c = np.expand_dims(a, axis=1)
# print(c.shape,'c')  # Output: (2, 1, 2)
#
#
# print(np.log([1, np.e, np.e**2, 0]),'ln')
#
# r3 = np.arange(0, 11.51, 0.01)
# r = np.arange(0,5,1)
# print(r3)
#
#
# # idx = [sq_enc(x, r, x_max_list[i],m) for i in x_max_list]
# # out1 = [sq_dec(idx[i])]
# #
#
# x = [1,5,7,9]
# def times(x):
#     y = 2*x
#     return y
# list = []
#
#
# list1 = [times(x[i]) for i in range(0,len(x))]
# print(list1)
#
# list2 = [times(i) for i in x]
# print(list2)
#
# print(np.array([3,4,5,6,7])-np.array([1,2,3,4,5]))
#
#
# outq_array = np.array([[1,2,3],[3,4,5]])
# print(outq_array.shape)
# print(outq_array[1,:])
# print(outq_array[1,:].shape)




from scipy import signal

# Generate an input signal
signal = [1, 2, 3, 2, 1, -1, -2, -1, 0, 1]

# Calculate LPC coefficients
order = 4  # order of the LPC filter
lpc_coeff = signal.lpc(signal, order)
print(lpc_coeff)

# Filter the signal using the LPC coefficients
filtered_signal = signal.lfilter([0] + -1 * lpc_coeff[1:], [1], signal)

# Calculate the residual signal
residual_signal = signal - filtered_signal

print(residual_signal)