from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QCheckBox

class HypertensionField(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()

        self.label = QLabel('Hypertension')
        self.layout.addWidget(self.label)

        self.field = QCheckBox()
        self.layout.addWidget(self.field)

        self.setLayout(self.layout)
