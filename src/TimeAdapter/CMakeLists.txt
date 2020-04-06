cmake_minimum_required(VERSION 3.2)

# Add project folder into includes
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Configure TimeAdapter static library
set(TIME_ADAPTER TimeAdapter)
file(GLOB_RECURSE TIME_ADAPTER_SRC "*.cpp")
file(GLOB_RECURSE TIME_ADAPTER_HDR "*.h")
add_library(${TIME_ADAPTER} STATIC ${TIME_ADAPTER_SRC} ${TIME_ADAPTER_HDR})
target_link_libraries(${TIME_ADAPTER})

#Configure source groups
foreach(FILE ${TIME_ADAPTER_SRC} ${TIME_ADAPTER_HDR}) 
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

