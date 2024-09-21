# run this script from the top level directory
# compile and run $1.mlir with iree

echo "Compiling $1.mlir..."

# compile
../iree-build/tools/iree-compile --iree-hal-target-backends=llvm-cpu iree-fork/$1.mlir -o iree-fork/out/$1.vmfb

echo "Done."
# # generate inputs
# python iree-fork/gen-matmul104x104-inputs.py

# # run
# ../iree-build/tools/iree-run-module \
#     --device=local-task \
#     --module=iree-fork/out/matmul104x104.vmfb \
#     --function=matmul104x104 \
#     --input=@iree-fork/out/matmul104x104-a.npy \
#     --input=@iree-fork/out/matmul104x104-b.npy \
#     --input=@iree-fork/out/matmul104x104-c.npy > iree-fork/out/matmul104x104.out