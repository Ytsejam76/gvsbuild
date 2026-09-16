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
class Brotli(Tarball, CmakeProject):
    def __init__(self):
        Project.__init__(
            self,
            "brotli",
            version="1.2.0",
            repository="https://github.com/google/brotli",
            archive_url="https://github.com/google/brotli/archive/refs/tags/v{version}.tar.gz",
            archive_filename="brotli-{version}.tar.gz",
            hash="816c96e8e8f193b40151dad7e8ff37b1221d019dbcb9c35cd3fadbfe6477dfec",
            dependencies=[
                "cmake",
                "ninja",
            ],
        )

    def build(self):
        CmakeProject.build(
            self,
            cmake_params=[
                "-DBROTLI_BUILD_TOOLS=OFF",
                "-DBROTLI_DISABLE_TESTS=ON",
            ],
            use_ninja=True,
        )

        self.install(r".\LICENSE share\doc\brotli")
