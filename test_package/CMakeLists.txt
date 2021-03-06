cmake_minimum_required(VERSION 3.2)

project(TimeAdapterPackageTestProject)

# Configure environment
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../cmake ${CMAKE_BINARY_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Find tested package
find_package(TimeAdapter)

# Configure test package project
set(TIME_ADAPTER_PACKAGE_TEST_PROJECT TimeAdapterPackageTest)
add_executable(${TIME_ADAPTER_PACKAGE_TEST_PROJECT} TimeAdapterExample.cpp)
target_link_libraries(${TIME_ADAPTER_PACKAGE_TEST_PROJECT} TimeAdapter::TimeAdapter)

# Register test
enable_testing()
add_test(NAME TimeAdapterPackageTest COMMAND ${TIME_ADAPTER_PACKAGE_TEST_PROJECT})
