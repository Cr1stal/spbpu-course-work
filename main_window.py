from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox, QCheckBox

from fields.gender_field import GenderField
from fields.age_field import AgeField
from fields.hypertension_field import HypertensionField
from fields.heart_disease_field import HeartDiseaseField
from fields.ever_married_field import EverMarriedField
from fields.work_type_field import WorkTypeField
from fields.residence_type_field import ResidenceTypeField
from fields.average_glucose_level_field import AverageGlucoseLevelField
from fields.body_mass_index_field import BodyMassIndexField

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.names = [
                'Gender',
                'Age',
                'Hypertension',
                'Heart Disease',
                'Ever Married',
                'Work Type',
                'Residence Type',
                'Average Glucose Level',
                'Body Mass Index'
                ]

        layout = QVBoxLayout()

        # Gender field
        widget = GenderField()
        layout.addWidget(widget)

        # Age field
        widget = AgeField()
        layout.addWidget(widget)

        # Hypertension field
        widget = HypertensionField()
        layout.addWidget(widget)

        # Heart Disease field
        widget = HeartDiseaseField()
        layout.addWidget(widget)

        # Ever married field
        widget = EverMarriedField()
        layout.addWidget(widget)

        # Work Type field
        widget = WorkTypeField()
        layout.addWidget(widget)

        # Residence Type field
        widget = ResidenceTypeField()
        layout.addWidget(widget)

        # Average Glucose Level field
        widget = AverageGlucoseLevelField()
        layout.addWidget(widget)

        # Body Mass Index field
        widget = BodyMassIndexField()
        layout.addWidget(widget)

        # Submit button
        layout.addWidget(QPushButton('Predict'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
