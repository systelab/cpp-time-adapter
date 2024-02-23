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
    exports_sources = "*", "!build*"

    def requirements(self):
        self.requires("gtest/1.14.0#4372c5aed2b4018ed9f9da3e218d18b3")

        if ("%s" % self.version) == "None":
            channel = os.environ['CHANNEL'] if "CHANNEL" in os.environ else "stable"
            self.requires(f"TimeAdapter/{os.environ['VERSION']}@systelab/{channel}")
        else:
            self.requires(f"TimeAdapter/{self.version}@systelab/{self.channel}")

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
