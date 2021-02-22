[![Build Status](https://travis-ci.org/systelab/cpp-time-adapter.svg?branch=master)](https://travis-ci.org/systelab/cpp-time-adapter)
[![Build status](https://ci.appveyor.com/api/projects/status/bgkmqmsbvyvkl2d6?svg=true)](https://ci.appveyor.com/project/systelab/cpp-time-adapter)
[![codecov](https://codecov.io/gh/systelab/cpp-time-adapter/branch/master/graph/badge.svg)](https://codecov.io/gh/systelab/cpp-time-adapter)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6526d0da00cb4c90ad196782faf09523)](https://www.codacy.com/manual/systelab/cpp-time-adapter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=systelab/cpp-time-adapter&amp;utm_campaign=Badge_Grade)
[![Download](https://api.bintray.com/packages/systelab/conan/TimeAdapter:systelab/images/download.svg)](https://bintray.com/systelab/conan/TimeAdapter:systelab/_latestVersion)

# C++ Time Adapter Library

This library provides utilities to access system time.


## Setup

### Download using Conan

This library is designed to be installed by making use of [Conan](https://conan.io/) package manager. So, you just need to add the following requirement into your Conan recipe:

```python
def requirements(self):
   self.requires("TimeAdapter/1.0.0@systelab/stable")
```

> Version number of this code snipped is set just as an example. Replace it for the desired package version to retrieve.

As this package is not available on the conan-center, you will also need to configure a remote repository before installing dependencies:

```bash
conan remote add systelab-public https://systelab.jfrog.io/artifactory/api/conan/cpp-conan-production-local
```

See Conan [documentation](https://docs.conan.io/en/latest/) for further details on how to integrate this package with your build system.

### Build from sources

See [BUILD.md](BUILD.md) document for details.


## Usage

### Current time

The current time (in UTC) can be retrieved using an instance of `systelab::time::ITimeAdapter` as follows:

``` cpp
#include "TimeAdapter/ITimeAdapter.h"

systelab::time::ITimeAdapter& timeAdapter = ...
std::chrono::system_clock::time_point currentUTCTime = timeAdapter.getCurrentUTCTime();
```
