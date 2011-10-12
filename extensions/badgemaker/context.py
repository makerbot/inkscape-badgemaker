from math import *
import sys

class BadgeLayerContext:
  def __init__(self, id, height):
    self.id = id
    self.height = height
    self.polygons = []

  def generate(self):
    print "module %s() {" % self.id
    for polygon in self.polygons:
      print "    // id: %s" % polygon['id']
      print "    polygon(points="
      print("      " + str(polygon['points']))
      print "      , paths="
      print("      " + str(polygon['paths']))
      print "      );"
    print "}"

  def generate_invocation(self):
    print "  linear_extrude(height = %s) %s();" % (self.height, self.id)

  def add_poly(self, id, points, paths):
    self.polygons.append({ 'id': id, 'points':points, 'paths':paths})

class BadgeContext:
  def __init__(self, file):
    self.file = file
    self.layers = [] # BadgeLayerContexts

  def generate(self):
    for layer in self.layers:
      layer.generate();
    # TODO: union all layers at their height
    print "union() {"
    for layer in self.layers:
      layer.generate_invocation();
    print "}"

  def add_layer(self, layer):
    self.layers.append(layer)

