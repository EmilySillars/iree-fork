# Emily's IREE Fork

## setup

0. Note: setup instructions are based on these: https://iree.dev/building-from-source/getting-started/#quickstart-clone-and-build

1. clone this forked repo, then switch to the tiling branch

```
git clone https://github.com/EmilySillars/iree-fork.git

git switch tiling
```

2. don't forget about all the submodules!

```
git submodule update --init
```

## Build IREE (development build) to target x86 + use python bindings

0. make sure your  Python installation >=3.9

1. navigate to this repo's top level directory

2. create a virtual environment + activate it

   ```
   python -m venv .venv
   source .venv/bin/activate
   ```

   use `deactivate` when finished.

3. upgrade pip + install iree-specific requirements

```
# Upgrade PIP before installing other requirements
python -m pip install --upgrade pip

# Install IREE build requirements
python -m pip install -r runtime/bindings/python/iree/runtime/build_requirements.txt
```

Can also install pytorch inside this environment with `pip install torchvision `

4. configure build settings as follows...

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

5. build with

```
cmake --build ../iree-build/
```

### I. Run tests

```
ctest --test-dir ../iree-build/
```

### II. Compile + Run a single MLIR file

1. vector-mul.mlir: 
   ````
   sh iree-fork/vector-mul.sh
   ````

2. matmul4x4.mlir
   ```
   sh iree-fork/matmul4x4.sh
   ```

3. matmul104x104.mlir
   ```
   sh iree-fork/matmul104x104.sh
   ```

### III. Compile Neural Network Kernels

1. matmul extracted from alexnet ([more details here](pulling-out-a-matmul-kernel.md))

   ```
   sh iree-fork/compile-from-mlir.sh alexnetMatmul
   ```

### Install IREE Turbine (outside of this repo)

Using these instructions: https://github.com/iree-org/iree-turbine/tree/main?tab=readme-ov-file#developers

1. `git clone https://github.com/iree-org/iree-turbine.git`

2. `cd iree-turbine`

3. set up a virtual environment
   ```
   python -m venv --prompt iree-turbine .venv
   source .venv/bin/activate
   ```

4. Install pytorch
   ```
   pip install -r pytorch-cpu-requirements.txt
   ```

5. Install dev packages
   ```
   # Install editable local projects.
   pip install -r requirements.txt -e .
   ```

6. Make sure everything is okay by running tests with
   ```
   pytest .
   ```

#### Make IREE Turbine use *your* IREE build

1. Inside the virtual environment, make sure to uninstall the iree compiler (so you don't accidentally use it instead of your dev build):

```
pip uninstall iree-compiler
pip uninstall iree-runtime
```

2. Copy the .env file from your iree build folder into the top level directory of your iree-turnine repo!

Then, before running any iree-turbine commands, do

```
source .env && export PYTHONPATH
```

#### Convert Python to MLIR using IREE Turbine

I am not sure I even needed to clone the iree-turbine repo.

It provides an ahead of time compilation tool that produces MLIR, for example [here](https://github.com/iree-org/iree-turbine/blob/main/examples/aot_mlp/mlp_export_simple.py), but maybe all I need to do is install iree-turbine with `pip install iree-turbine` for use as an end-user. Let's try that.

1. navigate to top-level iree-fork directory

2. ```
   source .venv/bin/activate
   ```

3. ```
   pip install iree-turbine
   ```

4. Now I can write a python file that uses the iree-turbine export functions to convert pytorch models to mlir...

- **Convert alexnet to MLIR and run:**

  ```
  sh iree-fork/alexnet-to-mlir.sh
  ```

- **Convert alexnet to MLIR and output linalg:**

  ```
  sh iree-fork/alexnet-to-linalg.sh
  ```

## extras

### notes

--mlir-print-local-scope

```
iree-compile \
    --iree-hal-target-backends=llvm-cpu \
    mobilenet_iree_input.mlir -o mobilenet_cpu.vmfb
```

I will try this:

```
../iree-build/tools/iree-compile --iree-hal-target-backends=llvm-cpu iree-fork/matmul.mlir -o iree-fork/out/matmul.vmfb
```

hoodle

#### Run a single file???

Read about it here: [../runtime/src/iree/runtime/demo/README.md](../runtime/src/iree/runtime/demo/README.md)
