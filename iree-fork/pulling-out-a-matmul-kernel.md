# Pulling out a matmul kernel from Alexnet
1. First I generated linalg

```h 
sh iree-fork/alexnet-to-linalg.sh
```

2. Then I searched for the matmul operation using `grep`

```
cat iree-fork/out/alexnet-hopefully-linalg.mlir | grep matmul -n
```

and found

```
1084:    %147 = linalg.matmul ins(%collapsed, %cast_652 : tensor<1x9216xf32>, tensor<9216x4096xf32>) outs(%146 : tensor<?x?xf32>) -> tensor<?x?xf32>
1163:    %163 = linalg.matmul ins(%cast_681, %cast_690 : tensor<1x4096xf32>, tensor<4096x4096xf32>) outs(%162 : tensor<?x?xf32>) -> tensor<?x?xf32>
1241:    %179 = linalg.matmul ins(%cast_720, %cast_727 : tensor<1x4096xf32>, tensor<4096x1000xf32>) outs(%178 : tensor<?x?xf32>) -> tensor<?x?xf32>
```

3. To isolate the first matmul at line 1084, printed out part of the file (starting at line 1060) using `more`

```
more iree-fork/out/alexnet-hopefully-linalg.mlir +1060
```

and found

```
%c6_645 = arith.constant 6 : index
    %c1_i64_646 = arith.constant 1 : i64
    %c9216_i64 = arith.constant 9216 : i64
    %collapsed = tensor.collapse_shape %cast_636 [[0], [1, 2, 3]] : tensor<1x256x6x6xf32> into tensor<1x9216xf32>
    %none_647 = torch.constant.none
    %__auto.constant_4096_9216_torch.float32 = util.global.load @__auto.constant_4096_9216_torch.float32 : tensor<4096x9216xf32>
    %142 = torch_c.from_builtin_tensor %__auto.constant_4096_9216_torch.float32 : tensor<4096x9216xf32> -> !torch.vtensor<[4096,9216],f32>
    %143 = torch_c.to_builtin_tensor %142 : !torch.vtensor<[4096,9216],f32> -> tensor<4096x9216xf32>
    %int0_648 = torch.constant.int 0
    %int1_649 = torch.constant.int 1
    %c0_650 = arith.constant 0 : index
    %c4096 = arith.constant 4096 : index
    %c1_651 = arith.constant 1 : index
    %c9216 = arith.constant 9216 : index
    %144 = tensor.empty() : tensor<9216x4096xf32>
    %transposed = linalg.transpose ins(%143 : tensor<4096x9216xf32>) outs(%144 : tensor<9216x4096xf32>) permutation = [1, 0] 
    %cast_652 = tensor.cast %transposed : tensor<9216x4096xf32> to tensor<9216x4096xf32>
    %c0_653 = arith.constant 0 : index
    %dim = tensor.dim %collapsed, %c0_653 : tensor<1x9216xf32>
    %c1_654 = arith.constant 1 : index
    %dim_655 = tensor.dim %cast_652, %c1_654 : tensor<9216x4096xf32>
    %145 = tensor.empty(%dim, %dim_655) : tensor<?x?xf32>
    %cst_656 = arith.constant 0.000000e+00 : f32
    %146 = linalg.fill ins(%cst_656 : f32) outs(%145 : tensor<?x?xf32>) -> tensor<?x?xf32>
    %147 = linalg.matmul ins(%collapsed, %cast_652 : tensor<1x9216xf32>, tensor<9216x4096xf32>) outs(%146 : tensor<?x?xf32>) -> tensor<?x?xf32>
    %cast_657 = tensor.cast %147 : tensor<?x?xf32> to tensor<1x4096xf32>
```

4. The meat of the operation is the following

```
...
%collapsed = tensor.collapse_shape %cast_636 [[0], [1, 2, 3]] : tensor<1x256x6x6xf32> into tensor<1x9216xf32>
...
%cast_652 = tensor.cast %transposed : tensor<9216x4096xf32> to tensor<9216x4096xf32>
...
%cst_656 = arith.constant 0.000000e+00 : f32
%146 = linalg.fill ins(%cst_656 : f32) outs(%145 : tensor<?x?xf32>) -> tensor<?x?xf32>
...
%147 = linalg.matmul ins(%collapsed, %cast_652 : tensor<1x9216xf32>, tensor<9216x4096xf32>) outs(%146 : tensor<?x?xf32>) -> tensor<?x?xf32>
```

5. Can I turn this into a little function that I can compile/tile with iree? I think so! I propose that it would look like...

```
func.func @alexnet-matmul(%collapsed: tensor<1x9216xf32>, %cast_652: tensor<9216x4096xf32>, %acc: tensor<?x?xf32>) -> tensor<?x?xf32> {
  %result = linalg.matmul 
  ins(%collapsed, %cast_652 : tensor<1x9216xf32>, tensor<9216x4096xf32>) 
  outs(%acc : tensor<?x?xf32>) 
  -> tensor<?x?xf32>
  return %result: tensor<?x?xf32>
}
```

