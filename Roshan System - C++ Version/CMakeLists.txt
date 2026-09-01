cmake_minimum_required(VERSION 4.0)

project(RoshanSystem CXX)

set(CMAKE_CXX_STANDARD 26)

find_package(Qt6 COMPONENTS Core Gui Widgets)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(ASSETS
        "${CMAKE_CURRENT_SOURCE_DIR}/textures"
        "${CMAKE_CURRENT_SOURCE_DIR}/styling"
)

qt_add_executable(
        RoshanSystem
        main.cpp
        ${ASSETS}
        core/style.cpp
        core/style.h
        core/window.cpp
        core/window.h
)

target_link_libraries(${PROJECT_NAME} PRIVATE Qt6::Core Qt6::Widgets Qt6::Gui stdc++exp)

add_custom_target(RoshanSystemCopy ALL
    COMMAND ${CMAKE_COMMAND} -E copy_directory
        "${CMAKE_CURRENT_SOURCE_DIR}/textures"
        "${CMAKE_BINARY_DIR}/textures"
    COMMAND ${CMAKE_COMMAND} -E copy_directory
        "${CMAKE_CURRENT_SOURCE_DIR}/styling"
        "${CMAKE_BINARY_DIR}/styling"
    COMMENT "Copying textures and styling to the build dir"
)

add_dependencies(${PROJECT_NAME} RoshanSystemCopy)