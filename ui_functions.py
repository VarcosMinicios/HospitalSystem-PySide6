from Objects.DataBase import DataBase, PatientRegister, HospitalizationInfo


class UiFunctions:
    def __init__(self):
        pass

    @staticmethod
    def hospitalization(parent):

        DataBase.insertHospitalizations(
            'hospitalizations', HospitalizationInfo(
                DataBase.getIdByCpf(parent.ui.firstLineCpf.text()), parent.ui.firstLineCpf.text(), parent.ui.firstLinePatientName.text(), 
                parent.ui.firstLineTreatDate.text(), parent.ui.firstBoxAdmission.currentText(), 
                parent.ui.firstBoxDoctor.currentText().split(' - ')[0], parent.ui.firstBoxDoctor.currentText().split(' - ')[1], 
                parent.ui.firstBoxClinic.currentText(), parent.ui.firstBoxBed.currentText(), parent.ui.firstBoxDependency.currentText(), 
                parent.ui.firstLineTreatHour.text(), parent.ui.firstLineResponsible.text()
            )
        )
    
    @staticmethod
    def register(parent):

        DataBase.insertOrReplacePatient(
            'patient_register', PatientRegister(
                parent.ui.firstLineCpf.text(), parent.ui.firstLinePatientName.text(), parent.ui.firstLineBornDay.text(), 
                parent.ui.firstLineProfession.text(), parent.ui.firstLineSusCard.text(), parent.ui.firstLineRG.text(), 
                parent.ui.firstLineMotherName.text(), parent.ui.firstLineFatherName.text(), parent.ui.firstLinePhoneOne, 
                parent.ui.firstLinePhoneTwo.text(), parent.ui.firstLineCity.text(), parent.ui.firstLineAdress.text(), parent.ui.firstLineUf.text(),
                parent.ui.firstLineDistrict.text(), parent.ui.firstLineCep.text(), parent.ui.firstBoxUrbanZone.currentText(), 
                parent.ui.firstBoxSex.currentText(), parent.ui.firstBoxSkinColor.currentText(), parent.ui.firstBoxCivilStats.currentText()
            )
        )

    @staticmethod
    def registerAndHospitalize(parent):

        DataBase.insertOrReplacePatient(
            'patient_register', PatientRegister(
                parent.ui.firstLineCpf.text(), parent.ui.firstLinePatientName.text(), parent.ui.firstLineBornDay.text(), 
                parent.ui.firstLineProfession.text(), parent.ui.firstLineSusCard.text(), parent.ui.firstLineRG.text(), 
                parent.ui.firstLineMotherName.text(), parent.ui.firstLineFatherName.text(), parent.ui.firstLinePhoneOne, 
                parent.ui.firstLinePhoneTwo.text(), parent.ui.firstLineCity.text(), parent.ui.firstLineAdress.text(), parent.ui.firstLineUf.text(),
                parent.ui.firstLineDistrict.text(), parent.ui.firstLineCep.text(), parent.ui.firstBoxUrbanZone.currentText(), 
                parent.ui.firstBoxSex.currentText(), parent.ui.firstBoxSkinColor.currentText(), parent.ui.firstBoxCivilStats.currentText()
            )
        )

        DataBase.insertHospitalizations(
            'hospitalizations', HospitalizationInfo(
                DataBase.getIdByCpf(parent.ui.firstLineCpf.text()), parent.ui.firstLineCpf.text(), parent.ui.firstLinePatientName.text(), 
                parent.ui.firstLineTreatDate.text(), parent.ui.firstBoxAdmission.currentText(), 
                parent.ui.firstBoxDoctor.currentText().split(' - ')[0], parent.ui.firstBoxDoctor.currentText().split(' - ')[1], 
                parent.ui.firstBoxClinic.currentText(), parent.ui.firstBoxBed.currentText(), parent.ui.firstBoxDependency.currentText(), 
                parent.ui.firstLineTreatHour.text(), parent.ui.firstLineResponsible.text()
            )
        )
