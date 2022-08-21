#! /usr/bin/python3
# -*- coding: utf-8 -*-
# ##############################################################################
# Copyright 2020 AlexPDev
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################
"""Module for stylesheets."""

import os
from urllib.request import pathname2url as path2url

from torrentfileQt.utils import get_icon

arrow = path2url(os.path.relpath(get_icon("arrow-down"), os.getcwd()))

dark_theme = """
* {
    background-color: #19232D;
    color: #FFFFFF;
    padding: 0px;
    margin: 0px;
    border-width: 0px;
    border-style: solid;
}
QMenu,
QTreeWidget,
QTreeWidget::item,
QTableWidget,
QTableWidget::item,
QHeaderView::section,
QTableView QTableCornerButton::section,
QLineEdit,
QTextEdit,
QComboBox,
QComboBox:editable,
QComboBox QAbstractItemView,
QProgressBar,
QScrollBar {
    border-width: 0px;
    border-style: solid;
    border-radius: 0px;
    padding: 0px;
    margin: 0px;
}
QHeaderView::section,
QTableView QTableCornerButton::section,
QLineEdit,
QTextEdit,
QComboBox:editable,
QComboBox,
QComboBox QAbstractItemView,
QProgressBar,
QScrollBar {
    border-color: #f61;
    selection-background-color: #2f4f4f;
}
QLabel,
QLabel:disabled {
    border-width: 1px;
    background-color: transparent;
    padding: 0px;
    font-size: 8pt;
    border-color: transparent;
    selection-background-color: #2f4f4f;
}
QMainWindow::separator {
    background: #000;
    border-width: 0px;
}
QMainWindow::separator:hover {
    background: transparent;
}
QWidget {
    background-color: #39434d;
    border-width: 0px;
}
QAbstractScrollArea {
    background-color: #19232D;
    border: 1px solid #f61;
    border-radius: 4px;
    padding: 2px;
    color: #E0E1E3;
}
QAbstractScrollArea:disabled {
    color: #9DA9B5;
}
QScrollArea QWidget QWidget:disabled {
    background-color: #19232D;
}
QScrollBar:horizontal {
    height: 16px;
    margin: 2px 16px 2px 16px;
    border: 1px solid #455364;
    border-radius: 4px;
    background-color: #19232D;
}
QScrollBar:vertical {
    background-color: #19232D;
    width: 16px;
    margin: 16px 2px 16px 2px;
    border: 1px solid #455364;
    border-radius: 4px;
}
QScrollBar::handle:horizontal {
    background-color: #60798B;
    border: 1px solid #455364;
    border-radius: 4px;
    min-width: 8px;
}
QScrollBar::handle:horizontal:hover {
    background-color: #346792;
    border: #346792;
    border-radius: 4px;
    min-width: 8px;
}
QScrollBar::handle:horizontal:focus {
    border: 1px solid #1A72BB;
}
QScrollBar::handle:vertical {
    background-color: #60798B;
    border: 1px solid #455364;
    min-height: 8px;
    border-radius: 4px;
}
QScrollBar::handle:vertical:hover {
    background-color: #346792;
    border: #346792;
    border-radius: 4px;
    min-height: 8px;
}
QScrollBar::handle:vertical:focus {
    border: 1px solid #1A72BB;
}
QScrollBar::add-line:horizontal {
    margin: 0px 0px 0px 0px;
    height: 12px;
    width: 12px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}
QScrollBar::add-line:horizontal:hover,
QScrollBar::add-line:horizontal:on {
    height: 12px;
    width: 12px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}
QScrollBar::add-line:vertical {
    margin: 3px 0px 3px 0px;
    height: 12px;
    width: 12px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:hover,
QScrollBar::add-line:vertical:on {
    height: 12px;
    width: 12px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
    margin: 0px 3px 0px 3px;
    height: 12px;
    width: 12px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {
    height: 12px;
    width: 12px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
    margin: 3px 0px 3px 0px;
    height: 12px;
    width: 12px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {
    height: 12px;
    width: 12px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}
QTabWidget::pane {
    border-top: 2px solid black;
    font-size: 10pt;
}
QTabWidget::tab-bar {
    left: 5px;
}
QTabBar::tab {
    border-style: outset;
    border-color: #f61;
    border-width: 3px;
    font-size: 10pt;
    color: #e9e7e6;
    padding-left: 8px;
    padding-right: 8px;
    margin-right: 2px;
    padding-bottom: 2px;
    background-color: #444;
}
QTabBar::tab:hover {
    color: #ffffff;
}
QTabBar::tab:selected, QTabBar::tab:last:selected {
    border-color: #e76500;
    font-style: bold;
    border-width: 2px;
    border-style: inset;
    color: #ffffff;
    padding-left: 8px;
    padding-right: 8px;
    padding-bottom: 0px;
    margin-right: 2px;
    background-color: #333;
}
QPushButton{
    margin-top: 3px;
    margin-bottom: 3px;
    margin-left: 8px;
    margin-right: 8px;
    border-style: outset;
    border-top-color: #e18133;
    border-right-color: #e67f2f;
    border-left-color: #e67f2f;
    border-bottom-color: #e67e22;
    border-radius: 8px;
    border-width: 3px;
    padding: 3px 4px 3px 4px;
    font-size: 12pt;
    font-weight: bold;
    color: #dedede;
    background-color: #111;
}
QPushButton:hover{
    border-style: inset;
    border-width: 3px;
    color: #efefefef;
    background-color: #000;
}
QPushButton:pressed{
    border-style: inset;
    border-bottom-width: 3px;
    color: #ffffff;
    background-color: #112;
}
QPushButton:disabled{
    border-style: solid;
    border-bottom-width: 1px;
    border-style: solid;
    color: #bbb;
    padding-bottom: 1px;
    background-color: #444;
}
QRadioButton {
    background-color: transparent;
    font-size: 12pt;
    border: transparent;
    padding-top: 2px;
    margin-top: 2px;
    margin-bottom: 2px;
    padding-bottom: 4px;
    color: #fff;
}
QRadioButton::indicator::unchecked {
    border: 1px inset #f73;
    border-radius: 6px;
    background-color:  #323232;
    width: 13px;
    height: 13px;
}
QRadioButton::indicator::unchecked:hover {
    border-radius: 5px;
    background-color:  #323232;
    width: 13px;
    height: 13px;
}
QRadioButton::indicator::checked {
    border: 1px inset #d73;
    border-radius: 5px;
    background-color: #ff5;
    width: 13px;
    height: 13px;
}
QCheckBox {
    color: #fff;
    padding: 4px;
    font-size: 12pt;
    border-color: transparent;
}
QCheckBox:disabled {
    color: #808086;
    padding: 6px;
}
QCheckBox::indicator:checked {
    height: 13px;
    width: 13px;
    border-style:solid;
    border-width: 2px;
    border-color: #e67e22;
    color: #a9b7c6;
    background-color: #d63d12;
}
QCheckBox::indicator:unchecked {
    height: 11px;
    width: 11px;
    border-style:solid;
    border-width: 2px;
    border-color: #e67e22;
    color: #a9b7c6;
    background-color: transparent;
}
QTreeWidget {
    border: 1px solid #f61;
    background-color: #5a5a5a;
    font-size: 9pt;
    color: #eeeeee;
}
QTreeWidget::item::selected {
    color: #FFFFFF;
    font-size: 9pt;
    border-color: transparent;
}
QTreeWidget::item::hover {
    color: #CFF8DC;
    border-color: transparent;
}
QTreeWidget::indicator::checked {
    background-color: #ffffff;
    border: 1px solid #536D79;
}
QTreeWidget::indicator::unchecked {
    background-color: #ffffff;
    border: 1px solid #536D79;
}
/* QTreeWidget QHeaderView::section {
    background-color: black;
    color: white;
}
QTreeWidget QHeaderView::section {
    border: 1px solid #e57e22;
    background-color: black;
    color: white;
}*/
QTreeWidget QProgressBar {
    color: black;
    background-color: #7a7a7a;
    border: 1px solid black;
    border-radius: 3px;
    margin-left: 2px;
    font-size: 12pt;
    font-weight: bold;
    margin-right: 2px;
    text-align: center;
}
QTreeWidget QProgressBar::chunk {
    background-color: #3ae1de;
    margin-left: .5px;
    margin-right: 0px;
    margin-top: 0px;
    margin-bottom: 0px;
    border-radius: 3px;
    width: 16px;
}
QTableWidget {
    color: #fff;
    border-color: #f71;
    border-width: 2px;
    border-style: ridge;
    border-radius: 4px;
    margin: 10px;
    font-size: 11pt;
    selection-background-color: #3a3a3a;
    gridline-color: #ac4a02;
}
QTableWidget::item:selected:hover {
    background-color: #7c7d7b;
}
QTableWidget::item:hover {
    background-color: #7c7d7b;
    border: dotted #ded 2px;
}
QTableWidget QTableCornerButton::section{
    background-color: black;
    border: 2px brown solid;
}
QHeaderView::section {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0,
                    y2: 1, stop:0 #54585b, stop:1 #393c3e);
    color: #CFF;
    padding: 1px 2px 1px 4px;
    border: 1px solid #323232;
    border-top-width: 0;
    font-size: 12pt;
    font-weight: bold;
    border-left-color: #5e6163;
    border-right-color: #2a2c2d;
}
QHeaderView::section:hover {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0,
                    y2: 1, stop:0 #64686b, stop:1 #494c4e);
    border-bottom-color: #424242;
}
QHeaderView::section:first {
    border-left-width: 0;
}
QHeaderView::section:last {
    border-right-width: 0;
}
QHeaderView::section:checked {
    color: #fff;
    background-color: #222;
}
QMenuBar {
    background-color: #322;
    padding: 2px;
    font-size: 9pt;
    margin-bottom: 2px;
    border-bottom: 2px solid #555555;
}
QMenuBar::item:pressed {
    background-color: #4b6eaf;
}
QMenuBar::item:selected:!pressed {
    background-color: #585b5d;
}
QMenu {
    border: 1px solid #2d2d2d;
    font-size: 8pt;
}
QMenu::item:disabled {
    color: #999999;
}
QMenu::item:selected {
    background-color: #4b6eaf;
}
QMenu::icon {
    border: 0px solid transparent;
    background-color: transparent;
}
QMenu::icon:checked {
    background-color: blue;
    border: 1px inset red;
    position: absolute;
    top: 1px;
    right: 1px;
    bottom: 1px;
    left: 1px;
}
QMenu::separator {
    height: 2px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0,
                    y2: 1, stop:0 #282a2b, stop:1 #45484b);
    margin: 0 1px;
}
QMenu::indicator {
    width: 13px;
    height: 13px;
    background-color: blue;
}
QDialog {
    background-color:#000000;
}
QLineEdit {
    padding: 4px;
    border-width: 1px;
    border-style: groove;
    margin-top: 3px;
    margin-bottom: 3px;
    font-size: 9pt;
    background-color: #19232D;
}
QLabel {
    padding: 2px;
    padding-top: 4px;
    padding-bottom: 4px;
    font-size: 10pt;
    font-weight: bold;
}
QStatusBar {
    border: 2px groove black;
    font-size: 8pt;
    color: #F00;
}
QComboBox {
    border: 2px solid #f73;
    padding: 1px 1px 1px 1px;
    font-size: 10pt;
    min-width: 2em;
}
QComboBox:on {
    padding-top: 3px;
    padding-left: 4px;
}
QComboBox::drop-down {
    width: 20px;
    background: #555;
    padding: 0px 2px 0px 2px;
    border-left-width: 2px;
    border-left-color: #311;
    border-left-style: outset;
}
QComboBox::down-arrow:on {
    top: 1px;
}
QToolBar {
    spacing: 8px;
}
QToolButton {
    font-size: 8pt;
    border-style: outset;
    border-color: #e67e22;
    border-width: 2px;
    border-radius: 8px;
    color: #FFF;
    padding: 2px;
    margin: 2px;
    background-color: #112;
}
QToolButton:hover {
    border-style: inset;
    margin-bottom: 1px;
    padding: 2px;
    background-color: #000;
}
*[editToolBar="true"] {
    background-color: #3a3a3a;
    spacing: 3px;
}
*[editToolBar="true"] QComboBox {
    background-color: #000;
    margin-left: 6px;
    border: 1px inset #f71;
    border-radius: 4px;
    font-size: 9pt;
    padding: 3px;
}
*[editToolBar="true"] QComboBox QLineEdit {
    margin: 0px;
    padding: 0px;
}
*[createButton="true"] {
    padding: 3px;
    margin: 0px;
    font-size: 9pt;
}
*[editCombo="true"] {
    font-size: 12pt;
    margin: 0px 0px 0px 0px;
    border-width: 1px;
    padding: 0px 0px 0px 0px;
    min-height: 19px;
}
*[editButton="true"] {
    margin-left: 2px;
    margin-right: 2px;
    font-size: 10pt;
    border-radius: 12px;
}
*[infoLine="true"] {
    background-color: transparent;
    color: #FFF;
    border-radius: 0px;
    border-width: 2px;
    font-size: 11pt;
    padding: 0px;
    margin: 0px;
    border-left-color: transparent;
    border-right-color: transparent;
    border-top-color: transparent;
}
QComboBox QAbstractItemView {
    border: 1px solid #444;
    selection-background-color: lightgray;
}
QComboBox::down-arrow {
    image: url(%s);
}
""" % arrow

light_theme = """
* {
    background-color: #E3E6F1;
    color: #000000;
    padding: 0px;
    margin: 0px;
    border-width: 0px;
    border-style: solid;
}
QMenu,
QTreeWidget,
QTreeWidget::item,
QTableWidget,
QTableWidget::item,
QHeaderView::section,
QTableView QTableCornerButton::section,
QLineEdit,
QTextEdit,
QComboBox,
QComboBox:editable,
QComboBox QAbstractItemView,
QProgressBar,
QScrollBar {
    border-width: 0px;
    border-style: solid;
    border-radius: 0px;
    padding: 0px;
    margin: 0px;
}
QHeaderView::section,
QTableView QTableCornerButton::section,
QLineEdit,
QTextEdit,
QComboBox:editable,
QComboBox,
QComboBox QAbstractItemView,
QProgressBar,
QScrollBar {
    border-color: #0CF;
    selection-background-color: #a6595b;
}
QLabel,
QLabel:disabled {
    border-width: 1px;
    background-color: transparent;
    padding: 0px;
    font-size: 8pt;
    border-color: transparent;
    selection-background-color: #ccc;
}
QMainWindow::separator {
    background: #0114fe;
    border-width: 0px;
}
QMainWindow::separator:hover {
    background: transparent;
}
QWidget {
    background-color: #E3E6F1;
    border-width: 0px;
}
QAbstractScrollArea {
    background-color: #CFC;
    border: 1px solid #0CF;
    border-radius: 4px;
    padding: 2px;
    color: #000;
}
QAbstractScrollArea:disabled {
    color: #E3E6F1;
}
QScrollArea QWidget QWidget:disabled {
    background-color: #E3E6F1;
}
QScrollBar:horizontal {
    height: 16px;
    margin: 2px 16px 2px 16px;
    border: 1px solid #ffc977;
    border-radius: 4px;
    background-color: #001c46;
}
QScrollBar:vertical {
    background-color: #25b511;
    width: 16px;
    margin: 16px 2px 16px 2px;
    border: 1px solid #eae64d;
    border-radius: 4px;
}
QScrollBar::handle:horizontal {
    background-color: #888;
    border: 1px solid #836727;
    border-radius: 4px;
    min-width: 8px;
}
QScrollBar::handle:horizontal:hover {
    background-color: #665997;
    border: #f9f046;
    border-radius: 4px;
    min-width: 8px;
}
QScrollBar::handle:horizontal:focus {
    border: 1px solid #1A72BB;
}
QScrollBar::handle:vertical {
    background-color: #336;
    border: 1px solid #eaf74a;
    min-height: 8px;
    border-radius: 4px;
}
QScrollBar::handle:vertical:hover {
    background-color: #E00F0F;
    border: #eae41a;
    border-radius: 4px;
    min-height: 8px;
}
QScrollBar::handle:vertical:focus {
    border: 1px solid #1A72BB;
}
QScrollBar::add-line:horizontal {
    margin: 0px 0px 0px 0px;
    height: 12px;
    width: 12px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}
QScrollBar::add-line:horizontal:hover,
QScrollBar::add-line:horizontal:on {
    height: 12px;
    width: 12px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}
QScrollBar::add-line:vertical {
    margin: 3px 0px 3px 0px;
    height: 12px;
    width: 12px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:hover,
QScrollBar::add-line:vertical:on {
    height: 12px;
    width: 12px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
    margin: 0px 3px 0px 3px;
    height: 12px;
    width: 12px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal:hover,
QScrollBar::sub-line:horizontal:on {
    height: 12px;
    width: 12px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
    margin: 3px 0px 3px 0px;
    height: 12px;
    width: 12px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:hover,
QScrollBar::sub-line:vertical:on {
    height: 12px;
    width: 12px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}
QTabWidget::pane {
    border-top-color: #667;
    border-top-width: 2px;
    border-top-style: outset;
    border-bottom-color: #444;
    border-bottom-width: 1px;

    font-size: 10pt;
}
QTabWidget::tab-bar {
    left: 5px;
}
QTabBar::tab {
    border-style: outset;
    border-color: #84378a;
    border-width: 3px;
    color: #000000;
    font-size: 10pt;
    font-weight: bold;
    padding-left: 8px;
    padding-right: 8px;
    margin-right: 2px;
    padding-bottom: 2px;
    background-color: #faf7e7;
}
QTabBar::tab:hover {
    color: #002288;
}
QTabBar::tab:selected, QTabBar::tab:last:selected {
    border-color: #883e00;
    border-bottom-color: transparent;
    font-style: bold;
    border-width: 2px;
    border-style: inset;
    color: #000000;
    padding-left: 8px;
    padding-right: 8px;
    font-size: 10pt;
    padding-bottom: 0px;
    margin-right: 2px;
    margin-bottom: -3px;
    background-color: #E3E6F1;
}
QPushButton{
    margin-top: 3px;
    margin-bottom: 3px;
    margin-left: 8px;
    margin-right: 8px;
    border-style: outset;
    border-top-color: #9b5317;
    border-right-color: #572c0b;
    border-left-color: #9f4f13;
    border-bottom-color: #5b310b;
    border-radius: 6px;
    border-width: 3px;
    padding-top: 4px;
    font-size: 12pt;
    padding-bottom: 4px;
    font-weight: bold;
    color: #000000;
    background-color: #8eC2fd;
}
QPushButton:hover{
    border-style: inset;
    border-width: 3px;
    color: #6b3232;
    background-color: #5bc6f9;
}
QPushButton:pressed {
    border-style: inset;
    border-bottom-width: 3px;
    color: #482622;
    background-color: #d0f5fd;
}
QPushButton:disabled {
    border-style: solid;
    border-bottom-width: 1px;
    border-style: solid;
    color: #011;
    padding-bottom: 1px;
    background-color: #CCC;
}
QRadioButton {
    background-color: transparent;
    border: transparent;
    padding-top: 2px;
    font-size: 12pt;
    margin-top: 2px;
    margin-bottom: 2px;
    padding-bottom: 4px;
    color: #005;
}
QRadioButton::indicator::unchecked {
    border: 2px inset #333;
    border-radius: 6px;
    background-color:  #ffe006;
    width: 13px;
    height: 13px;
}
QRadioButton::indicator::unchecked:hover {
    border-radius: 5px;
    background-color: #fdfd00;
    width: 13px;
    height: 13px;
}
QRadioButton::indicator::checked {
    border: 2px inset #8e5740;
    border-radius: 4px;
    background-color: #f00;
    width: 13px;
    height: 13px;
}
QCheckBox {
    color: #000;
    padding: 4px;
    font-size: 12pt;
    border-color: transparent;
}
QCheckBox:disabled {
    color: #808086;
    font-size: 9pt;
    padding: 6px;
}
QCheckBox::indicator:checked {
    height: 13px;
    width: 13px;
    border-style: solid;
    border-width: 2px;
    border-color: #111;
    color: #a9b7c6;
    background-color: #d63d12;
}
QCheckBox::indicator:unchecked {
    height: 11px;
    width: 11px;
    border-style: solid;
    border-width: 2px;
    border-color: #111;
    color: #a9b7c6;
    background-color: transparent;
}
QTreeWidget {
    border: 1px solid #f61;
    background-color: #cbfefc;
    font-size: 9pt;
    color: #000;
}
QTreeWidget::item::selected {
    font-size: 9pt;
    color: #000000;
    border-color: transparent;
}
QTreeWidget::item::hover {
    color: #3F3833;
    border-color: transparent;
}
QTreeWidget::indicator::checked {
    background-color: #000000;
    border: 1px solid #536D79;
}
QTreeWidget::indicator::unchecked {
    background-color: #000000;
    border: 1px solid #536D79;
}
/*QTreeWidget QHeaderView::section {
    background-color: #ffffff;
    color: #000;
}
QTreeWidget QHeaderView::section {
    border: 1px solid #027740;
    background-color: #fff;
    color: #000;
}*/
QTreeWidget QProgressBar {
    color: black;
    background-color: #323;
    font-size: 12pt;
    border: 1px solid black;
    border-radius: 3px;
    margin-left: 2px;
    margin-right: 2px;
    text-align: center;
}
QTreeWidget QProgressBar::chunk {
    background-color: #99F;
    margin-left: .5px;
    margin-right: 0px;
    margin-top: 0px;
    margin-bottom: 0px;
    border-radius: 3px;
    width: 16px;
}
QTableWidget {
    color: #000;
    font-size: 11pt;
    border-color: #f71;
    border-width: 2px;
    border-style: ridge;
    border-radius: 4px;
    margin: 10px;
    selection-background-color: #E07FE3;
    gridline-color: #ac4a02;
}
QTableWidget::item:selected:hover {
    background-color: #E66;
}
QTableWidget::item:hover {
    background-color: #CFF;
    border: dotted #ded 2px;
}
QTableWidget QTableCornerButton::section{
    background-color: black;
    border: 2px brown solid;
}
QHeaderView::section {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1, stop:0 #719bfd:1 #88d9ff);
    color: #001111;
    font-size: 12pt;
    border: 1px solid #287743;
    border-top-width: 0;
    border-left-color: #5e6163;
    border-right-color: #2a2c2d;
}
QHeaderView::section:hover {
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1, stop:0 #77AFFF, stop:1 #99dcee);
    border-bottom-color: #424242;
}
QHeaderView::section:first {
    border-left-width: 0;
}
QHeaderView::section:last {
    border-right-width: 0;
}
QHeaderView::section:checked {
    color: #000;
    background-color: #AFF;
}
QMenuBar {
    background-color: #CFF;
    font-size: 9pt;
    padding: 2px;
    margin-bottom: 2px;
    border-bottom: 2px solid #555555;
}
QMenuBar::item:pressed {
    background-color: #4b6eaf;
}
QMenuBar::item:selected:!pressed {
    background-color: #585b5d;
}
QMenu {
    font-size: 8pt;
    border: 1px solid #2d2d2d;
}
QMenu::item:disabled {
    color: #999999;
}
QMenu::item:selected {
    background-color: #4b6eaf;
}
QMenu::icon {
    border: 0px solid transparent;
    background-color: transparent;
}
QMenu::icon:checked {
    background-color: #AFF;
    border: 1px inset red;
    position: absolute;
    top: 1px;
    right: 1px;
    bottom: 1px;
    left: 1px;
}
QMenu::separator {
    height: 2px;
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1, stop:0 #282a2b, stop:1 #45484b);
    margin: 0 1px;
}
QMenu::indicator {
    width: 13px;
    height: 13px;
    background-color: #FAA;
}
QDialog {
    background-color: #CFE;
}
QLineEdit {
    padding: 4px;
    border-width: 1px;
    border-style: groove;
    margin-top: 3px;
    margin-bottom: 3px;
    font-size: 9pt;
    background-color: #CFC;
}
QLineEdit::read-only {
    background-color: #CFC;
}
QLabel {
    padding: 2px;
    padding-top: 4px;
    padding-bottom: 4px;
    font-size: 10pt;
    font-weight: bold;
}
QStatusBar {
    border: 1px groove #6f3375;
    background-color: #222;
    color: #F00;
    font-size: 8pt;
    border-radius: 3px;
    padding: 3px;
}

QComboBox {
    border: 2px solid #645a3c;
    background-color: #0EE;
    font-size: 10pt;
    padding: 1px 1px 1px 3px;
    min-width: 2em;
}
QComboBox:on {
    padding-top: 3px;
    padding-left: 4px;
}
QComboBox::drop-down {
    width: 20px;
    background: #0EE;
    padding: 0px 2px 0px 2px;
    border-left-width: 2px;
    border-left-color: #449;
    border-left-style: outset;
}
QComboBox::down-arrow:on {
    top: 1px;
    background-color: #555;
}
QToolButton {
    border-style: outset;
    font-size: 10pt;
    border-color: #111;
    border-width: 3px;
    border-radius: 8px;
    color: #000;
    padding: 5px;
    padding-top: 3px;
    background-color: #8ea2fd;
}
QToolButton:hover {
    border-style: inset;
    margin-bottom: 1px;
    padding: 4px;
    background-color: #5bc6f9;
}
*[createButton="true"] {
    padding: 3px;
    font-size: 9pt;
    margin: 0px;
}
*[editCombo="true"] {
    margin: 0px 0px 0px 0px;
    font-size: 12pt;
    border-width: 1px;
    padding: 0px 0px 0px 0px;
    min-height: 19px;
}
*[editButton="true"] {
    margin: 2px;
    padding: 2px;
    font-size: 11pt;
    border-radius: 12px;
}
*[infoLine="true"] {
    background-color: transparent;
    color: #000;
    font-size: 11pt;
    border-radius: 0px;
    border-width: 2px;
    padding: 0px;
    margin: 0px;
    border-left-color: transparent;
    border-right-color: transparent;
    border-top-color: transparent;
}
*[editToolBar="true"] {
    background-color:
}
QComboBox QAbstractItemView {
    border: 1px solid #DFF;
    selection-background-color: lightgray;
}
QComboBox::down-arrow {
    image: url(%s);
}
""" % arrow
