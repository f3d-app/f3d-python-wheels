cmake_minimum_required(VERSION 3.15...3.26)

project(f3d-python-wheels VERSION "2.1")

include(GNUInstallDirs)
#include(FetchContent)
#
#FetchContent_Declare(
#  pybind11
#  URL https://github.com/pybind/pybind11/archive/refs/tags/v2.10.4.tar.gz
#  URL_HASH SHA256=832e2f309c57da9c1e6d4542dedd34b24e4192ecb4d62f6f4866a737454c9970
#  OVERRIDE_FIND_PACKAGE
#)
#FetchContent_MakeAvailable(pybind11)

add_subdirectory(f3d)
