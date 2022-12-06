from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class EverMarriedField(QComboBox):
    def __init__(self):
        super().__init__()

        self.addItems(['Yes', 'No'])
