# -*- coding: utf-8 -*-
# renamer/app.py

"""This module provides the renamer application."""

import sys

from PyQt5.QtWidgets import QtApplication

from .views import Window

def main():
    # Create the application 
    app = QtApplication(sys.argv)
    # Create and show the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())