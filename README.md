PyDOC
=====

#### A Sublime Text 3 plugin that supports Python documentation search from selections in the editor.

## About

PyDOC is a plugin for Sublime Text 3 that allows you to open Python 2, 3, Numpy/SciPy/Matplotlib, and TensorFlow documentation from selections in your text editor.  The selected text is used as your query for the official documentation provided on docs.python.org and the respective package websites..  This is opened in your default browser.  By default, the documentation for the current release version of each package is opened.

## Install PyDOC

### Using Sublime Package Control

PyDOC can be installed using [Sublime Package Control](https://sublime.wbond.net/).  Open the command palette with:

##### Mac OSX
```
Cmd + Shift + P
```

##### Linux & Windows
```
Ctrl + Shift + P
```

Type `install` and select the menu item, `Package Control: Install Package`.

Type `PyDOC` and select the PyDOC package that is displayed.  This will install the package in your editor.

### Using Git

Use the Sublime Text menu items `Preferences -> Browse Packages` to locate your Packages directory.

Navigate to the directory in your terminal and clone the PyDOC source repository inside the Packages directory using the command:

``` bash
git clone https://github.com/chrissimpkins/PyDOC.git "PyDOC"
```

### Manual Install

Download the [zip compressed archive from GitHub](https://github.com/chrissimpkins/PyDOC/archive/master.zip).

Decompress the zip archive and rename the directory `PyDOC`.

Open your Sublime Text Packages directory using the `Preferences -> Browse Packages` menu items.

Move the entire `PyDOC` directory into your Sublime Text Packages directory.

## Use PyDOC

### Search with Right Click Menu

Select a built-in Python object in your editor text, then use the `Python 2 Doc Search`, `Python 3 Doc Search`, `Numpy Doc Search`, `SciPy Doc Search`, `Matplotlib Doc Search`, or `TensorFlow Doc Search` menu item in the right click menu.

### Search with Keybinding

Select a built-in Python object in your editor text, then use one of the following keybindings to perform the search:

##### Python 2 Documentation Search Keybinding

```
Ctrl-2
```

##### Python 3 Documentation Search Keybinding

```
Ctrl-3
```
##### Numpy Documentation Search Keybinding

```
Ctrl-4
```
##### SciPy Documentation Search Keybinding

```
Ctrl-5
```
##### Matplotlib Documentation Search Keybinding

```
Ctrl-6
```
##### TensorFlow Documentation Search Keybinding

```
Ctrl-7
```

### Search with the Command Palette

Select a built-in Python object in your editor text then enter the keybinding to open the command palette (see description above in the Sublime Package Control section).  Type 'pydoc' and then select either `Python 2 Doc Search (PyDOC)`, `Python 3 Doc Search (PyDOC)`,`Numpy Doc Search (PyDOC)`, `SciPy Doc Search (PyDOC)`, `Matplotlib Doc Search (PyDOC)`, or `TensorFlow Doc Search (PyDOC)`.

## Issues

Having a problem? Let's fix it.  Here are a few steps that will lead to the most rapid fix:

1. Make sure that you selected text in the editor before attempting to use PyDOC.  It's not that good (yet...).

2. Open the Sublime Text console with <code>Ctrl-`</code> or <code>View -> Show Console</code>, then run PyDOC again.  It generally provides helpful hints for problems and any exceptions that are raised will be displayed.

3. Submit the issue on [the GitHub repository](https://github.com/chrissimpkins/PyDOC/issues) with as much detail as you can provide.  Please paste the console ouptut for any exceptions that are raised.

## Changes

v.2.0.0 - Added support for nearest text to cursor.  Added support for Numpy, SciPy, maptlotlib, and TensorFlow documentation searches.

v.1.2.3 - added PyDOC to main menu for access to README and keybindings

v1.2.2 - updated user status and error messages, added install docs

v1.2.1 - added horizontal bar dividers to the context menu

v.1.2.0 - updated Python 2 & 3 URL handling

v1.1.1 - modified ST3 URL encoding (Python 3)

v.1.1.0 - modified ST2 URL encoding (Python 2)

v.1.0.1 - updated menu items

v1.0.0 - initial release


## License

[MIT License](https://github.com/chrissimpkins/PyDOC/blob/master/LICENSE)


