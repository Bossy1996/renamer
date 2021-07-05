# -*- coding: utf-8 -*-
# renamer/views.py

"""This module provides the renamer main window."""

from collections import deque
from pathlib import Path

from PyQt5.QtWidgets import QFileDialog,QWidget

from .ui.window import Ui_Window

FILTERS = ";;".join(
    (
        "PNG Files (*.png)",
        "JPEG Files (*.jpeg)",
        "JPG Files (*.jpg)",
        "GIF Files (*.gif)",
        "TextFiles (*.txt)",
        "Python Files (*.py)", 
    )
)

class Window(QWidget, Ui_Window):
    def __init__(self) -> None:
        super().__init__()
        self._setupUi()

    def _setupUi(self):
        self.setupUi()