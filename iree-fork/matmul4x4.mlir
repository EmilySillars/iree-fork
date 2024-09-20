func.func @matmul4x4(%lhs: tensor<4x4xi8>, %rhs: tensor<4x4xi8>, %acc: tensor<4x4xi32>) -> tensor<4x4xi32> {
  %result = linalg.matmul
    ins(%lhs, %rhs: tensor<4x4xi8>, tensor<4x4xi8>)
    outs(%acc: tensor<4x4xi32>)
  -> tensor<4x4xi32>
  return %result: tensor<4x4xi32>
}
