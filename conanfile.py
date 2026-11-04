import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain
from conan.tools.files import collect_libs, copy

required_conan_version = ">=2.0.0"


class TimeAdapterConan(ConanFile):
    name = "time-adapter"
    description = "C++ Time Adapter library"
    url = "https://github.com/systelab/cpp-time-adapter"
    homepage = "https://github.com/systelab/cpp-time-adapter"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "json", "configuration", "settings")
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "*", "!test/TimeAdapterTestUtilities", "!build*", "!*.yml", "!*.md", "!*.in", "!ci", "!.gitattributes", "!.gitignore", "!LICENSE"

    def requirements(self):
        self.requires("gtest/1.14.0")

    def generate(self):
        CMakeToolchain(self).generate()
        CMakeDeps(self).generate()
        for dep in self.dependencies.values():
            for bindir in dep.cpp_info.bindirs:
                copy(self, "*.dll", bindir, os.path.join(self.build_folder, "bin", str(self.settings.build_type)))
            for libdir in dep.cpp_info.libdirs:
                copy(self, "*.dylib*", libdir, os.path.join(self.build_folder, "bin"))
                copy(self, "*.so*", libdir, os.path.join(self.build_folder, "bin"))

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        inc = os.path.join(self.package_folder, "include", "TimeAdapter")
        src = os.path.join(self.source_folder, "src", "TimeAdapter")
        copy(self, "ITimeAdapter.h", src, inc)
        copy(self, "TimeAdapter.h", src, inc)
        lib = os.path.join(self.package_folder, "lib")
        copy(self, "*TimeAdapter.lib", self.build_folder, lib, keep_path=False)
        copy(self, "*TimeAdapter.pdb", self.build_folder, lib, keep_path=False)
        copy(self, "*TimeAdapter.a", self.build_folder, lib, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
