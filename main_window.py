from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox, QCheckBox, QDataWidgetMapper
from PySide6.QtSql import QSqlTableModel

from fields.gender_field import GenderField
from fields.age_field import AgeField
from fields.hypertension_field import HypertensionField
from fields.heart_disease_field import HeartDiseaseField
from fields.ever_married_field import EverMarriedField
from fields.work_type_field import WorkTypeField
from fields.residence_type_field import ResidenceTypeField
from fields.average_glucose_level_field import AverageGlucoseLevelField
from fields.body_mass_index_field import BodyMassIndexField

from client import Client

class MainWindow(QMainWindow):
    def __init__(self, db_arg):
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
        submit_btn = QPushButton('Predict')
        submit_btn.clicked.connect(self.submit_button_clicked)
        form.addWidget(submit_btn)

        self.model = QSqlTableModel(db=db_arg)

        self.mapper = QDataWidgetMapper()
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)

        self.mapper.addMapping(self.gender, 0)
        self.mapper.addMapping(self.age, 1)
        self.mapper.addMapping(self.hypertension, 2)
        self.mapper.addMapping(self.heart_disease, 3)
        self.mapper.addMapping(self.ever_married, 4)
        self.mapper.addMapping(self.work_type, 5)
        self.mapper.addMapping(self.residence_type, 6)
        self.mapper.addMapping(self.average_glucose_level, 7)
        self.mapper.addMapping(self.body_mass_index, 8)

        self.model.setTable("strokes_data")

        self.setMinimumSize(QSize(400, 400))
        self.setWindowTitle('Stroke prediction app')

        widget = QWidget()
        widget.setLayout(form)
        self.setCentralWidget(widget)

    def submit_button_clicked(self):
        self.mapper.submit()

        gender_value = (str(self.gender.currentText()) == 'Male')
        age_value = int(self.age.value())
        hypertension_value = self.hypertension.isChecked()
        heart_disease_value = self.heart_disease.isChecked()
        ever_married_value = (str(self.ever_married.currentText()) == 'Yes')
        work_type_value = str(self.work_type.currentText())
        residence_type_value = str(self.residence_type.currentText())
        average_glucose_level_value = int(self.average_glucose_level.value() * 100)
        body_mass_index_value = int(self.body_mass_index.value() * 100)

        client = Client()
        client.run(
                gender_arg=gender_value,
                age_arg=age_value,
                hypertension_arg=hypertension_value,
                heart_disease_arg=heart_disease_value,
                ever_married_arg=ever_married_value,
                work_type_arg=work_type_value,
                residence_type_arg=residence_type_value,
                average_glucose_level_arg=average_glucose_level_value,
                body_mass_index_arg=body_mass_index_value
                )

