# run this script from the top level directory
# compile and run vector-mul.mlir with iree

# compile
../iree-build/tools/iree-compile --iree-hal-target-backends=llvm-cpu iree-fork/vector-mul.mlir -o iree-fork/out/vector-mul.vmfb

# run
../iree-build/tools/iree-run-module \
    --device=local-task \
    --module=iree-fork/out/vector-mul.vmfb \
    --function=vector_mul \
    --input="4xf32=[1, 2, 3, 4]" \
    --input="4xf32=[1, 87, 1, 1]" > iree-fork/out/vector-mul.out