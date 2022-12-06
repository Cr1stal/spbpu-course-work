from PySide6.QtWidgets import QLabel, QWidget, QComboBox, QHBoxLayout

class GenderField(QComboBox):
    def __init__(self):
        super().__init__()

        self.addItems(['Male', 'Female'])
