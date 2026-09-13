cmake_minimum_required(VERSION 3.12)

project(RoshanSystem CXX)

set(CMAKE_CXX_STANDARD 26)

find_package(Qt6 COMPONENTS Core Gui Widgets)
find_package(nlohmann_json)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(ASSETS
        "${CMAKE_CURRENT_SOURCE_DIR}/textures"
        "${CMAKE_CURRENT_SOURCE_DIR}/styling"
)

add_library(RoshanSystemCoreLib SHARED
        core/style.cpp
        core/style.h
        core/window.cpp
        core/window.h
        core/core.h
        core/filedialog.cpp
        core/filedialog.h
)

target_link_libraries(RoshanSystemCoreLib PRIVATE Qt6::Core Qt6::Widgets Qt6::Gui nlohmann_json::nlohmann_json)
target_include_directories(RoshanSystemCoreLib PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/core")

qt_add_executable(
        RoshanSystem
        main.cpp
        mainWidgets/taskbar.cpp
        mainWidgets/taskbar.h
)

set_target_properties(RoshanSystem PROPERTIES
        WIN32_EXECUTABLE TRUE
        MACOSX_BUNDLE TRUE
)

set_target_properties(RoshanSystemCoreLib PROPERTIES
        WINDOWS_EXPORT_ALL_SYMBOLS ON
        CXX_VISIBILITY_PRESET default
        C_VISIBILITY_PRESET default
        VISIBILITY_INLINES_HIDDEN OFF
)

target_link_libraries(RoshanSystem PRIVATE Qt6::Core Qt6::Widgets Qt6::Gui nlohmann_json::nlohmann_json RoshanSystemCoreLib)

add_custom_target(RoshanSystemCopy ALL
    COMMAND ${CMAKE_COMMAND} -E copy_directory
        "${CMAKE_CURRENT_SOURCE_DIR}/textures"
        "${CMAKE_BINARY_DIR}/textures"
    COMMAND ${CMAKE_COMMAND} -E copy_directory
        "${CMAKE_CURRENT_SOURCE_DIR}/styling"
        "${CMAKE_BINARY_DIR}/styling"
    COMMENT "Copying textures and styling to the build dir"
)

add_dependencies(RoshanSystem RoshanSystemCopy)
