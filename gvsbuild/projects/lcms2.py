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

from gvsbuild.utils.base_builders import Meson
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import project_add


@project_add
class Lcms2(Tarball, Meson):
    def __init__(self):
        Meson.__init__(
            self,
            "lcms2",
            version="2.19.1",
            repository="https://github.com/mm2/Little-CMS",
            archive_url="https://github.com/mm2/Little-CMS/releases/download/lcms{version}/lcms2-{version}.tar.gz",
            archive_filename="lcms2-{version}.tar.gz",
            hash="bfc54f7bab59fbc921012014a8032e4cba4abd46db47d46b76416a8c0b2815c8",
            dependencies=[
                "meson",
                "ninja",
                "pkgconf",
            ],
        )
        self.add_param("-Djpeg=disabled")
        self.add_param("-Dtests=disabled")
        self.add_param("-Dtiff=disabled")

    def build(self):
        Meson.build(self)

        self.install(r".\LICENSE share\doc\lcms2")
