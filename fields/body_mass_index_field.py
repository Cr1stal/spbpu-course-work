from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QDoubleSpinBox

class BodyMassIndexField(QDoubleSpinBox):
    def __init__(self):
        super().__init__()

        self.setRange(0, 50)
        self.setSingleStep(0.1)
