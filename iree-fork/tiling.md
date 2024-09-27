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

2. `../iree-build/tools/iree-opt --help | grep tiling`

   ```
         --iree-codegen-affinemin-scf-canonicalization                          -   Pass to run pass cleaning up affineMinOp after tiling and distribute.
           --tile-outer-to-one                                                  - Always apply tiling to make outer dimension be ones
           --enable-cleanup                                                     - Enable cleanups after vectorization. The patterns touch the structuregenerated from tiling so it affects later steps like bufferization and vector hoisting.
         --iree-codegen-gpu-apply-tiling-level                                  -   Pass to tile tensor ops based on tiling configs
           --tiling-level=<value>                                               - Tiling level to tile. Supported levels are 'reduction' and 'thread'
           --tiling-level=<long>                                                - Use default tiling level used to retrieve the configuration from lowering_config
           --tiling-level=<long>                                                - Use default tiling level used to retrieve the configuration from lowering_config
           --tiling-level=<long>                                                - Use default tiling level used to retrieve the configuration from lowering_config
           --tiling-factor=<int>                                                - Tiling factor for the channel dimension of NCHW-like convolutions. Defaults to fully transposing all channel-like dimensions
           --skip-thread                                                        - Skip tiling and distributing to GPU threads
         --scf-parallel-loop-tiling                                             -   Tile parallel loops
           --no-min-max-bounds                                                  - Perform tiling with fixed upper bound with inbound check inside the internal loops
     --iree-dispatch-creation-experimental-data-tiling                          - Enable data-tiling at flow level, i.e., it sets encodings in dispatch regions, hoist them out of region, and enables fusion for the set_encodings. This is still an experimental path. The current main data tiling path is iree-opt-data-tiling, which is on by default. To use this path, --iree-opt-data-tiling=false must be set as wells
     --iree-dispatch-creation-pad-factor=<int>                                  - Provides padding size hints that will be attached to encodings. This only affects the experimental data tiling path in Flow with iree-dispatch-creation-experimental-data-tiling.
     --iree-llvmcpu-disable-arm-sme-tiling                                      - Disables tiling for SME even if it is supported by the target (i.e., when the +sme feature flag is present)
   
   ```


## Examples



## Compile for riscv??

```
--iree-llvmcpu-list-targets                                                - Lists all registered targets that the LLVM backend can generate code for.
  --iree-llvmcpu-target-abi=<string>                                         - LLVM target machine ABI; specify for -mabi
  --iree-llvmcpu-target-cpu=<string>                                         - LLVM target machine CPU; use 'host' for your host native CPU.
  --iree-llvmcpu-target-cpu-features=<string>                                - LLVM target machine CPU features; use 'host' for your host native CPU.
  --iree-llvmcpu-target-data-layout=<string>                                 - LLVM target machine data layout override.
  --iree-llvmcpu-target-float-abi=<value>                                    - LLVM target codegen enables soft float abi e.g -mfloat-abi=softfp
  --iree-llvmcpu-target-triple=<string>                                      - LLVM target machine triple.
  --iree-llvmcpu-target-vector-width-in-bytes=<uint>                         - Overrides the native vector register width (in bytes) of the target.
  --iree-llvmcpu-wasm-linker-path=<string>                                   - Tool used to link WebAssembly modules produced by IREE (for --iree-llvmcpu-target-triple=wasm32-*).

```

hoodle

```
# compile llvm to .o file (target riscv)
echo "START: clang (llvm to .o)"
clang \
-Wno-unused-command-line-argument \
-D__DEFINED_uint64_t \
--target=riscv32-unknown-elf \
-mcpu=generic-rv32 \
-march=rv32imafdzfh \
-mabi=ilp32d \
-mcmodel=medany \
-ftls-model=local-exec \
-ffast-math \
-fno-builtin-printf \
-fno-common \
-O3 \
-std=gnu11 \
-Wall \
-Wextra \
-x ir \
-c $basename/out/$basename-w-memrefCopy.ll \
-o $basename/out/$basename.o
echo "FINISHED: clang (llvm to .o)"
```

