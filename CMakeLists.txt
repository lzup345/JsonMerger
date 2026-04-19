cmake_minimum_required(VERSION 4.2)
project(JsonMerger)

set(CMAKE_CXX_STANDARD 20)

add_executable(JsonMerger main.cpp
        json.hpp)
