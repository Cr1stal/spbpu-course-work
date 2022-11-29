from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSpinBox

class AgeField(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        self.label = QLabel('Age')
        self.layout.addWidget(self.label)

        self.field = QSpinBox()
        self.field.setRange(0, 150)
        self.layout.addWidget(self.field)

        self.setLayout(self.layout)
