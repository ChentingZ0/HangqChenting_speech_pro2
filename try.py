import numpy as np

# Create a 2D array
a = np.array([[1, 2], [3, 4]])
print(a.shape,'a')
# Add a new dimension at position 0
b = np.expand_dims(a, axis=0)
print(b.shape,'b')  # Output: (1, 2, 2)

# Add a new dimension at position 1
c = np.expand_dims(a, axis=1)
print(c.shape,'c')  # Output: (2, 1, 2)


print(np.log([1, np.e, np.e**2, 0]),'ln')