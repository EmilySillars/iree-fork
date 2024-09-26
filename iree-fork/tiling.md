# What kinds of tiling does iree support?

## Setup

As soon as you enter the top level directory,

```
source .venv/bin/activate
```

If you add any new source files, or modify a cmake file,

```
cmake -G Ninja -B ../iree-build/ -S . \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DIREE_ENABLE_ASSERTIONS=ON \
    -DIREE_ENABLE_SPLIT_DWARF=ON \
    -DIREE_ENABLE_THIN_ARCHIVES=ON \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DIREE_ENABLE_LLD=ON \
    -DIREE_BUILD_PYTHON_BINDINGS=ON  \
    -DPython3_EXECUTABLE="$(which python3)" \
    .
```

If you modify any source files,

```
cmake --build ../iree-build/
```

## Investigation

1. `../iree-build/tools/iree-opt --help | grep tile`

   a whole bunch of passes; too many to list! 

   Some notable passes:
   ```
           --iree-codegen-gpu-apply-tiling-level                                  -   Pass to tile tensor ops based on tiling configs
           --tiling-level=<value>                                               - Tiling level to tile. Supported levels are 'reduction' and 'thread'
         --iree-codegen-gpu-distribute-scf-for                                  -   Distribute tiled loop nests to invocations
         --iree-codegen-gpu-tensor-tile                                         -   Pass to tile tensor (linalg) ops within a GPU workgroup
         --iree-codegen-gpu-tensor-tile-to-serial-loops                         -   Pass to tile reduction dimensions for certain GPU ops
         --iree-codegen-gpu-tile                                                -   Tile Linalg ops with tensor semantics to invocations
         --iree-codegen-gpu-tile-reduction                                      -   Pass to tile linalg reduction dimensions.
           --logTile=<uint>                                                     - The log2 of the tile size used for swizzling. (0: disabled, non-0: swizzling enabled)
         --iree-codegen-tile-and-distribute-to-workgroups                       -   Tile and distribute operations to workgroups
         --iree-codegen-tile-and-distribute-to-workgroups-using-forall-op       -   Tile and distribute operation to workgroups (using scf.forall op)
     --iree-codegen-llvmgpu-enable-transform-dialect-aligned-matmul             - activate the matmul tensorcore strategy for tile aligned shapes
     --iree-codegen-llvmgpu-test-tile-and-fuse-matmul                           - test the the tile and fuse pipeline for matmul
     --iree-codegen-llvmgpu-test-tile-and-fuse-vectorize                        - test the tile and fuse pipeline for all supported operations
   
   ```

   

## Examples

