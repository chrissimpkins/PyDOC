#!/usr/bin/env python
# encoding: utf-8

import sublime
import sublime_plugin
import webbrowser
from sys import version_info
import urllib

# Python 3 Documentation Search
class PythonThreeDocCommand(sublime_plugin.TextCommand):
    def run(self, selected_text):
        try:
            selections = self.view.sel()
            if selections:
                needle = self.view.substr(selections[0])
                if len(needle) == 0:
                    print("PyDOC Plugin Error: There was no selected string for the Python 3 documentation search.  Please select a string in your document and try again.")
                else:
                    if version_info[0] == 2:
                        needle = urllib.quote_plus(needle) # url encode Python 2 interpreter
                        url = "http://docs.python.org/3/search.html?q=" + needle + "&check_keywords=yes"
                    else:
                        url = "http://docs.python.org/3/search.html?q=" + needle + "&check_keywords=yes"
                        url = urllib.parse.urlparse(url).geturl() # url encode Python 3 interpreter
                    print("PyDOC: Performing search for Python 3 documentation on the keyword, '" + needle + "'")
                    webbrowser.open(url)
            else:
                print("PyDOC Plugin Error: There was no selected string for the search.  Please select a string in your document and try again.")
        except Exception as e:
            print("PyDOC Plugin Error: There was an error during the execution of the plugin.\n")
            raise e

# Python 2 Documentation Search
class PythonTwoDocCommand(sublime_plugin.TextCommand):
    def run(self, selected_text):
        try:
            selections = self.view.sel()
            if selections:
                needle = self.view.substr(selections[0])
                if len(needle) == 0:
                    print("PyDOC Plugin Error: There was no selected string for the Python 2 documentation search.  Please select a string in your document and try again.")
                else:
                    if version_info[0] == 2:
                        needle = urllib.quote_plus(needle)
                        url = "http://docs.python.org/2/search.html?q=" + needle + "&check_keywords=yes" # url encode Python 2 interpreter
                    else:
                        url = "http://docs.python.org/2/search.html?q=" + needle + "&check_keywords=yes"
                        url = urllib.parse.urlparse(url).geturl() # url encode Python 3 interpreter
                    print("PyDOC: Performing search for Python 2 documentation on the keyword, '" + needle + "'")
                    webbrowser.open(url)
            else:
                print("PyDOC Plugin Error: There was no selected string for the search.  Please select a string in your document and try again.")
        except Exception as e:
            print("PyDOC Plugin Error: There was an error during the execution of the plugin.\n")
            raise e

