# --------MODULE 2: NUMPY-------------

# *****Broadcasting and Vectorised Thinking*****

# --------------------TASK01----------------
import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

result = arr + 10

print(result)



# -----------------------TASK02----------------------
import numpy as np

table = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
])

row_vector = np.array([10, 20, 30])

result = table + row_vector

print(result)



# ----------------TASK03----------------

import numpy as np

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

B = np.array([1, 2, 3])

# Attempt that causes a shape mismatch
try:
    result = A + B
    print(result)
except ValueError as e:
    print("Error:", e)

# Fix by reshaping B from (3,) to (3,1)
B_fixed = B.reshape(3, 1)

result = A + B_fixed

print("After reshaping:")
print(result)


# ------------TASK04-----------
import numpy as np

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

B = np.array([
    [2],
    [3],
    [4]
])

result = A * B

print(result)



# ---------------TASK05------------------------
import numpy as np

np.random.seed(42)

data = np.random.uniform(1, 100, size=(10, 3))

standardised = (data - data.mean(axis=0)) / data.std(axis=0)

print("Original data:")
print(data)

print("\nStandardised data:")
print(standardised)


# *******Fancy Indexing, Masks and Reshaping*******

# -----------------TASK01----------------
import numpy as np

data = np.array([10, 20, 30, 40, 50])

result = data[[4, 0, 4]]

print(result)

# -----------------TASK02----------------
import numpy as np

data = np.array([15, 25, 35, 45, 55])

result = data[(data > 40) | (data < 20)]

print(result)


# ---------------TASK03----------------
import numpy as np

x = np.arange(12)

result = x.reshape(3, -1)

print(result)
print("Shape:", result.shape)


# ------------TASK04----------------
import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

horizontal = np.hstack([a, b])
vertical = np.vstack([a, b])

print("Horizontal:")
print(horizontal)

print("Vertical:")
print(vertical)



# --------------TASK05----------------
import numpy as np

data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

flattened = data.flatten()

column = flattened.reshape(-1, 1)

print("Flattened:")
print(flattened)

print("\nFinal column:")
print(column)

print("\nFinal shape:", column.shape)



# ******Mathematical and Linear Algebra Operations******  

# -------------TASK01----------------

import numpy as np

x = np.array([1, 2, 3, 4, 5])

log_result = np.log(x)
sqrt_result = np.sqrt(x)

print("Log:", log_result)
print("Square Root:", sqrt_result)

# ------------TASK02----------------

import numpy as np

probabilities = np.array([0.1, 0.7, 0.2])

predicted_class = probabilities.argmax()

print("Predicted class index:", predicted_class)


# -----------------------TASK03----------------
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

element_wise = a * b
dot_product = a @ b

print("Element-wise multiplication:", element_wise)
print("Dot product:", dot_product)


# -----------------TASK04----------------
import numpy as np

X = np.array([
    [2, 3],
    [4, 5],
    [6, 7]
])

w = np.array([10, 2])

predictions = X @ w

print("Predictions:", predictions)


# --------------------TASK05----------------
import numpy as np

values = np.array([10, 20, 30])
weights = np.array([0.2, 0.5, 0.3])

method1 = (values * weights).sum()

print("Method 1:", method1)