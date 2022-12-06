from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class EverMarriedField(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        self.label = QLabel('Ever Married')
        self.layout.addWidget(self.label)

        self.field = QComboBox()
        self.field.addItems(['Yes', 'No'])
        self.layout.addWidget(self.field)

        self.setLayout(self.layout)
