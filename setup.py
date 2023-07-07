from pathlib import Path

from skbuild import setup

def exclude_static_libraries(cmake_manifest):
    return list(filter(lambda name: not (name.endswith(".a") and not name.endswith(".lib")), cmake_manifest))

here = Path(__file__).parent.resolve()
long_description = (here / "f3d" / "README.md").read_text(encoding="utf-8")

setup(
    name="f3d",
    description="F3D, a fast and minimalist 3D viewer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://f3d.app",
    project_urls={
        "Source Code": "https://github.com/f3d-app/f3d",
        "Bug Tracker": "https://github.com/f3d-app/f3d/issues",
        "Documentation": "https://f3d.app",
    },
    author="Michael Migliore and Mathieu Westphal",
    author_email="mcmigliore+pip@gmail.com",
    license="BSD 3-Clause",
    license_files=["LICENSE.md"],
    classifiers=[  # TODO?
        "License :: OSI Approved :: BSD License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Programming Language :: C++",
        "Programming Language :: Python :: 3",
    ],
    keywords="vtk;animations;fbx;step;stl;dcm;ex2;gml;obj;3ds;gltf;pbr;raytracing;scivis;volume;rendering",
    python_requires=">=3.7",
    packages=["f3d"],
    package_dir={
        "f3d": "python_packaging",
    },
    install_requires=[],
    entry_points={"console_scripts": ["f3d=f3d.__main__:main"]},
    cmake_source_dir=".",
    cmake_install_dir="python_packaging",
    cmake_args=[
        "-DCMAKE_PREFIX_PATH:PATH=" + str(here / "f3d-superbuild-build/install"),
        "-DCMAKE_BUILD_TYPE=Release",
        "-DCMAKE_OSX_DEPLOYMENT_TARGET=10.15",
        "-DBUILD_SHARED_LIBS=OFF",
        "-DF3D_BINDINGS_PYTHON=ON",
        "-DF3D_PLUGIN_BUILD_EXODUS=OFF",
        "-DF3D_PLUGIN_BUILD_ASSIMP=ON",
        "-DF3D_PLUGIN_BUILD_ALEMBIC=ON",
        "-DF3D_PLUGIN_BUILD_DRACO=ON",
        "-DF3D_MODULE_EXR=ON",
        "-DF3D_MODULE_EXTERNAL=ON",
        "-DF3D_BUILD_APPLICATION=OFF",
        "-DF3D_EXCLUDE_DEPRECATED=OFF",
    ],
    #cmake_process_manifest_hook=exclude_static_libraries,
    zip_safe=False,
)
