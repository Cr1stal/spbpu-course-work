from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class ResidenceTypeField(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        self.label = QLabel('Residence Type')
        self.layout.addWidget(self.label)

        self.field = QComboBox()
        self.field.addItems(['Urban', 'Rural'])
        self.layout.addWidget(self.field)

        self.setLayout(self.layout)
