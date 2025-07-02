cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

add_library(mymath STATIC src/mymath.cpp)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)
find_package(Python3 REQUIRED COMPONENTS Interpreter)

pybind11_add_module(${SKBUILD_PROJECT_NAME} src/binder.cpp)
target_link_libraries(${SKBUILD_PROJECT_NAME} PRIVATE mymath)

enable_testing()

target_compile_definitions(${SKBUILD_PROJECT_NAME}
                           PRIVATE VERSION_INFO=${SKBUILD_PROJECT_VERSION})

install(TARGETS ${SKBUILD_PROJECT_NAME}
    LIBRARY DESTINATION .
)


