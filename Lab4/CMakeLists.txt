cmake_minimum_required(VERSION 4.1)
project(Lab4 C)

set(CMAKE_C_STANDARD 11)

add_executable(main_prog main.c)
add_executable(child_process child_process.c)
target_link_libraries(child_process wininet)