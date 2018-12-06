#!/usr/bin/env python
# encoding: utf-8

import sublime
import sublime_plugin
import webbrowser
from sys import version_info
import urllib

# Python 3 Documentation Search


class DocSearch(sublime_plugin.TextCommand):
    def run(self, edit, url, name, extra):
        try:
            for region in self.view.sel():
                if region.begin() == region.end():
                    word = self.view.word(region)
                else:
                    word = region
            if not word.empty():
                needle = self.view.substr(word)
                if len(needle.rstrip()) <= 1 or len(needle.lstrip()) <= 1:
                    print("PyDOC Plugin Error: You did not select text for "
                          "the {} documentation search. Please select a {} "
                          " object in your editor and"
                          " try again.".format(name, name))
                else:
                    if version_info[0] == 2:
                        # url encode Python 2 interpreter
                        needle = urllib.quote_plus(needle)
                        url = url + needle + extra
                    else:
                        url = url + needle + extra
                        # url encode Python 3 interpreter
                        url = urllib.parse.urlparse(url).geturl()
                    user_message = ("PyDOC: Performing search for {} "
                                    "documentation on the keyword, '" +
                                    needle + "'").format(name)
                    print(user_message)
                    sublime.status_message(user_message)
                    webbrowser.open(url)
            else:
                print("PyDOC Plugin Error: You did not select text for the "
                      "{} documentation search.  Please select a "
                      "{} object in your editor "
                      "and try again.".format(name, name))
                sublime.status_message(
                    "PyDOC Plugin Error: Text was not selected")
        except Exception as e:
            print(
                "PyDOC Plugin Error: There was an error "
                "during the execution of the plugin.\n")
            sublime.status_message("PyDOC Plugin Error: Open console for info")
            raise e


class TensorflowDocCommand(DocSearch):
    def run(self, edit):
        url = "https://www.tensorflow.org/s/results/?q="
        name = "TensorFlow"
        extra = ''
        super().run(edit, url, name, extra)


class PythonThreeDocCommand(DocSearch):
    def run(self, edit):
        url = "http://docs.python.org/3/search.html?q="
        name = "Python 3"
        extra = "&check_keywords=yes"
        super().run(edit, url, name, extra)


class NumpyDocCommand(DocSearch):
    def run(self, edit):
        url = "https://docs.scipy.org/doc/numpy/search.html?q="
        name = "Numpy"
        extra = ""
        super().run(edit, url, name, extra)


class ScipyDocCommand(DocSearch):
    def run(self, edit):
        url = "https://docs.scipy.org/doc/scipy/reference/search.html?q="
        name = "SciPy"
        extra = ""
        super().run(edit, url, name, extra)


class MatplotlibDocCommand(DocSearch):
    def run(self, edit):
        url = "https://matplotlib.org/search.html?q="
        name = "Matplotlib"
        extra = "&check_keywords=yes"
        super().run(edit, url, name, extra)


class PythonTwoDocCommand(DocSearch):
    def run(self, edit):
        url = "http://docs.python.org/2/search.html?q="
        name = "Python 2"
        extra = ""
        super().run(edit, url, name, extra)
