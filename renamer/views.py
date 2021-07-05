# -*- coding: utf-8 -*-
# renamer/views.py

"""This module provides the renamer main window."""

from PyQt5.QtWidgets import QWidget

from .ui.window import Ui_Window

class Window(QWidget, Ui_Window):
    def __init__(self) -> None:
        super().__init__()
        self._setupUi()

    def _setupUi(self):
        self.setupUi()