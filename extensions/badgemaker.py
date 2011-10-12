#!/usr/bin/env python
'''
Copyright (c) 2011 MakerBot(r) Industries

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''
import sys,os
import inkex
from math import *
import getopt
from badgemaker.context import BadgeContext
from badgemaker.svg_parser import BadgeSvgParser

class MyEffect(inkex.Effect):
  def __init__(self):
    inkex.Effect.__init__(self)
    self.OptionParser.add_option("--tab",
                      action="store", type="string",
                      dest="tab")

  def output(self):
    self.context.generate()

  def effect(self):
    self.context = BadgeContext(self.svg_file)
    parser = BadgeSvgParser(self.document.getroot())
    parser.parse()
    for layer in parser.layers:
      self.context.add_layer(layer)

if __name__ == '__main__':   #pragma: no cover
  e = MyEffect()
  e.affect()
