CREATE TABLE doctor
(
    doctor_id INTEGER NOT NULL 
    doctor_name VARCHAR (50) NOT NULL
    doctor_specialty VARCHAR (50)
    doctor_available BOOLEAN 
    CONSTRAINT doctor_pk PRIMARY KEY (doctor_id)
);
INSERT INTO doctor VALUES ("1","DR.ABIA", "CARDIOLOGY", "True");

CREATE TABLE patient
(
    patient_id INTEGER NOT NULL
    name VARCHAR(50)
    contact VARCHAR(15)
);

INSERT INTO patient VALUES ("1", "SIMAR", "403-992-1148")

CREATE TABLE appointments
(
    appointment_id INTEGER NOT NULL
    patient_id INTEGER NOT NULL
    doctor_id INTEGER NOT NULL
    date DATE
    start_time TIME
    end_time TIME
)
INSERT INTO appointments ("1", "1", "1", "2024-10-05", "00:00:00", "00:10:00")
