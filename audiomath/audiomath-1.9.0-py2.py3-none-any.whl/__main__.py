# $BEGIN_AUDIOMATH_LICENSE$
# 
# This file is part of the audiomath project, a Python package for
# recording, manipulating and playing sound files.
# 
# Copyright (c) 2008-2020 Jeremy Hill
# 
# audiomath is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/ .
# 
# The audiomath distribution includes binaries from the third-party
# AVbin and PortAudio projects, released under their own licenses.
# See the respective copyright, licensing and disclaimer information
# for these projects in the subdirectories `audiomath/_wrap_avbin`
# and `audiomath/_wrap_portaudio` . It also includes a fork of the
# third-party Python package `pycaw`, released under its original
# license (see `audiomath/pycaw_fork.py`).
# 
# $END_AUDIOMATH_LICENSE$
"""
If no options are supplied, `-s` is assumed---i.e., an IPython
shell will be opened on the console, with `audiomath` and `numpy`
already imported (both under their full names and under their
respective abbreviated names, `am` and `np`).

If options are supplied, the shell will not be opened unless the
`-s` option is explicitly present among them.
"""
import argparse
		
parser = argparse.ArgumentParser( prog='python -m ' + __package__, description=__doc__ )
parser.add_argument( "-v", "--version", action='store_true', default=False, help='print the version number' )
parser.add_argument( "-V", "--versions", action='store_true', default=False, help='print package and dependency version information' )
parser.add_argument( "-a", "--apis", "--host-apis", action='store_true', default=False, help='print a list of host APIs' )
parser.add_argument( "-d", "--devices", action='store_true', default=False, help='print a list of devices' )
parser.add_argument( "-8", "--eightChannelTest", action='store_true', default=False, help='play an 8-channel test stimulus on an endless loop' )
parser.add_argument( "-s", "--shell", action='store_true', default=False, help='open an IPython shell, even if other flags are supplied' )
parser.add_argument(       "--device",  metavar='DEVICE_INDEX',  action='store', default=None, type=int, help='specify which device should be used for playback in the --eightChannelTest' )
parser.add_argument(       "--install-ffmpeg",  metavar='PATH_TO_FFMPEG_BINARY',  action='store', default=None, type=str, help='call `ffmpeg.Install()` on the specified path' )
parser.add_argument(       "--install-sox",  metavar='PATH_TO_SOX_BINARY', action='store', default=None, type=str, help='call `sox.Install()` on the specified path' )
args = parser.parse_args()

openShell = True
player = None
playerName = 'p'

if args.version:
	openShell = args.shell
	import audiomath
	print( audiomath.__version__ )

if args.versions:
	openShell = args.shell
	import audiomath
	print( '' )
	audiomath.ReportVersions()

if args.apis:
	openShell = args.shell
	import audiomath
	print( '' )
	print( audiomath.GetHostApiInfo() )

if args.devices:
	openShell = args.shell
	import audiomath
	print( '' )
	print( audiomath.GetDeviceInfo() )

if args.eightChannelTest:
	openShell = args.shell
	import audiomath
	player = audiomath.Player( audiomath.TestSound(), device=args.device )
	if openShell:
		print( '\n%s = %r' % ( playerName, player ) )
		player.Play( loop=True, wait=False )
	else:
		print( '\n%s\n\npress ctrl-C to stop/exit' % player.sound )
		player.Play( loop=True, wait=True )
		import time; time.sleep( 0.25 )

if args.install_ffmpeg:
	openShell = args.shell
	import audiomath
	try: audiomath.ffmpeg.Install( args.install_ffmpeg )
	except Exception as err: sys.sterr.write( '%s\n' % err )

if args.install_sox:
	openShell = args.shell
	import audiomath
	try: audiomath.sox.Install( args.install_sox )
	except Exception as err: sys.sterr.write( '%s\n' % err )

if openShell:
	def Shell():
		if player: locals()[ playerName ] = player
		import os, sys, time, IPython, numpy, numpy as np, audiomath, audiomath as am
		del sys.argv[ 1: ]
		print( '' )
		IPython.start_ipython( user_ns=locals() )	
	Shell()
