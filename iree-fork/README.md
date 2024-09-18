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

### Run tests

```
ctest --test-dir ../iree-build/
```

### Install IREE Turbine

Using these instructions: https://github.com/iree-org/iree-turbine/tree/main?tab=readme-ov-file#developers

## Run a single file???

Read about it here: [../runtime/src/iree/runtime/demo/README.md](../runtime/src/iree/runtime/demo/README.md)

## extras

