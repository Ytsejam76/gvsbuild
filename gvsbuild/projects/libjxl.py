#  Copyright (C) 2016 The Gvsbuild Authors
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from gvsbuild.utils.base_builders import CmakeProject
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add


@project_add
class Libjxl(Tarball, CmakeProject):
    def __init__(self):
        Project.__init__(
            self,
            "libjxl",
            version="0.12.0",
            repository="https://github.com/libjxl/libjxl",
            archive_url="https://github.com/libjxl/libjxl/archive/refs/tags/v{version}.tar.gz",
            archive_filename="libjxl-{version}.tar.gz",
            hash="03e9be69a30be4011f559da75328b6d7cea8ad921fabfbd551ce10bf45cdc992",
            dependencies=[
                "cmake",
                "ninja",
                "brotli",
                "highway",
                "lcms2",
            ],
            patches=[
                "0001-Include-intrin.h-before-using-_sub_overflow_i32-on-M.patch",
            ],
        )

    def build(self):
        # The release tarball ships no third_party sources, so brotli, highway
        # and lcms2 must come from the already built projects.
        cmake_params = [
            f"-DCMAKE_PREFIX_PATH={self.builder.gtk_dir}",
            "-DBUILD_TESTING=OFF",
            "-DJPEGXL_ENABLE_TOOLS=OFF",
            "-DJPEGXL_ENABLE_DEVTOOLS=OFF",
            "-DJPEGXL_ENABLE_DOXYGEN=OFF",
            "-DJPEGXL_ENABLE_MANPAGES=OFF",
            "-DJPEGXL_ENABLE_BENCHMARK=OFF",
            "-DJPEGXL_ENABLE_EXAMPLES=OFF",
            "-DJPEGXL_ENABLE_JNI=OFF",
            "-DJPEGXL_ENABLE_SJPEG=OFF",
            "-DJPEGXL_ENABLE_OPENEXR=OFF",
            "-DJPEGXL_ENABLE_PLUGINS=OFF",
            "-DJPEGXL_ENABLE_FUZZERS=OFF",
            "-DJPEGXL_ENABLE_SKCMS=OFF",
            "-DJPEGXL_BUNDLE_LIBPNG=OFF",
            "-DJPEGXL_FORCE_SYSTEM_BROTLI=ON",
            "-DJPEGXL_FORCE_SYSTEM_HWY=ON",
            "-DJPEGXL_FORCE_SYSTEM_LCMS2=ON",
        ]

        CmakeProject.build(self, cmake_params=cmake_params, use_ninja=True)

        self.install(r".\LICENSE share\doc\libjxl")
