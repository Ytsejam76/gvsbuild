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
            version="1.1.0",
            repository="https://github.com/google/brotli",
            archive_url="https://github.com/google/brotli/archive/refs/tags/v{version}.tar.gz",
            archive_filename="brotli-{version}.tar.gz",
            hash="e720a6ca29428b803f4ad165371771f5398faba397edf6778837a18599ea13ff",
            dependencies=[
                "cmake",
                "ninja",
            ],
        )

    def build(self):
        CmakeProject.build(self, use_ninja=True)

        self.install(r".\LICENSE share\doc\brotli")
