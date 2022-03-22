from PySide6.QtSql import QSqlDatabase, QSqlQuery


class DataBase:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('data/main.db')
        self.db.open()
    
    def insertOrReplacePatient(self, table, patient):

        query = f"insert or replace into {table} (id, cpf, patient_name, born_date, profession, sus_card, rg, mother_name, " \
                "father_name, phone_one, phone_two, city, adress, uf, district, cep, zone, gender, skin_color, civil_status) " \
                f"values ((select id from {table} where cpf='{patient.cpf}'), '{patient.cpf}', '{patient.patient_name}', {patient.born_date}, " \
                f"'{patient.profession}', '{patient.sus_card}', '{patient.rg}', '{patient.mother_name}', '{patient.father_name}', " \
                f"'{patient.phone_one}', '{patient.phone_two}', '{patient.city}', '{patient.adress}', '{patient.uf}', '{patient.district}', " \
                f"'{patient.cep}', '{patient.zone}', '{patient.gender}', '{patient.skin_color}', '{patient.civil_status}')"

        if QSqlQuery.exec(query):
            return True
        else:
            return False

    def selectAll(self, table):
        return QSqlQuery.exec(f"select * from {table}").first()

    def insertHospitalizations(self, table, info):

        query = f"insert into {table} (id, card_code, cpf, patient, hospitalize_date, admission, doctor, crm, clinic, bed, dependency, " \
                f"hospitalize_hour, responsible) values ({info.id}, {info.card_code}, '{info.cpf}', '{info.patient}', {info.hospitalize_date}, " \
                f"'{info.admission}', '{info.doctor}', '{info.crm}', '{info.clinic}', '{info.bed}', '{info.dependency}', "\
                f"'{info.hospitalize_hour}', '{info.responsible}')"

        if QSqlQuery.exec(query):
            return True
        else:
            return False

class PatientRegister:
    def __init__(self, cpf, patient_name, born_date, profession, sus_card, rg, mother_name, father_name, phone_one, phone_two,
                 city, adress, uf, district, cep, zone, gender, skin_color, civil_status):

        self.cpf = cpf
        self.patient_name = patient_name
        self.born_date = born_date 
        self.profession = profession
        self.sus_card = sus_card
        self.rg = rg
        self.mother_name = mother_name
        self.father_name = father_name
        self.phone_one = phone_one
        self.phone_two = phone_two
        self.city = city
        self.adress = adress
        self.uf = uf
        self.district = district
        self.cep = cep
        self.zone = zone
        self.gender = gender
        self.skin_color = skin_color
        self.civil_status = civil_status


class HospitalizationInfo:
    def __init__(self,id, card_code, cpf, patient, hospitalize_date, admission, doctor, crm, clinic, bed, dependency,
                 hospitalize_hour, responsible):

        self.id = id
        self.card_code = card_code
        self.cpf = cpf
        self.patient = patient
        self.hospitalize_date = hospitalize_date
        self.admission = admission
        self.doctor = doctor
        self.crm = crm
        self.clinic = clinic
        self.bed = bed
        self.dependency = dependency
        self.hospitalize_hour = hospitalize_hour
        self.responsible = responsible
