from PySide6.QtWidgets import QLabel, QWidget, QComboBox, QHBoxLayout

class GenderField(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        self.label = QLabel('Gender')
        self.layout.addWidget(self.label)

        self.field = QComboBox()
        self.field.addItems(['Male', 'Female'])
        self.layout.addWidget(self.field)

        self.setLayout(self.layout)
