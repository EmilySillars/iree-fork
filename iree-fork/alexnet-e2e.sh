# run this script from the top level directory
# convert alexnet (pytorch model) to mlir using iree-turbine, 
# then compile with iree and run.

# convert alexnet pytorch model to torch mlir
python iree-fork/alexnet-to-mlir.py

# compile (all the way down to executable)
../iree-build/tools/iree-compile --iree-hal-target-backends=llvm-cpu iree-fork/out/alexnet-as-mlir.mlir -o iree-fork/out/alexnet-executable.vmfb

# run
../iree-build/tools/iree-run-module \
    --device=local-task \
    --module=iree-fork/out/alexnet-executable.vmfb \
    --input=@iree-fork/out/alexnet-ex-input.npy > iree-fork/out/alexnet.out