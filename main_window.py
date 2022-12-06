from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout
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

        form = QFormLayout()

        # Gender field
        self.gender = GenderField()
        form.addRow(QLabel('Gender'), self.gender)

        # Age field
        self.age = AgeField()
        form.addRow(QLabel('Age'), self.age)

        # Hypertension field
        self.hypertension = HypertensionField()
        form.addRow(QLabel('Hypertension'), self.hypertension)

        # Heart Disease field
        self.heart_disease = HeartDiseaseField()
        form.addRow(QLabel('Heart Disease'), self.heart_disease)

        # Ever married field
        self.ever_married = EverMarriedField()
        form.addRow(QLabel('Ever married'), self.ever_married)

        # Work Type field
        self.work_type = WorkTypeField()
        form.addRow(QLabel('Work Type'), self.work_type)

        # Residence Type field
        self.residence_type = ResidenceTypeField()
        form.addRow(QLabel('Residence Type'), self.residence_type)

        # Average Glucose Level field
        self.average_glucose_level = AverageGlucoseLevelField()
        form.addRow(QLabel('Average Glucose Level'), self.average_glucose_level)

        # Body Mass Index field
        self.body_mass_index = BodyMassIndexField()
        form.addRow(QLabel('Body Mass Index'), self.body_mass_index)

        # Submit button
        form.addWidget(QPushButton('Predict'))

        widget = QWidget()
        widget.setLayout(form)
        self.setCentralWidget(widget)
