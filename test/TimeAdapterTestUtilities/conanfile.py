import os
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain
from conan.tools.files import collect_libs, copy

required_conan_version = ">=2.0.0"


class TimeAdapterTestUtilitiesConan(ConanFile):
    name = "time-adapter-test-utilities"
    description = "Test utilities for C++ time adapter library"
    url = "https://github.com/systelab/cpp-time-adapter"
    homepage = "https://github.com/systelab/cpp-time-adapter"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "json", "settings", "utils")
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "stdafx.h", "Mocks/*", "Stubs/*"

    def layout(self):
        self.folders.build = os.path.join("build", f"{self.settings.build_type}-{self.settings.arch}")
        self.folders.generators = self.folders.build

    def requirements(self):
        self.requires("gtest/1.14.0")
        self.requires(f"time-adapter/{self.version}")

    def generate(self):
        CMakeToolchain(self).generate()
        CMakeDeps(self).generate()
        for dep in self.dependencies.values():
            for bindir in dep.cpp_info.bindirs:
                copy(self, "*.dll", bindir, os.path.join(self.build_folder, "bin"))
            for libdir in dep.cpp_info.libdirs:
                copy(self, "*.dylib*", libdir, os.path.join(self.build_folder, "bin"))
                copy(self, "*.so*", libdir, os.path.join(self.build_folder, "bin"))

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "*.h", self.source_folder, os.path.join(self.package_folder, "include", "TimeAdapterTestUtilities"), keep_path=True)
        lib = os.path.join(self.package_folder, "lib")
        copy(self, "*TimeAdapterTestUtilities.lib", self.build_folder, lib, keep_path=False)
        copy(self, "*TimeAdapterTestUtilities.pdb", self.build_folder, lib, keep_path=False)
        copy(self, "*TimeAdapterTestUtilities.a", self.build_folder, lib, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
