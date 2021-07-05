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
        self._files = deque()
        self._filesCount = len(self._files)
        self._setupUi()
        self._connectSignalsSlots()

    def _setupUi(self):
        self.setupUi()

    def _connectSignalsSlots(self):
        self.loadFilesButton.clicked.connect(self.loadFiles)

    def loadFiles(self):
        self.dstFileList.clear()
        if self.dirEdit.text():
            initDir = self.dirEdit.text()
        else:
            initDir = str(Path.home())
        
        files, filter = QFileDialog.getOpenFileName(
            self, "Choose Files to rename", initDir, filter=FILTERS
        )

        if len(files) > 0:
            fileExtension = filter[filter.index("*"): -1]
            self.extensionLabel.setText(fileExtension)
            srcDirName = str(Path(files[0]).parent)
            self.dirEdit.setText(srcDirName)
            for file in files:
                self._files.append(Path(file))
                self.srcFileList.addItem(file)
            self._filesCount = len(self._files)