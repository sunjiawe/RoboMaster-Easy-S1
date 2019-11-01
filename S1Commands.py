#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Doc."""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import os
import sys
import shutil

import sublime
import sublime_plugin


def get_relative_path(relative_dir):
    """."""
    cur_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.normpath(os.path.join(cur_path, relative_dir))
    return dir_path


def add_relative_dir_to_sys_path(relative_dir):
    """."""
    dir_path = get_relative_path(relative_dir)
    sys.path.append(dir_path)


s1_instance = None
add_relative_dir_to_sys_path('libs')
s1_version = 0


def plugin_loaded():
    """."""
    global s1_instance
    #import runtime as s1_instance

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, S1!")

# #############################################
# # View Monitor
# #############################################
# class ViewMonitor(sublime_plugin.EventListener):
#     """."""

#     def __init__(self):
#         """."""
#         pass

#     def on_query_completions(self, view, prefix, locations):
#         pass