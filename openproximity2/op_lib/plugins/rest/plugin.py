# -*- coding: utf-8 -*-
# REST interface for OpenProximity
# Copyright (C) 2010 Manuel Coli <manuel@polline.net>
# Copyright (C) 2010,2009,2008 Naranjo Manuel Francisco <manuel@aircable.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

name='REST interface plugin'	# friendly name
enabled=True			# disable me please
django=True                     # expose me as a django enabled plugin

urls=( 'REST', 'urls' )		# urls I give to django
