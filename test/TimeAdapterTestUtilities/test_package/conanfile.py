import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain
from conan.tools.files import copy

required_conan_version = ">=2.0.0"


class TimeAdapterTestUtilitiesTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def layout(self):
        self.folders.build = os.path.join("build", f"{self.settings.build_type}-{self.settings.arch}")
        self.folders.generators = self.folders.build

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

    def test(self):
        cmake = CMake(self)
        cmake.test()
