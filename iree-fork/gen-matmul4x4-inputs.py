import numpy as np

MAT_WIDTH = 4
MAT_WIDTH_SQUARED = MAT_WIDTH * MAT_WIDTH

# intialize A input matrix
flatA = [2] * MAT_WIDTH_SQUARED
# flatA[0] = 78
a = np.asarray(flatA, np.int8).reshape(MAT_WIDTH,MAT_WIDTH)

# intialize B input matrix
flatB = [1] * MAT_WIDTH_SQUARED
# flatB[5] = 88
b = np.asarray(flatB, np.int8).reshape(MAT_WIDTH,MAT_WIDTH)

# intialize C output matrix
flatC = [0] * MAT_WIDTH_SQUARED
c = np.asarray(flatC, np.int32).reshape(MAT_WIDTH,MAT_WIDTH)

# initialize correct result
golden = np.matmul(a,b, dtype=np.int32)

fileA = "./iree-fork/out/matmul4x4-a.npy"
fileB = "./iree-fork/out/matmul4x4-b.npy"
fileC = "./iree-fork/out/matmul4x4-c.npy"
np.save(fileA, a)
np.save(fileB, b)
np.save(fileC, c)
f = open('./iree-fork/out/matmul4x4-golden.txt', 'w')
f.write(np.array2string(golden))
f.close()
print(a)
print(b)
print(c)
print(golden)