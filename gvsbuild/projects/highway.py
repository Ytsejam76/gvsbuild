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
class Highway(Tarball, CmakeProject):
    def __init__(self):
        Project.__init__(
            self,
            "highway",
            version="1.2.0",
            repository="https://github.com/google/highway",
            archive_url="https://github.com/google/highway/archive/refs/tags/{version}.tar.gz",
            archive_filename="highway-{version}.tar.gz",
            hash="7e0be78b8318e8bdbf6fa545d2ecb4c90f947df03f7aadc42c1967f019e63343",
            dependencies=[
                "cmake",
                "ninja",
            ],
        )

        self.add_param("-DHWY_ENABLE_TESTS=OFF")
        self.add_param("-DHWY_ENABLE_EXAMPLES=OFF")

    def build(self):
        CmakeProject.build(self, use_ninja=True)

        self.install(r".\LICENSE share\doc\highway")
