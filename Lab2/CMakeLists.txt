cmake_minimum_required(VERSION 3.29)
project(Lab2 C)

set(CMAKE_C_STANDARD 11)

add_library(math_static STATIC math.c)
add_library(math_dynamic SHARED math.c)

add_executable(app_static main.c)
target_link_libraries(app_static math_static)

add_executable(app_dynamic main.c)
target_link_libraries(app_dynamic math_dynamic)

