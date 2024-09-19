// func.func @simple_matmul(%arg0: memref<104x104xi8>, %arg1: memref<104x104xi8>, %arg2: memref<104x104xi32>) {
// linalg.matmul ins(%arg0, %arg1 : memref<104x104xi8>, memref<104x104xi8>) outs(%arg2 : memref<104x104xi32>)
// return
// }

// #map = affine_map<(d0, d1, d2) -> (d0, d2)>
// #map1 = affine_map<(d0, d1, d2) -> (d2, d1)>
// #map2 = affine_map<(d0, d1, d2) -> (d0, d1)>
// "builtin.module"() ({
//   "func.func"() ({
//   ^bb0(%arg0: tensor<104x104xi8>, %arg1: tensor<104x104xi8>, %arg2: tensor<104x104xi32>):
//     "linalg.matmul"(%arg0, %arg1, %arg2) ({
//     ^bb0(%arg3: i8, %arg4: i8, %arg5: i32):
//       %0 = "arith.extsi"(%arg3) : (i8) -> i32
//       %1 = "arith.extsi"(%arg4) : (i8) -> i32
//       %2 = "arith.muli"(%0, %1) : (i32, i32) -> i32
//       %3 = "arith.addi"(%arg5, %2) : (i32, i32) -> i32
//       "linalg.yield"(%3) : (i32) -> ()
//     }) {linalg.memoized_indexing_maps = [#map, #map1, #map2], operand_segment_sizes = array<i32: 2, 1>} : (tensor<104x104xi8>, tensor<104x104xi8>, tensor<104x104xi32>) -> ()
//     "func.return"() : () -> ()
//   }) {function_type = (tensor<104x104xi8>, tensor<104x104xi8>, tensor<104x104xi32>) -> (), sym_name = "simple_matmul"} : () -> ()
// }) : () -> ()

// func.func @simple_mul(%arg0: tensor<4xf32>, %arg1: tensor<4xf32>) -> tensor<4xf32> {
//   %0 = "arith.mulf"(%arg0, %arg1) : (tensor<4xf32>, tensor<4xf32>) -> tensor<4xf32>
//   return %0 : tensor<4xf32>
// }

// func.func @simple_matmul(%arg0: tensor<104x104xi8>, %arg1: tensor<104x104xi8>, %arg2: tensor<104x104xi32>{
// linalg.matmul ins(%arg0, %arg1, %arg2 : tensor<104x104xi8>, tensor<104x104xi8>, tensor<104x104xi32>)
// }

// func.func @simple_matmul(%arg0: tensor<104x104xi8>, %arg1: tensor<104x104xi8>, %arg2: tensor<104x104xi32>) -> tensor<104x104xi32>{
// linalg.matmul ins(%arg0, %arg1: tensor<104x104xi8>, tensor<104x104xi8>) outs(%arg2: tensor<104x104xi32>)
// }

// func.func @simple_matmul(%arg0: tensor<104x104xi8>, %arg1: tensor<104x104xi8>, %arg2: tensor<104x104xi32>){
// linalg.matmul ins(%arg0, %arg1, %arg2 : tensor<104x104xi8>, tensor<104x104xi8>, tensor<104x104xi32>)
// }