import numpy as np
import kangaroo as kanga

def whoAmI():
    kanga = "Wallaby"
    print(f"{kanga}\n")

def compare104x104(a, b):
    for i in range(104):
        for j in range(104):
            if a[i][j] != b[i][j]:
                return False
    return True

def printCompare104x104(a,b,a_name, b_name):
    if compare104x104(a,b):
        print(f"{a_name} = {b_name}.")
    else:
        print(f"{a_name} != {b_name} D:")

def main():
    whoAmI()
    kanga.whoAmI()
    # a = np.asarray(kanga.a_list).reshape(16,16)
    # b = np.asarray(kanga.b_list).reshape(16,16)
    # print("np.linalg.matmul(a,b.transpose()):")
    # print(np.matmul(a,b.transpose()))
    # print("np.linalg.matmul(a,b):")
    # print(np.matmul(a,b))
    a = np.asarray(kanga.matA).reshape(104,104)
    b = np.asarray(kanga.matB).reshape(104,104)
    simple_matmul_no_strides = np.asarray(kanga.simple_matmul_no_strides).reshape(104,104)
    simple_matmul = np.asarray(kanga.simple_matmul).reshape(104,104)
    regular_matmul = np.asarray(kanga.regular_matmul).reshape(104,104)
    c_matmul = np.asarray(kanga.c_matmul).reshape(104,104)
    myC = np.matmul(a,b)
    myQ = np.matmul(a,b.transpose())
    printCompare104x104(a, a, "a", "a")
    printCompare104x104(a, b, "a", "b")
    printCompare104x104(simple_matmul, simple_matmul_no_strides, "simple_matmul", "simple_matmul_no_strides")
    printCompare104x104(myC, simple_matmul, "myC", "simple_matmul")
    printCompare104x104(myC, simple_matmul_no_strides, "myC", "simple_matmul_no_strides")
    printCompare104x104(myC, regular_matmul, "myC", "regular_matmul")
    printCompare104x104(myC, c_matmul, "myC", "c_matmul")
    # if compare104x104(a,a):
    #     print("a = a.")
    # if compare104x104(b,b):
    #     print("b = b.")
    # if compare104x104(simple_matmul,simple_matmul_no_strides):
    #     print("simple_matmul = simple_matmul_no_strides.")
    # else:
    #     print("simple_matmul != simple_matmul_no_strides D:")
    # if compare104x104(myC, simple_matmul):
    #     print("myC = simple_matmul.")
    # else:
    #     print("myC != simple_matmul D:")
    # if compare104x104(myC, simple_matmul_no_strides):
    #     print("myC = simple_matmul_no_strides.")
    # else:
    #     print("myC != simple_matmul_no_strides D:")
    # if compare104x104(myQ, simple_matmul):
    #     print("myQ = simple_matmul.")
    # else:
    #     print("myQ != simple_matmul D:")
     

if __name__ == "__main__":
    main()