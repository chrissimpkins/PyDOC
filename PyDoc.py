#!/usr/bin/env python
# encoding: utf-8

import sublime
import sublime_plugin
import webbrowser
from sys import version_info
import urllib

# Python 3 Documentation Search

class TensorflowDocCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            for region in self.view.sel():
                if region.begin() == region.end():
                    word = self.view.word(region)
                else:
                    word = region
            if not word.empty():
                needle = self.view.substr(word)
                if len(needle.rstrip()) == 0 or len(needle.lstrip()) == 0:
                    print("PyDOC Plugin Error: You did not select text for the tensorflow documentation search.  Please select a tensorflow object in your editor and try again.")
                else:
                    if version_info[0] == 2:
                        # url encode Python 2 interpreter
                        needle = urllib.quote_plus(needle)
                        url = "https://www.tensorflow.org/s/results/?q=" + needle
                    else:
                        url = "https://www.tensorflow.org/s/results/?q=" + needle
                        # url encode Python 3 interpreter
                        url = urllib.parse.urlparse(url).geturl()
                    user_message = "PyDOC: Performing search for tensorflow documentation on the keyword, '" + needle + "'"
                    print(user_message)
                    sublime.status_message(user_message)
                    webbrowser.open(url)
            else:
                print("PyDOC Plugin Error: You did not select text for the tensorflow documentation search.  Please select a tensorflow object in your editor and try again.")
                sublime.status_message(
                    "PyDOC Plugin Error: Text was not selected")
        except Exception as e:
            print(
                "PyDOC Plugin Error: There was an error during the execution of the plugin.\n")
            sublime.status_message("PyDOC Plugin Error: Open console for info")
            raise e
class PythonThreeDocCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            for region in self.view.sel():
                if region.begin() == region.end():
                    word = self.view.word(region)
                else:
                    word = region
            if not word.empty():
                needle = self.view.substr(word)
                if len(needle.rstrip()) == 0 or len(needle.lstrip()) == 0:
                    print("PyDOC Plugin Error: You did not select text for the Python 3 documentation search.  Please select a Python built-in object in your editor and try again.")
                else:
                    if version_info[0] == 2:
                        # url encode Python 2 interpreter
                        needle = urllib.quote_plus(needle)
                        url = "http://docs.python.org/3/search.html?q=" + needle + "&check_keywords=yes"
                    else:
                        url = "http://docs.python.org/3/search.html?q=" + needle + "&check_keywords=yes"
                        # url encode Python 3 interpreter
                        url = urllib.parse.urlparse(url).geturl()
                    user_message = "PyDOC: Performing search for Python 3 documentation on the keyword, '" + needle + "'"
                    print(user_message)
                    sublime.status_message(user_message)
                    webbrowser.open(url)
            else:
                print("PyDOC Plugin Error: You did not select text for the Python 3 documentation search.  Please select a Python built-in object in your editor and try again.")
                sublime.status_message(
                    "PyDOC Plugin Error: Text was not selected")
        except Exception as e:
            print(
                "PyDOC Plugin Error: There was an error during the execution of the plugin.\n")
            sublime.status_message("PyDOC Plugin Error: Open console for info")
            raise e


class NumpyDocCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            for region in self.view.sel():
                if region.begin() == region.end():
                    word = self.view.word(region)
                else:
                    word = region
            if not word.empty():
                needle = self.view.substr(word)
                if len(needle.rstrip()) == 0 or len(needle.lstrip()) == 0:
                    print("PyDOC Plugin Error: You did not select text for the Numpy documentation search.  Please select a numpy object in your editor and try again.")
                else:
                    if version_info[0] == 2:
                        # url encode Python 2 interpreter
                        needle = urllib.quote_plus(needle)
                        url = "https://docs.scipy.org/doc/numpy-1.13.0/search.html?q=" + needle
                    else:
                        url = "https://docs.scipy.org/doc/numpy-1.13.0/search.html?q=" + needle
                        # url encode Python 3 interpreter
                        url = urllib.parse.urlparse(url).geturl()
                    user_message = "PyDOC: Performing search for Numpy documentation on the keyword, '" + needle + "'"
                    print(user_message)
                    sublime.status_message(user_message)
                    webbrowser.open(url)
            else:
                print("PyDOC Plugin Error: You did not select text for the Numpy documentation search.  Please select a numpy object in your editor and try again.")
                sublime.status_message(
                    "PyDOC Plugin Error: Text was not selected")
        except Exception as e:
            print(
                "PyDOC Plugin Error: There was an error during the execution of the plugin.\n")
            sublime.status_message("PyDOC Plugin Error: Open console for info")
            raise e


class ScipyDocCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            for region in self.view.sel():
                if region.begin() == region.end():
                    word = self.view.word(region)
                else:
                    word = region
            if not word.empty():
                needle = self.view.substr(word)
                if len(needle.rstrip()) == 0 or len(needle.lstrip()) == 0:
                    print("PyDOC Plugin Error: You did not select text for the Scipy documentation search.  Please select a scipy object in your editor and try again.")
                else:
                    if version_info[0] == 2:
                        # url encode Python 2 interpreter
                        needle = urllib.quote_plus(needle)
                        url = "https://docs.scipy.org/doc/scipy/reference/search.html?q=" + needle
                    else:
                        url = "https://docs.scipy.org/doc/scipy/reference/search.html?q=" + needle
                        # url encode Python 3 interpreter
                        url = urllib.parse.urlparse(url).geturl()
                    user_message = "PyDOC: Performing search for scipy documentation on the keyword, '" + needle + "'"
                    print(user_message)
                    sublime.status_message(user_message)
                    webbrowser.open(url)
            else:
                print("PyDOC Plugin Error: You did not select text for the Scipy documentation search.  Please select a scipy object in your editor and try again.")
                sublime.status_message(
                    "PyDOC Plugin Error: Text was not selected")
        except Exception as e:
            print(
                "PyDOC Plugin Error: There was an error during the execution of the plugin.\n")
            sublime.status_message("PyDOC Plugin Error: Open console for info")
            raise e

class MatplotlibDocCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            for region in self.view.sel():
                if region.begin() == region.end():
                    word = self.view.word(region)
                else:
                    word = region
            if not word.empty():
                needle = self.view.substr(word)
                if len(needle.rstrip()) == 0 or len(needle.lstrip()) == 0:
                    print("PyDOC Plugin Error: You did not select text for the matplotlib documentation search.  Please select a matplotlib object in your editor and try again.")
                else:
                    if version_info[0] == 2:
                        # url encode Python 2 interpreter
                        needle = urllib.quote_plus(needle)
                        url = "https://matplotlib.org/search.html?q=" + needle
                    else:
                        url = "https://matplotlib.org/search.html?q=" + needle
                        # url encode Python 3 interpreter
                        url = urllib.parse.urlparse(url).geturl()
                    user_message = "PyDOC: Performing search for matplotlib documentation on the keyword, '" + needle + "'"
                    print(user_message)
                    sublime.status_message(user_message)
                    webbrowser.open(url)
            else:
                print("PyDOC Plugin Error: You did not select text for the matplotlib documentation search.  Please select a matplotlib object in your editor and try again.")
                sublime.status_message(
                    "PyDOC Plugin Error: Text was not selected")
        except Exception as e:
            print(
                "PyDOC Plugin Error: There was an error during the execution of the plugin.\n")
            sublime.status_message("PyDOC Plugin Error: Open console for info")
            raise e



class PythonTwoDocCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            for region in self.view.sel():
                if region.begin() == region.end():
                    word = self.view.word(region)
                else:
                    word = region
            if not word.empty():
                needle = self.view.substr(word)
                if len(needle.rstrip()) == 0 or len(needle.lstrip()) == 0:
                    print("PyDOC Plugin Error: You did not select text for the Python 2 documentation search.  Please select a Python built-in object in your editor and try again.")
                else:
                    if version_info[0] == 2:
                        needle = urllib.quote_plus(needle)
                        url = "http://docs.python.org/2/search.html?q=" + needle + \
                            "&check_keywords=yes"  # url encode Python 2 interpreter
                    else:
                        url = "http://docs.python.org/2/search.html?q=" + needle + "&check_keywords=yes"
                        # url encode Python 3 interpreter
                        url = urllib.parse.urlparse(url).geturl()
                    user_message = "PyDOC: Performing search for Python 2 documentation on the keyword, '" + needle + "'"
                    print(user_message)
                    sublime.status_message(user_message)
                    webbrowser.open(url)
            else:
                print("PyDOC Plugin Error: You did not select text for the Python 2 documentation search.  Please select a Python built-in object in your editor and try again.")
                sublime.status_message(
                    "PyDOC Plugin Error: Text was not selected")
        except Exception as e:
            print(
                "PyDOC Plugin Error: There was an error during the execution of the plugin.\n")
            sublime.status_message("PyDOC Plugin Error: Open console for info")
            raise e
