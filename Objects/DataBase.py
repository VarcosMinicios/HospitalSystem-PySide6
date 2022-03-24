from PySide6.QtSql import QSqlDatabase, QSqlQuery


class DataBase:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('data/main.db')
        self.db.open()

    @staticmethod
    def insertOrReplacePatient(table, patient):

        query = f"insert or replace into {table} (id, cpf, patient_name, born_date, profession, sus_card, rg, mother_name, " \
                "father_name, phone_one, phone_two, city, adress, uf, district, cep, zone, gender, skin_color, civil_status) " \
                f"values ((select id from {table} where cpf='{patient.cpf}'), '{patient.cpf}', '{patient.patient_name}', {patient.born_date}, " \
                f"'{patient.profession}', '{patient.sus_card}', '{patient.rg}', '{patient.mother_name}', '{patient.father_name}', " \
                f"'{patient.phone_one}', '{patient.phone_two}', '{patient.city}', '{patient.adress}', '{patient.uf}', '{patient.district}', " \
                f"'{patient.cep}', '{patient.zone}', '{patient.gender}', '{patient.skin_color}', '{patient.civil_status}')"

        if QSqlQuery(query).exec():
            return True
        else:
            return False
    
    @staticmethod
    def selectAll(table):
        return QSqlQuery.exec(f"select * from {table}").first()

    @staticmethod
    def insertHospitalizations(table, info):

        query = f"insert into {table} (patient_id, cpf, patient, hospitalize_date, admission, doctor, crm, clinic, bed, dependency, " \
                f"hospitalize_hour, responsible) values ({info.patient_id}, '{info.cpf}', '{info.patient}', " \
                f"'{info.hospitalize_date}', '{info.admission}', '{info.doctor}', '{info.crm}', '{info.clinic}', '{info.bed}', " \
                f"'{info.dependency}', '{info.hospitalize_hour}', '{info.responsible}')"

        if QSqlQuery(query):
            return True
        else:
            return False

    @staticmethod
    def getCardCode():
        return QSqlQuery("select top 1 card_code from hospitalizations order by card_code desc").exec()

    @staticmethod
    def getIdByCpf(cpf):
        return QSqlQuery(f"select id from patient_register where cpf={cpf}").exec()


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
    def __init__(self, patient_id, cpf, patient, hospitalize_date, admission, doctor, crm, clinic, bed, dependency, hospitalize_hour,
                 responsible):

        self.patient_id = patient_id
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
