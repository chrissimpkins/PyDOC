PyDOC
=====

#### A Sublime Text 2/3 plugin that supports Python documentation search from selections in the editor.

## About

PyDOC allows you to search Python 2 or Python 3 documentation on [http://docs.python.org](http://docs.python.org/) for built-in Python modules, classes, methods, and functions that are selected in the Sublime Text editor.  A browser window is launched (in your default browser), using your selected text as the query term for the Python 2 or Python 3 documentation.

By default, the most recent Python 2 or Python 3 release documentation is used.

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

Select a built-in Python object in your editor text, then use the `Python 2 Doc Search` or `Python 3 Doc Search` menu item in the right click menu.

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

### Search with the Command Palette

Select a built-in Python object in your editor text then enter the keybinding to open the command palette (see description above in the Sublime Package Control section).  Type 'pydoc' and then select either `Python 2 Doc Search (PyDOC)` or `Python 3 Doc Search (PyDOC)`.

## Issues

Having a problem? Let's fix it.  Here are a few steps that will lead to the most rapid fix:

1. Make sure that you selected text in the editor before attempting to use PyDOC.  It's not that good (yet...).

2. Open the Sublime Text console with <code>Ctrl-`</code> or <code>View -> Show Console</code>, then run PyDOC again.  It generally provides helpful hints for problems and any exceptions that are raised will be displayed here.

3. Submit the issue on [the GitHub repository](https://github.com/chrissimpkins/PyDOC/issues) with as much detail as you can provide.  Please paste the console ouptut for any exceptions that are raised.

## License

[MIT License](https://github.com/chrissimpkins/PyDOC/blob/master/LICENSE)


