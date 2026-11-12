import numpy as np
scores = np.array([88, 72, 55, 91, 63])
mask = scores >= 60          # array([ True, True, False, True, True])
passed = scores[mask]        # array([88, 72, 91, 63])
scores[scores < 60] = 0      # set every failing score to 0
print(mask)
print(passed)
print(scores)



# ------TASK01------------
a = np.array([10, 20, 30])
print("Shape: ", a.shape)
print("dtype: ", a.dtype)

# ------TASK02------------
data = [1, 2, 3, 4, 5]
b = np.array(data)
result = b * 10
print("Result:", result)


# -----------TASK03------------
import numpy as np 
vals = np.array([15, 42, 7, 88, 21]) 
mask = vals > 20 
filter = vals[mask] 
print("Filtered:", filter)

# ----------TASK04------------
c = np.random.randint(1, 101, 6)

print("Earlier:", c)

c[c < 50] = 0

print("Then:", c)


# -------TASK05-------------- 

d = np.array([10, 20, 30]) 
result = d / 2 
print("Result:", result) 
print("Dtype:", result.dtype)