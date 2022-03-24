<h1 style='align: center;'>Hospital System</h1>

<p>This is a Hospital System designed for register and control of hospitalized patients</p>

## Methods

The initial screen is the map of hospital beds, with the name and the clinic of patient, each patient is suposed
to be linked at the medical record, and the button named "alta" in the right side of the name is to update Database
and update the map, removing the patient who was discharged, the second screen, acessible by the Menu in the top of
application is the way to hospitalize and register the patient. The 3rd button of menu is the historic of patient in the 
establishment. After this is the register of patient, with all his personal informations. The "Exportação" button move to the 
search of Database, to make a record of the hospital, or patient or hospitalizations. The last menu button is the "Recibo"
where you can make the receipt of payment to the hospitalizations debits of the patient.

## is used in this Project

The database used is SQLite, provided by the package QSqlDataBase of PySide6, the LineEdits has a personalized class, to handle their design
and the utility functions comom to all LineEdits of the application.