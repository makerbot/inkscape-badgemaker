Thingiverse Badgemaker for Inkscape
===================================

This is an Inkscape extension that allows you to create Thingiverse Badges
using the Thingiverse Badge template, and save your Inkscape drawings as
OpenSCAD (.scad) files containing the code to render them into 3D shapes.

Author: [Marty McGuire](http://github.com/martymcguire)

Website: [http://github.com/makerbot/inkscape-badgemaker](http://github.com/makerbot/inkscape-badgemaker)

Credits
=======

* This is a fork of my [OpenSCAD Polygon extension](https://github.com/martymcguire/inkscape-openscad-poly).
* [Inkscape](http://www.inkscape.org/) is an awesome open source vector graphics app.
* [OpenSCAD](http://www.openscad.org/) is an awesome open source language for creating 3D objects.
* [Scribbles](https://github.com/makerbot/Makerbot/tree/master/Unicorn/Scribbles%20Scripts) is the original DXF-to-Unicorn Python script.
* [The Egg-Bot Driver for Inkscape](http://code.google.com/p/eggbotcode/) provided inspiration and good examples for working with Inkscape's extensions API.

Install
=======

Get the code by (preferred) cloning this Git repository or (not-preferred) downloading the .tar.gz or .zip from GitHub.

Symlink (preferred!) or copy the contents of `extensions/` to your Inkscape `extensions/` folder.

Symlink (preferred!) or copy the contents of `templates/` to your Inkscape `templates/` folder.

Typical locations for the `extensions` and `templates` folders include:

* OS X - `/Applications/Inkscape.app/Contents/Resources`
* Linux - `/usr/share/inkscape`
* Windows - `C:\Program Files\Inkscape\share`

Usage
=====

* Start with the **Thingiverse Badge** template by selecting it from the
  **File | New** menu.
* Work *only* in the layers named "Layer 1", "Layer 2", and "Layer 3"
* Keep your drawings inside the inset circle.
* Use only closed paths - individual lines and non-closed paths will
  cause bizarre behavior.
* Convert all text to paths:
	* Select all text objects.
	* Choose **Path | Object to Path**.
* Save as OpenSCAD:
	* **File | Save a Copy**.
	* Select **Thingiverse Badge (\*.scad)**.
	* Save your file.

Use in OpenSCAD
===============

* Open the **.scad** file you created above.
* Render it!
* Export as STL.

You'll find each layer from your Inkscape file appears as a `module` in the
resulting OpenSCAD file.

For example:

	// my_drawing.scad
	module layer1() {
	  polygon(points=
		[[-16.704628355490897, -20.69348168358303], [-13.479257330090903, -35.207652708983034], [-2.1904573300909078, -23.918852708983053], [17.161771644509102, -71.493081683583029], [-11.866570406290904, -40.045710658183026], [-13.479257330090903, -63.429652708983014], [-36.056857330090907, -56.172565785182996], [-30.412457330090902, -2.9539396327830048], [-0.57777040629089527, -1.3412527089830064], [16.355429593709104, -20.693481683583002], [38.126687542909096, -57.785252708983023]]
		, paths=
		[[0, 1, 2, 0], [3, 4, 5, 6, 7, 8, 9, 10, 3]]
		);}

The file also contains the calls necessary to extrude each of these layers into 3D.

TODOs
=====

* Choose better badge background colors.
* Parameterize layer heights.
* Parameterize smoothness for curve approximation.
* Add more TODOs.
