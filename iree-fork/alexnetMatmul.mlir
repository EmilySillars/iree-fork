func.func @alexnetMatmul(%collapsed: tensor<1x9216xf32>, %cast_652: tensor<9216x4096xf32>, %acc: tensor<?x?xf32>) -> tensor<?x?xf32> {
  %result = linalg.matmul 
  ins(%collapsed, %cast_652 : tensor<1x9216xf32>, tensor<9216x4096xf32>) 
  outs(%acc : tensor<?x?xf32>) 
  -> tensor<?x?xf32>
  return %result: tensor<?x?xf32>
}