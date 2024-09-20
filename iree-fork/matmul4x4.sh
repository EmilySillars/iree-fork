# run this script from the top level directory
# compile and run matmul4x4.mlir with iree

# compile
../iree-build/tools/iree-compile --iree-hal-target-backends=llvm-cpu iree-fork/matmul4x4.mlir -o iree-fork/out/matmul4x4.vmfb

# generate inputs
python iree-fork/gen-matmul4x4-inputs.py

# run
../iree-build/tools/iree-run-module \
    --device=local-task \
    --module=iree-fork/out/matmul4x4.vmfb \
    --function=matmul4x4 \
    --input=@iree-fork/out/matmul4x4-a.npy \
    --input=@iree-fork/out/matmul4x4-b.npy \
    --input=@iree-fork/out/matmul4x4-c.npy > iree-fork/out/matmul4x4.out