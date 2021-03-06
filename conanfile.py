from conans import ConanFile, CMake, tools

class TimeAdapterConan(ConanFile):
    name = "TimeAdapter"
    description = "C++ Time Adapter library"
    url = "https://github.com/systelab/cpp-time-adapter"
    homepage = "https://github.com/systelab/cpp-time-adapter"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "json", "configuration", "settings")
    license = "MIT"
    generators = "cmake_find_package"
    settings = "os", "compiler", "build_type", "arch"
    options = {"gtest": ["1.7.0", "1.8.1", "1.10.0"]}
    default_options = {"gtest":"1.10.0"}
    exports_sources = "*"

    def configure(self):
        self.options["TimeAdapter"].gtest = self.options.gtest

    def build_requirements(self):
        if self.options.gtest == "1.7.0":
            self.build_requires("gtest/1.7.0@systelab/stable")
        elif self.options.gtest == "1.8.1":
            self.build_requires("gtest/1.8.1")
        else:
            self.build_requires("gtest/1.10.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst=("bin/%s" % self.settings.build_type), src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy("*.so*", dst="bin", src="lib")

    def package(self):
        self.copy("ITimeAdapter.h", dst="include/TimeAdapter", src="src/TimeAdapter")
        self.copy("TimeAdapter.h", dst="include/TimeAdapter", src="src/TimeAdapter")
        self.copy("*TimeAdapter.lib", dst="lib", keep_path=False)
        self.copy("*TimeAdapter.pdb", dst="lib", keep_path=False)
        self.copy("*TimeAdapter.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
