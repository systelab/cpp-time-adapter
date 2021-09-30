import os
from conans import ConanFile, CMake, tools

class TimeAdapterTestUtilitiesConan(ConanFile):
    name = "TimeAdapterTestUtilities"
    description = "Test utilities for C++ time adapter library"
    url = "https://github.com/systelab/cpp-time-adapter"
    homepage = "https://github.com/systelab/cpp-time-adapter"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "json", "settings", "utils")
    license = "MIT"
    generators = "cmake_find_package"
    settings = "os", "compiler", "build_type", "arch"
    options = {"gtest": ["1.7.0", "1.8.1","1.10.0"]}
    default_options = {"gtest":"1.10.0"}
    exports_sources = "*"

    def configure(self):
        self.options["TimeAdapter"].gtest = self.options.gtest

    def requirements(self):
        if self.options.gtest == "1.7.0":
            self.requires("gtest/1.7.0@systelab/stable")
        elif self.options.gtest == "1.8.1":
            self.requires("gtest/1.8.1")
        elif self.options.gtest == "1.10.0":
            self.build_requires("gtest/1.10.0#0c895f60b461f8fee0da53a84d659131")
        else:
            self.build_requires(f"gtest/{self.options.gtest}")

        if ("%s" % self.version) == "None":
            self.requires("TimeAdapter/%s@systelab/stable" % os.environ['VERSION'])
        else:
            self.requires("TimeAdapter/%s@systelab/stable" % self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy("*.so*", dst="bin", src="lib")

    def package(self):
        self.copy("*.h", dst="include/TimeAdapterTestUtilities", keep_path=True)
        self.copy("*TimeAdapterTestUtilities.lib", dst="lib", keep_path=False)
        self.copy("*TimeAdapterTestUtilities.pdb", dst="lib", keep_path=False)
        self.copy("*TimeAdapterTestUtilities.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
