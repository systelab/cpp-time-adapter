[![Build Status](https://travis-ci.org/systelab/cpp-time-adapter.svg?branch=master)](https://travis-ci.org/systelab/cpp-time-adapter)
[![Build status](https://ci.appveyor.com/api/projects/status/vl7vvxt33ex4l1bk?svg=true)](https://ci.appveyor.com/project/systelab/cpp-time-adapter)
[![codecov](https://codecov.io/gh/systelab/cpp-time-adapter/branch/master/graph/badge.svg)](https://codecov.io/gh/systelab/cpp-time-adapter)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6526d0da00cb4c90ad196782faf09523)](https://www.codacy.com/manual/systelab/cpp-time-adapter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=systelab/cpp-time-adapter&amp;utm_campaign=Badge_Grade)
[![Download](https://api.bintray.com/packages/systelab/conan/TimeAdapter:systelab/images/download.svg)](https://bintray.com/systelab/conan/TimeAdapter:systelab/_latestVersion)

# C++ Time Adapter Library

This library provides utilities to access system time.

## Setup

### Build from sources

Prerequisites:
  - [Git](https://git-scm.com/)
  - [Conan](https://conan.io/)
  - [CMake](https://cmake.org/)
  - [Visual Studio](https://visualstudio.microsoft.com/) (only on Windows)
  - [GCC](https://gcc.gnu.org/) (only on Linux)

Build library with the following steps:
  1. Clone this repository in a local drive
  2. Make a build directory (i.e. `build/`)
  3. Register bintray repository for Systelab libraries on conan
  4. Install `conan` dependencies in the build directory
  5. Run `cmake` in the build directory to configure build targets
  6. Use `Visual Studio` (on Windows) or `make` (on Linux) to build the library

#### Windows

In order to build the application on Windows for the `Release` configuration, run the following commands ($VSINSTALLPATH is the path where Visual Studio has been installed):

``` bash
> git clone https://github.com/systelab/cpp-time-adapter
> md build && cd build
> conan remote add systelab-bintray https://api.bintray.com/conan/systelab/conan
> conan install .. -s build_type=Release -s compiler.toolset=v142 -s arch=x86_64
> cmake .. -G "Visual Studio 16 2019" -A x64
> "$VSINSTALLPATH/devenv.com" TimeAdapter.sln /build "Release" /PROJECT "TimeAdapter"
```

However, if you want to `Debug` the source code, you will need these commands:

``` bash
> git clone https://github.com/systelab/cpp-time-adapter
> md build && cd build
> conan remote add systelab-bintray https://api.bintray.com/conan/systelab/conan
> conan install .. -s build_type=Debug -s compiler.toolset=v142 -s arch=x86_64
> cmake .. -G "Visual Studio 16 2019" -A x64
> "$VSINSTALLPATH/devenv.com" TimeAdapter.sln /build "Debug" /PROJECT "TimeAdapter"
```

#### Linux
``` bash
> git clone https://github.com/systelab/cpp-time-adapter
> mkdir build && cd build
> conan remote add systelab-bintray https://api.bintray.com/conan/systelab/conan
> conan install ..
> cmake .. -DCMAKE_BUILD_TYPE=[Debug | Coverage | Release]
> make
```

### Download using Conan

  1. Create/update your `conanfile.txt` to add this library as follows:

```
[requires]
TimeAdapter/1.0.0@systelab/stable

[generators]
cmake
```

  2. Integrate Conan into CMake by adding the following code into your `CMakeLists.txt`:

```cmake
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
```

  3. Link against `${CONAN_LIBS}` when configuring your executables in CMake:

```cmake
set(MY_PROJECT MyProject)
add_executable(${MY_PROJECT} main.cpp)
target_link_libraries(${MY_PROJECT} ${CONAN_LIBS})
```

## Usage

### Current time

The current time (in UTC) can be retrieved using an instance of `systelab::time::ITimeAdapter` as follows:

``` cpp
#include "TimeAdapter/ITimeAdapter.h"

systelab::time::ITimeAdapter& timeAdapter = ...
std::chrono::system_clock::time_point currentUTCTime = timeAdapter.getCurrentUTCTime();
```
