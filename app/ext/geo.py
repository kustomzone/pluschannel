"""
Copyright (C) 2012-2017  Luca Zanconato (<luca.zanconato@nharyes.net>)

This file is part of Plus Channel.

Plus Channel is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Plus Channel is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Plus Channel.  If not, see <http://www.gnu.org/licenses/>.
"""

from feedgen.ext.base import BaseExtension


class GeoExtension(BaseExtension):
    def extend_ns(self):
        return {'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#'}
