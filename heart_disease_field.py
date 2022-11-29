from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QCheckBox

class HeartDiseaseField(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()

        self.label = QLabel('Heart Disease')
        self.layout.addWidget(self.label)

        self.field = QCheckBox()
        self.layout.addWidget(self.field)

        self.setLayout(self.layout)
