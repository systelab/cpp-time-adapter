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
    exports_sources = "*", "!test/TimeAdapterTestUtilities", "!build-*", "!*.yml", "!*.md", "!*.in", "!ci", "!.gitattributes", "!.gitignore", "!LICENSE"

    def requirements(self):
        self.requires("gtest/1.14.0#4372c5aed2b4018ed9f9da3e218d18b3")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
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
