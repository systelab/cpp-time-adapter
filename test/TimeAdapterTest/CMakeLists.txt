cmake_minimum_required(VERSION 3.2)

# Enable testing module
enable_testing()

# Add project folder into includes
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Find external dependencides
find_package(gtest)
find_package(TimeAdapterTestUtilities)

# Configure test project
set(TIME_ADAPTER_TEST_PROJECT TimeAdapterTest)
file(GLOB_RECURSE TIME_ADAPTER_TEST_PROJECT_SRC "*.cpp")
file(GLOB_RECURSE TIME_ADAPTER_TEST_PROJECT_HDR "*.h")
add_executable(${TIME_ADAPTER_TEST_PROJECT} ${TIME_ADAPTER_TEST_PROJECT_SRC} ${TIME_ADAPTER_TEST_PROJECT_HDR})
target_link_libraries(${TIME_ADAPTER_TEST_PROJECT} TimeAdapter 
					  gtest::gtest TimeAdapterTestUtilities::TimeAdapterTestUtilities)

# Ignored missing PDBs link warning on Visual Studio
if (CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
	set_target_properties(${TIME_ADAPTER_TEST_PROJECT} PROPERTIES LINK_FLAGS "/ignore:4099")
endif()

#Configure source groups
foreach(FILE ${TIME_ADAPTER_TEST_PROJECT_SRC} ${TIME_ADAPTER_TEST_PROJECT_HDR}) 
    get_filename_component(PARENT_DIR "${FILE}" DIRECTORY)
    string(REPLACE "${CMAKE_CURRENT_SOURCE_DIR}" "" GROUP "${PARENT_DIR}")
    string(REPLACE "/" "\\" GROUP "${GROUP}")

    if ("${FILE}" MATCHES ".*\\.cpp")
       set(GROUP "Source Files${GROUP}")
    elseif("${FILE}" MATCHES ".*\\.h")
       set(GROUP "Header Files${GROUP}")
    endif()

    source_group("${GROUP}" FILES "${FILE}")
endforeach()

# Register tests
add_test(NAME TimeAdapterTest COMMAND ${TIME_ADAPTER_TEST_PROJECT})

# Additional target for code coverage analysis
if (CMAKE_BUILD_TYPE STREQUAL "Coverage")
	include(CodeCoverage)
	setup_target_for_coverage(TimeAdapterTestCoverage TimeAdapterTest coverage)
endif()
