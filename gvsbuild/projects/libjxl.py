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
            version="0.11.2",
            repository="https://github.com/libjxl/libjxl",
            archive_url="https://github.com/libjxl/libjxl/archive/refs/tags/v{version}.tar.gz",
            archive_filename="libjxl-{version}.tar.gz",
            hash="ab38928f7f6248e2a98cc184956021acb927b16a0dee71b4d260dc040a4320ea",
            dependencies=[
                "cmake",
                "ninja",
                "brotli",
                "highway",
            ],
        )

        self.add_param("-DJPEGXL_ENABLE_TOOLS=OFF")
        self.add_param("-DJPEGXL_ENABLE_JPEGLI=OFF")
        self.add_param("-DJPEGXL_ENABLE_DOXYGEN=OFF")
        self.add_param("-DJPEGXL_ENABLE_MANPAGES=OFF")
        self.add_param("-DJPEGXL_ENABLE_EXAMPLES=OFF")
        self.add_param("-DJPEGXL_ENABLE_PLUGINS=OFF")
        self.add_param("-DJPEGXL_ENABLE_FUZZERS=OFF")
        self.add_param("-DJPEGXL_ENABLE_DEVTOOLS=OFF")
        self.add_param("-DBUILD_TESTING=OFF")
        self.add_param("-DJPEGXL_FORCE_SYSTEM_HWY=ON")
        self.add_param("-DJPEGXL_FORCE_SYSTEM_BROTLI=ON")

    def build(self):
        CmakeProject.build(self, use_ninja=True)

        self.install(r".\LICENSE share\doc\libjxl")
