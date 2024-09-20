# filling the matrices according to the values in set in the main.c program here:
# https://github.com/EmilySillars/Quidditch-zigzag/blob/9d3c8263a8a1b3cd07b5802e03d680fc563e3677/runtime/tests/tiledMatmul13/main.c#L113-L127
# This main.c program comes from this example: https://github.com/EmilySillars/Quidditch-zigzag/tree/tiling/runtime/tests/tiledMatmul13#matrix-multiplication-13

#   for (size_t i = 0; i < MAT_WIDTH_SQUARED; i++) {
#     memrefA.aligned_data[i] = (int8_t)2;
#   }
#   memrefA.aligned_data[0] = 78;

#   for (size_t i = 0; i < MAT_WIDTH_SQUARED; i++) {
#     memrefB.aligned_data[i] = (int8_t)3;
#   }
#   memrefB.aligned_data[5] = 88;
#   memrefB.aligned_data[200] = 96;


#   for (size_t i = 0; i < MAT_WIDTH_SQUARED; i++) {
#     memrefC.aligned_data[i] = (int32_t)0;
#   }
import numpy as np

MAT_WIDTH = 104
MAT_WIDTH_SQUARED = MAT_WIDTH * MAT_WIDTH

# intialize A input matrix
flatA = [2] * MAT_WIDTH_SQUARED
flatA[0] = 78
a = np.asarray(flatA, np.int8).reshape(MAT_WIDTH,MAT_WIDTH)

# intialize B input matrix
flatB = [3] * MAT_WIDTH_SQUARED
flatB[5] = 88
flatB[200] = 96
b = np.asarray(flatB, np.int8).reshape(MAT_WIDTH,MAT_WIDTH)

# intialize C output matrix
flatC = [0] * MAT_WIDTH_SQUARED
c = np.asarray(flatC, np.int32).reshape(MAT_WIDTH,MAT_WIDTH)

# initialize correct result
golden = np.matmul(a,b, dtype=np.int32)

fileA = "./iree-fork/out/matmul104x104-a.npy"
fileB = "./iree-fork/out/matmul104x104-b.npy"
fileC = "./iree-fork/out/matmul104x104-c.npy"
np.save(fileA, a)
np.save(fileB, b)
np.save(fileC, c)
f = open('./iree-fork/out/matmul104x104-golden.txt', 'w')
f.write(np.array2string(golden))
f.close()