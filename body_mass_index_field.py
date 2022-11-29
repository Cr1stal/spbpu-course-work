from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QDoubleSpinBox

class BodyMassIndexField(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        self.label = QLabel('Body Mass Index')
        self.layout.addWidget(self.label)

        self.field = QDoubleSpinBox()
        self.field.setRange(0, 50)
        self.field.setSingleStep(0.1)
        self.layout.addWidget(self.field)

        self.setLayout(self.layout)
