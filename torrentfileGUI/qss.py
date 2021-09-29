"""*{
  color: {{secondaryTextColor}};
  font-family: {{font_family}};
  line-height: {{line_height}};
  font-size: {{font_size}};
  selection-background-color: {{primaryLightColor}};
  selection-color: {{primaryTextColor}};
}"""

"""*:focus {
   outline: none;
}"""

""".danger{
  color: {{danger}};
}"""

""".warning{
  color: {{warning}};
}"""

""".success{
  color: {{success}};
}"""

"""QWidget {
  background-color: {{secondaryDarkColor}};
}"""

"""QFrame {
  background-color: {{secondaryDarkColor}};
  border: 1px solid {{secondaryColor}};
  border-radius: 4px;
}"""

"""QSplitter {
  background-color: transparent;
  border: none
}"""

"""QStatusBar {
  color: {{secondaryTextColor}};
  background-color: {{secondaryLightColor|opacity(0.2)}};
  border-radius: 0px;
}"""

"""QScrollArea,
QStackedWidget,
QWidget > QToolBox,
QToolBox > QWidget,
QTabWidget > QWidget {
  border: none;
}"""

"""QTabWidget::pane {
  border: none;
}"""

"""QDateTimeEdit,
QSpinBox,
QDoubleSpinBox,
QTextEdit,
QLineEdit,
QPushButton {
  color: {{primaryColor}};
  background-color: {{secondaryDarkColor}};
  border: 2px solid {{primaryColor}};
  border-radius: 4px;
  padding: 8px 16px ;
  height: 18px;
}"""

"""QDateTimeEdit,
QSpinBox,
QDoubleSpinBox,
QTreeView,
QListView,
QLineEdit,
QComboBox {
  padding-left: 15px;
  border-radius: 0px;
  background-color: {{secondaryColor}};
  border-width: 0 0 2px 0;
  border-radius: 0px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
}"""

"""QPlainTextEdit {
  border-radius: 4px;
  padding: 8px 16px;
  background-color: {{secondaryDarkColor}};
  border: 1px solid {{secondaryColor}};
}"""

"""QDateTimeEdit:disabled,
QSpinBox:disabled,
QDoubleSpinBox:disabled,
QTextEdit:disabled,
QLineEdit:disabled {
  color: {{primaryColor|opacity(0.2)}};
  background-color: {{secondaryColor|opacity(0.75)}};
  border: 2px solid {{primaryColor|opacity(0.2)}};
  border-width: 0 0 2px 0;
  padding: 8px 16px ;
  border-radius: 0px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
}"""

"""QTextEdit {
  padding: 8px;
  border-radius: 4px;
  background-color: {{secondaryColor}};
}"""

"""QDateTimeEdit:disabled,
QSpinBox:disabled,
QDoubleSpinBox:disabled,
QTextEdit:disabled,
QLineEdit:disabled {
  color: {{primaryColor|opacity(0.2)}};
  background-color: {{secondaryColor|opacity(0.75)}};
  border: 2px solid {{primaryColor|opacity(0.2)}};
  border-width: 0 0 2px 0;
}"""

"""QComboBox {
  color: {{primaryColor}};
  border: 1px solid {{primaryColor}};
  border-width: 0 0 2px 0;
  background-color: {{secondaryColor}};
  border-radius: 0px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  height: 36px;
}"""

"""QComboBox:disabled {
  color: {{primaryColor|opacity(0.2)}};
  background-color: {{secondaryColor|opacity(0.75)}};
  border-bottom: 2px solid {{primaryColor|opacity(0.2)}};
}"""

"""QComboBox::drop-down {
  border: none;
  color: {{primaryColor}};
  width: 20px;
}"""

"""QComboBox::down-arrow {
  image: url(icon:/primary/downarrow.svg);
  margin-right: 10px;
}"""

"""QComboBox::down-arrow:disabled {
  image: url(icon:/disabled/downarrow.svg);
  margin-right: 10px;
}"""

"""QComboBox QAbstractItemView {
  background-color: {{secondaryColor}};
  border: 2px solid {{secondaryLightColor}};
  border-radius: 4px;
}"""

"""QComboBox[frame='false'] {
  color: {{primaryColor}};
  background-color: transparent;
  border: 1px solid transparent;
}
QComboBox[frame='false']:disabled {
  color: {{primaryColor|opacity(0.2)}};
}"""

"""QDateTimeEdit::up-button,
QDoubleSpinBox::up-button,
QSpinBox::up-button {
  subcontrol-origin: border;
  subcontrol-position: top right;
  width: 20px;
  image: url(icon:/primary/uparrow.svg);
  border-width: 0px;
  margin-right: 5px;
}"""

"""QDateTimeEdit::up-button:disabled,
QDoubleSpinBox::up-button:disabled,
QSpinBox::up-button:disabled {
  image: url(icon:/disabled/uparrow.svg);
}"""

"""QDateTimeEdit::down-button,
QDoubleSpinBox::down-button,
QSpinBox::down-button {
  subcontrol-origin: border;
  subcontrol-position: bottom right;
  width: 20px;
  image: url(icon:/primary/downarrow.svg);
  border-width: 0px;
  border-top-width: 0;
  margin-right: 5px;
}"""

"""QDateTimeEdit::down-button:disabled,
QDoubleSpinBox::down-button:disabled,
QSpinBox::down-button:disabled {
  image: url(icon:/disabled/downarrow.svg);
}"""

"""QPushButton {
  text-transform: uppercase;
  margin: 0px;
  padding: 0px 16px;
  height: 34px;
  min-height: 34px;
  max-height: 34px;
  font-weight: bold;
}"""

"""QPushButton:checked,
QPushButton:pressed {
  color: {{secondaryDarkColor}};
  background-color: {{primaryColor}};
}"""

"""QPushButton:flat {
  padding: 5px;
  margin: 0px;
  color: {{primaryColor}};
  border: none;
  background-color: transparent;
}"""

"""QPushButton:flat:hover {
  background-color: {{primaryColor|opacity(0.2)}};
}"""

"""QPushButton:flat:pressed,
QPushButton:flat:checked {
  background-color: {{primaryColor|opacity(0.1)}};
}"""

"""QPushButton:disabled,
QPushButton:flat:disabled {
  color: {{secondaryLightColor|opacity(0.75)}};
  background-color: transparent;
  border-color:  {{secondaryColor}};
}"""

"""QPushButton:disabled {
  border: 2px solid {{secondaryLightColor|opacity(0.75)}};
}"""

"""QPushButton:checked:disabled {
  color: {{secondaryColor}};
  background-color: {{secondaryLightColor}};
  border-color:  {{secondaryLightColor}};
}"""

"""QTabBar{
  text-transform: uppercase;
  font-weight: bold;
}"""

"""QTabBar::tab {
  color: {{secondaryTextColor}};
  border: 0px;
}"""

"""QTabBar::tab:bottom,
QTabBar::tab:top{
  padding: 0 15px;
  height: 30px;
}"""

"""QTabBar::tab:left,
QTabBar::tab:right{
  padding: 15px 0;
  width: 30px;
}"""

"""QTabBar::tab:top:selected,
QTabBar::tab:top:hover {
  color: {{primaryColor}};
  border-bottom: 2px solid {{primaryColor}};
}"""

"""QTabBar::tab:bottom:selected,
QTabBar::tab:bottom:hover {
  color: {{primaryColor}};
  border-top: 2px solid {{primaryColor}};
}"""

"""QTabBar::tab:right:selected,
QTabBar::tab:right:hover {
  color: {{primaryColor}};
  border-left: 2px solid {{primaryColor}};
}"""

"""QTabBar::tab:left:selected,
QTabBar::tab:left:hover {
  color: {{primaryColor}};
  border-right: 2px solid {{primaryColor}};
}"""

"""QTabBar QToolButton:hover,
QTabBar QToolButton {
  border: 20px;
  background-color: {{secondaryDarkColor}};
}"""

"""QTabBar QToolButton::up-arrow {
  image: url(icon:/disabled/uparrow2.svg);
}"""

"""QTabBar QToolButton::up-arrow:hover {
  image: url(icon:/primary/uparrow2.svg);
}"""

"""QTabBar QToolButton::down-arrow {
  image: url(icon:/disabled/downarrow2.svg);
}"""

"""QTabBar QToolButton::down-arrow:hover {
  image: url(icon:/primary/downarrow2.svg);
}"""

"""QTabBar QToolButton::right-arrow {
  image: url(icon:/primary/rightarrow2.svg);
}"""

"""QTabBar QToolButton::right-arrow:hover {
  image: url(icon:/disabled/rightarrow2.svg);
}"""

"""QTabBar QToolButton::left-arrow {
  image: url(icon:/primary/leftarrow2.svg);
}"""

"""QTabBar QToolButton::left-arrow:hover {
  image: url(icon:/disabled/leftarrow2.svg);
}"""

"""QTabBar::close-button {
  image: url(icon:/disabled/tab_close.svg);
}"""

"""QTabBar::close-button:hover {
  image: url(icon:/primary/tab_close.svg);
}"""

"""QGroupBox {
  background-color: {{secondaryColor}};
  border-radius: 4px;
  padding: 15px;
  padding-top: 30px;
  line-height: 13px;
  text-transform: uppercase;
}"""

"""QGroupBox::title {
  color: {{secondaryTextColor|opacity(0.4)}};
  subcontrol-origin: margin;
  subcontrol-position: top left;
  padding: 0 15px;
  margin-top: 10px;
  background-color: {{secondaryDarkColor}};
  background-color: transparent;
  height: 20px;
}"""

"""QRadioButton,
QCheckBox {
  spacing: 10px;
  color: {{secondaryTextColor}};
  line-height: 14px;
  height: 30px;
  background-color: transparent;
  spacing: 5px;
}"""

"""QRadioButton:disabled,
QCheckBox:disabled {
  color: {{secondaryTextColor|opacity(0.3)}};
}"""

"""QMenu::indicator,
QListView::indicator,
QTableWidget::indicator,
QRadioButton::indicator,
QCheckBox::indicator {
  width: 24px;
  height: 24px;
  border-radius: 4px;
 }"""

"""QListView::indicator:checked,
QListView::indicator:checked:selected,
QListView::indicator:checked:focus {
  image: url(icon:/primary/checklist.svg);
}"""

"""QListView::indicator:checked:selected:active {
  image: url(icon:/primary/checklist_invert.svg);
}"""

"""QListView::indicator:checked:disabled {
  image: url(icon:/disabled/checklist.svg);
}"""

"""QListView::indicator:indeterminate,
QListView::indicator:indeterminate:selected,
QListView::indicator:indeterminate:focus {
  image: url(icon:/primary/checklist_indeterminate.svg);
}"""

"""QListView::indicator:indeterminate:selected:active {
  image: url(icon:/primary/checklist_indeterminate_invert.svg);
}"""

"""QListView::indicator:indeterminate:disabled {
  image: url(icon:/disabled/checklist_indeterminate.svg);
}"""

"""QTableView::indicator:enabled:checked,
QTableView::indicator:enabled:checked:selected,
QTableView::indicator:enabled:checked:focus {
  image: url(icon:/primary/checkbox_checked.svg);
}"""

"""QTableView::indicator:checked:selected:active {
  image: url(icon:/primary/checkbox_checked_invert.svg);
}"""

"""QTableView::indicator:disabled:checked,
QTableView::indicator:disabled:checked:selected,
QTableView::indicator:disabled:checked:focus {
  image: url(icon:/disabled/checkbox_checked.svg);
}"""

"""QTableView::indicator:enabled:unchecked,
QTableView::indicator:enabled:unchecked:selected,
QTableView::indicator:enabled:unchecked:focus {
  image: url(icon:/primary/checkbox_unchecked.svg);
}"""

"""QTableView::indicator:unchecked:selected:active {
  image: url(icon:/primary/checkbox_unchecked_invert.svg);
}"""

"""QTableView::indicator:disabled:unchecked,
QTableView::indicator:disabled:unchecked:selected,
QTableView::indicator:disabled:unchecked:focus {
  image: url(icon:/disabled/checkbox_unchecked.svg);
}"""

"""QTableView::indicator:enabled:indeterminate,
QTableView::indicator:enabled:indeterminate:selected,
QTableView::indicator:enabled:indeterminate:focus {
  image: url(icon:/primary/checkbox_indeterminate.svg);
}"""

"""QTableView::indicator:indeterminate:selected:active {
  image: url(icon:/primary/checkbox_indeterminate_invert.svg);
}"""

"""QTableView::indicator:disabled:indeterminate,
QTableView::indicator:disabled:indeterminate:selected,
QTableView::indicator:disabled:indeterminate:focus {
  image: url(icon:/disabled/checkbox_indeterminate.svg);
}"""

"""QCheckBox::indicator:checked {
  image: url(icon:/primary/checkbox_checked.svg);
}"""

"""QCheckBox::indicator:unchecked {
  image: url(icon:/primary/checkbox_unchecked.svg);
}"""

"""QCheckBox::indicator:indeterminate {
  image: url(icon:/primary/checkbox_indeterminate.svg);
}"""

"""QCheckBox::indicator:checked:disabled {
  image: url(icon:/disabled/checkbox_checked.svg);
}"""

"""QCheckBox::indicator:unchecked:disabled {
  image: url(icon:/disabled/checkbox_unchecked.svg);
}"""

"""QCheckBox::indicator:indeterminate:disabled {
  image: url(icon:/disabled/checkbox_indeterminate.svg);
}"""

"""QRadioButton::indicator:checked {
  image: url(icon:/primary/radiobutton_checked.svg);
}"""

"""QRadioButton::indicator:unchecked {
  image: url(icon:/primary/radiobutton_unchecked.svg);
}"""

"""QRadioButton::indicator:checked:disabled {
  image: url(icon:/disabled/radiobutton_checked.svg);
}"""

"""QRadioButton::indicator:unchecked:disabled {
  image: url(icon:/disabled/radiobutton_unchecked.svg);
}"""

"""QDockWidget {
  color: {{secondaryTextColor}};
  text-transform: uppercase;
  border: 2px solid {{secondaryColor}};
  titlebar-close-icon: url(icon:/primary/close.svg);
  titlebar-normal-icon: url(icon:/primary/float.svg);
  border-radius: 4px;
}"""

"""QDockWidget::title {
  text-align: left;
  padding-left: 35px;
  padding: 3px;
  margin-top: 4px;
}"""

"""QComboBox::indicator:checked {
  image: url(icon:/primary/checklist.svg);
}"""

"""QComboBox::indicator:checked:selected {
  image: url(icon:/primary/checklist_invert.svg);
}"""

"""QComboBox::item,
QCalendarWidget QMenu::item,
QMenu::item {
  height: 26px;
  border: 8px solid transparent;
  color: {{secondaryTextColor}};
}"""

"""QCalendarWidget QMenu::item,
QMenu::item {
  padding: 0px 25px 0px 20px;
}"""

"""QComboBox::item:selected,
QCalendarWidget QMenu::item:selected,
QMenu::item:selected {
  color: {{primaryTextColor}};
  background-color: {{primaryLightColor}};
  border-radius: 4px;
}"""

"""QComboBox::item:disabled,
QCalendarWidget QMenu::item:disabled,
QMenu::item:disabled {
  color: {{secondaryTextColor|opacity(0.3)}};
}"""

"""QCalendarWidget QMenu,
QMenu {
  background-color: {{secondaryColor}};
  border: 2px solid {{secondaryLightColor}};
  border-radius: 4px;
  margin-top: 3px;
}"""

"""QMenu::separator {
  height: 2px;
  background-color: {{secondaryLightColor}};
  margin-left: 2px;
  margin-right: 2px;
}"""

"""QMenu::right-arrow{
  image: url(icon:/primary/rightarrow.svg);
  width: 15px;
  height: 15px;
}"""

"""QMenu::right-arrow:selected{
  image: url(icon:/disabled/rightarrow.svg);
}"""

"""QMenu::indicator:non-exclusive:unchecked {
  image: url(icon:/primary/checkbox_unchecked.svg);
}"""

"""QMenu::indicator:non-exclusive:unchecked:selected {
  image: url(icon:/primary/checkbox_unchecked_invert.svg);
}"""

"""QMenu::indicator:non-exclusive:checked {
  image: url(icon:/primary/checkbox_checked.svg);
}"""

"""QMenu::indicator:non-exclusive:checked:selected {
  image: url(icon:/primary/checkbox_checked_invert.svg);
}"""

"""QMenu::indicator:exclusive:unchecked {
  image: url(icon:/primary/radiobutton_unchecked.svg);
}"""

"""QMenu::indicator:exclusive:unchecked:selected {
  image: url(icon:/primary/radiobutton_unchecked_invert.svg);
}"""

"""QMenu::indicator:exclusive:checked {
  image: url(icon:/primary/radiobutton_checked.svg);
}"""

"""QMenu::indicator:exclusive:checked:selected {
  image: url(icon:/primary/radiobutton_checked_invert.svg);
}"""

"""QMenuBar {
  background-color: {{secondaryColor}};
  color: {{secondaryTextColor}};
}"""

"""QMenuBar::item {
  height: 30px;
  padding: 8px;
  background-color: transparent;
  color: {{secondaryTextColor}};
}"""

"""QMenuBar::item:selected,
QMenuBar::item:pressed {
  color: {{primaryTextColor}};
  background-color: {{primaryLightColor}};
}"""

"""QToolBox::tab {
  background-color: {{secondaryColor}};
  color: {{secondaryTextColor}};
  padding-left: 15px;
  text-transform: uppercase;
  border-radius: 4px;
}"""

"""QToolBox::tab:hover {
  background-color: {{primaryColor|opacity(0.2)}};
}"""

"""QProgressBar {
  border-radius: 0;
  background-color: {{secondaryLightColor}};
  text-align: center;
  color: transparent;
}"""

"""QProgressBar::chunk {
  background-color: {{primaryColor}};
}"""

"""QScrollBar:horizontal {
  border: 0;
  background: {{secondaryColor}};
  height: 8px;
}"""

"""QScrollBar:vertical {
  border: 0;
  background: {{secondaryColor}};
  width: 8px;
}"""

"""QScrollBar::handle:horizontal {
  background: {{secondaryLightColor}};
  min-width: 20px;
}"""

"""QScrollBar::handle:vertical {
  background: {{secondaryLightColor}};
  min-height: 20px;
}"""

"""QScrollBar::handle:vertical:hover,
QScrollBar::handle:horizontal:hover {
  background: {{primaryColor}};
}"""

"""QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical,
QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
  border: 0;
  background: transparent;
  width: 0px;
  height: 0px;
}"""

"""QSlider:horizontal {
  min-height: 20px;
  max-height: 20px;
}"""

"""QSlider:vertical {
  min-width: 20px;
  max-width: 20px;
}"""

"""QSlider::groove:horizontal {
  height: 4px;
  background: #393939;
  margin: 0 10px;
}"""

"""QSlider::groove:vertical {
  width: 4px;
  background: #393939;
  margin: 10px 0;
  border-radius: 20px;
}"""

"""QSlider::handle:horizontal {
  image: url(icon:/primary/slider.svg);
  width: 20px;
  height: 20px;
  margin: -20px -10px;
}"""

"""QSlider::handle:vertical {
  image: url(icon:/primary/slider.svg);
  border-radius: 20px;
  width: 20px;
  height: 20px;
  margin: -10px -20px;
}"""

"""QSlider::add-page {
background: {{secondaryColor}};
}"""

"""QSlider::sub-page {
background: {{primaryColor}};
}"""

"""QLabel {
  border: none;
  background: transparent;
  color: {{secondaryTextColor}}
}"""

"""QLabel:disabled {
  color: {{secondaryTextColor|opacity(0.2)}}
}"""

"""QFrame[frameShape="4"] {
    border-width: 1px 0 0 0;
    background: none;
}"""

"""QFrame[frameShape="5"] {
    border-width: 0 1px 0 0;
    background: none;
}"""

"""QFrame[frameShape="4"],
QFrame[frameShape="5"] {
  border-color: {{secondaryLightColor}};
}"""

"""QToolBar {
  background: {{secondaryDarkColor}};
  border: 0px solid;
}"""

"""QToolBar:horizontal {
  border-bottom: 1px solid {{secondaryLightColor}};
}"""

"""QToolBar:vertical {
  border-right: 1px solid {{secondaryLightColor}};
}"""

"""QToolBar::handle:horizontal {
  image: url(icon:/primary/toolbar-handle-horizontal.svg);
}"""

"""QToolBar::handle:vertical {
  image: url(icon:/primary/toolbar-handle-vertical.svg);
}"""

"""QToolBar::separator:horizontal {
  border-right: 1px solid {{secondaryLightColor}};
  border-left: 1px solid {{secondaryLightColor}};
  width: 1px;
}"""

"""QToolBar::separator:vertical {
  border-top: 1px solid {{secondaryLightColor}};
  border-bottom: 1px solid {{secondaryLightColor}};
  height: 1px;
}"""

"""QToolButton {
  background: {{secondaryDarkColor}};
  border: 0px;
  height: 40px;
  margin: 0px;
  padding: 5px;
  border-right: 10px solid {{secondaryDarkColor}};
  border-left: 10px solid {{secondaryDarkColor}};
}"""

"""QToolButton:hover {
  background: {{secondaryLightColor}};
  border-right: 10px solid {{secondaryLightColor}};
  border-left: 10px solid {{secondaryLightColor}};
}"""

"""QToolButton:pressed {
  background: {{secondaryColor}};
  border-right: 10px solid {{secondaryColor}};
  border-left: 10px solid {{secondaryColor}};
}"""

"""QToolButton:checked {
  background: {{secondaryLightColor}};
  border-left: 10px solid {{secondaryLightColor}};
  border-right: 10px solid {{primaryColor}};
}"""

"""QTableView {
  background-color: {{secondaryDarkColor}};
  border: 1px solid {{secondaryColor}};
  border-radius: 4px;
}"""

"""QTreeView,
QListView {
  border-radius: 4px;
  padding: 5px;
  margin: 0px;
}"""

"""QTableView::item,
QTreeView::item,
QListView::item {
  padding: 5px;
  min-height: 25px;
  color: {{secondaryTextColor}};
  selection-color: {{secondaryTextColor}};
}"""


"""QTableView:item:selected,
QTreeView::item:selected,
QListView::item:selected {
  background-color: {{primaryColor|opacity(0.2)}};
  selection-background-color: {{primaryColor|opacity(0.2)}};
  color: {{secondaryTextColor}};
  selection-color: {{secondaryTextColor}};
}"""

"""QTableView:item:selected:focus,
QTreeView::item:selected:focus,
QListView::item:selected:focus {
  background-color: {{primaryColor}};
  selection-background-color: {{primaryColor}};
  color: {{primaryTextColor}};
  selection-color: {{primaryTextColor}};
}"""

"""QTableView {
  selection-background-color: {{primaryColor|opacity(0.2)}};
}"""

"""QTableView:focus {
  selection-background-color: {{primaryColor}};
}"""

"""QTableView::item:disabled {
  color: {{secondaryTextColor|opacity(0.3)}};
  selection-color: {{secondaryTextColor|opacity(0.3)}};
  background-color: {{secondaryColor}};
  selection-background-color: {{secondaryColor}};
}"""

"""QTreeView::branch{
  background-color: {{secondaryColor}};
}"""

"""QTreeView::branch:closed:has-children:has-siblings,
QTreeView::branch:closed:has-children:!has-siblings {
  image: url(icon:/primary/branch-closed.svg);
}"""

"""QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings {
  image: url(icon:/primary/branch-open.svg);
}"""

"""QTreeView::branch:has-siblings:!adjoins-item {
  border-image: url(icon:/disabled/vline.svg) 0;
}"""

"""QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(icon:/disabled/branch-more.svg) 0;
}"""

"""QTreeView::branch:!has-children:!has-siblings:adjoins-item,
QTreeView::branch:has-children:!has-siblings:adjoins-item {
    border-image: url(icon:/disabled/branch-end.svg) 0;
}"""

"""QTreeView QHeaderView::section {
  border: none;
}"""


"""QPushButton.danger {
  border-color: {{danger}};
  color: {{danger}};
}"""

"""QPushButton.danger:checked,
QPushButton.danger:pressed {
  color: {{secondaryDarkColor}};
  background-color: {{danger}};
}"""

"""QPushButton.warning{
  border-color: {{warning}};
  color: {{warning}};
}"""

"""QPushButton.warning:checked,
QPushButton.warning:pressed {
  color: {{secondaryDarkColor}};
  background-color: {{warning}};
}"""

"""QPushButton.success {
  border-color: {{success}};
  color: {{success}};
}"""

"""QPushButton.success:checked,
QPushButton.success:pressed {
  color: {{secondaryDarkColor}};
  background-color: {{success}};
}"""

"""QPushButton.danger:flat:hover {
  background-color: {{danger|opacity(0.2)}};
}"""

"""QPushButton.danger:flat:pressed,
QPushButton.danger:flat:checked {
  background-color: {{danger|opacity(0.1)}};
  color: {{danger}};
}"""

"""QPushButton.warning:flat:hover {
  background-color: {{warning|opacity(0.2)}};
}"""

"""QPushButton.warning:flat:pressed,
QPushButton.warning:flat:checked {
  background-color: {{warning|opacity(0.1)}};
  color: {{warning}};
}"""

"""QPushButton.success:flat:hover {
  background-color: {{success|opacity(0.2)}};
}"""

"""QPushButton.success:flat:pressed,
QPushButton.success:flat:checked {
  background-color: {{success|opacity(0.1)}};
  color: {{success}};
}"""

"""QTableCornerButton::section {
  background-color: {{secondaryColor}};
  border-radius: 0px;
  border-right: 1px solid;
  border-bottom: 1px solid;
  border-color: {{secondaryDarkColor}};
}"""

"""QTableView {
  alternate-background-color: {{secondaryColor|opacity(0.7)}};
}"""

"""QHeaderView {
  border: none;
}"""

"""QHeaderView::section {
  color: {{secondaryTextColor|opacity(0.7)}};
  text-transform: uppercase;
  background-color: {{secondaryColor}};
  padding: 0 20px;
  height: 35px;
  border-radius: 0px;
  border-right: 1px solid;
  border-bottom: 1px solid;
  border-color: {{secondaryDarkColor}};
}"""

"""
""""""QLCDNumber {
  color: {{primaryColor}};
  background-color:{{primaryColor|opacity(0.1)}};
  border: 1px solid {{primaryColor|opacity(0.3)}};
  border-radius: 4px;
}"""

"""#qt_calendar_prevmonth {
  qproperty-icon: url(icon:/primary/leftarrow.svg);
}"""

"""#qt_calendar_nextmonth {
  qproperty-icon: url(icon:/primary/rightarrow.svg);
}"""

"""QTreeView QLineEdit,
QTableView QLineEdit,
QListView QLineEdit {
  color: {{secondaryTextColor}};
  background-color: {{secondaryColor}};
  border: 1px solid unset;
  border-radius: unset;
  padding: unset;
  padding-left: unset;
  height: unset;
  border-width: unset;
  border-top-left-radius: unset;
  border-top-right-radius: unset;
}"""

"""QToolTip {
  padding: 5px;
  border: 1px solid {{secondaryDarkColor}};
  border-radius: 4px;
  color: {{secondaryTextColor}};
  background-color: {{secondaryLightColor}};
}"""

"""QDialog QToolButton,
QDialog QToolButton:hover,
QDialog QToolButton:pressed,
QDialog QToolButton:checked {
  background-color: unset;
  border: 0px;
  height: unset;
  margin: unset;
  padding: unset;
  border-right: unset;
  border-left: unset;
}"""

"""QMainWindow::separator:vertical,
QSplitter::handle:horizontal {
  image: url(icon:/primary/splitter-horizontal.svg);
}
"""
"""QMainWindow::separator:horizontal,
QSplitter::handle:vertical {
  image: url(icon:/primary/splitter-vertical.svg);
}"""

"""QSizeGrip {
  image: url(icon:/primary/sizegrip.svg);
  background-color: transparent;
  width: 16px;
  height: 16px;
}"""
