cmake_minimum_required(VERSION 3.19)
project(RoshanOS-Cpp-version LANGUAGES CXX)

set(CMAKE_AUTORCC ON)

find_package(Qt6 6.5 REQUIRED COMPONENTS Core Widgets)

qt_standard_project_setup()

qt_add_executable(RoshanOS-Cpp-version
    WIN32 MACOSX_BUNDLE
    main.cpp
    mainwindow.cpp
    mainwindow.h
    mainwindow.ui
    resources.qrc
    calculator.h calculator.cpp calculator.ui
)

target_link_libraries(RoshanOS-Cpp-version
    PRIVATE
        Qt::Core
        Qt::Widgets
)

install(TARGETS RoshanOS-Cpp-version
    BUNDLE  DESTINATION .
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

qt_generate_deploy_app_script(
    TARGET RoshanOS-Cpp-version
    OUTPUT_SCRIPT deploy_script
    NO_UNSUPPORTED_PLATFORM_ERROR
)
install(SCRIPT ${deploy_script})
