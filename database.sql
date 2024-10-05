CREATE DATABASE mydb;
\c mydb

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


CREATE SEQUENCE appointments_id_seq;

CREATE TABLE appointments (
  id BIGINT NOT NULL DEFAULT NEXTVAL('appointments_id_seq'::regclass),
  content_editor_id BIGINT NOT NULL,
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  appointment_id INTEGER NOT NULL
  patient_id INTEGER NOT NULL
  doctor_id INTEGER NOT NULL
  date DATE
  start_time TIME
  end_time TIME
  PRIMARY KEY (id)
);

INSERT INTO appointments (content_editor_id, start_time, end_time) VALUES
(1, CURRENT_DATE + INTERVAL '08:30', CURRENT_DATE + INTERVAL '09:00'),
(1, CURRENT_DATE + INTERVAL '09:30', CURRENT_DATE + INTERVAL '10:00'),
(2, CURRENT_DATE + INTERVAL '09:30', CURRENT_DATE + INTERVAL '10:00'),
(1, CURRENT_DATE + INTERVAL '13:30', CURRENT_DATE + INTERVAL '14:00');



