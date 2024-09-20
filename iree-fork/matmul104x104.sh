# run this script from the top level directory
# compile and run matmul104x104.mlir with iree

# compile
../iree-build/tools/iree-compile --iree-hal-target-backends=llvm-cpu iree-fork/matmul104x104.mlir -o iree-fork/out/matmul104x104.vmfb

# generate inputs
python iree-fork/gen-matmul104x104-inputs.py

# run
../iree-build/tools/iree-run-module \
    --device=local-task \
    --module=iree-fork/out/matmul104x104.vmfb \
    --function=matmul104x104 \
    --input=@iree-fork/out/matmul104x104-a.npy \
    --input=@iree-fork/out/matmul104x104-b.npy \
    --input=@iree-fork/out/matmul104x104-c.npy > iree-fork/out/matmul104x104.out