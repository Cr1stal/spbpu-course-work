from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSpinBox

class AgeField(QSpinBox):
    def __init__(self):
        super().__init__()

        self.setRange(0, 150)
