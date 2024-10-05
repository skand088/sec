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
WITH RECURSIVE date_range AS 

(
  SELECT STR_TO_DATE('2019-10-10 09:00:00','%Y-%m-%d %H:%i:%s') AS ts
  UNION  ALL
  SELECT ts + INTERVAL 15 MINUTE
  FROM   date_range
  WHERE  ts < STR_TO_DATE('2019-10-15 21:00:00','%Y-%m-%d %H:%i:%s')
)

SELECT
  DATE_FORMAT(ts, '%a') AS DOW,
  WEEKDAY(ts), 
  WEEKDAY(ts) % 6,
  ts from date_range
WHERE CAST(ts AS DATE) >= CAST('2019-10-10 09:00:00' AS DATE) 
AND   CAST(ts AS DATE) <= CAST('2019-10-15 21:00:00' AS DATE)
AND DATE_FORMAT(ts, '%H:%i:%s') >= '09:00:00'
AND DATE_FORMAT(ts, '%H:%i:%s') <= '21:00:00'
AND DATE_FORMAT(ts, '%a') != 'Sat'
AND DATE_FORMAT(ts, '%a') != 'Sun';

CREATE TABLE slot
(
  slot_id    INTEGER NOT NULL AUTO_INCREMENT,
  slot_begin TIMESTAMP NOT NULL,
  slot_end   TIMESTAMP NOT NULL,
  CONSTRAINT slot_pk PRIMARY KEY (slot_id),
  CONSTRAINT slot_begin_end_uq UNIQUE (slot_begin, slot_end)
);

WITH RECURSIVE date_range AS 
(
  SELECT STR_TO_DATE('2019-10-10 09:00:00','%Y-%m-%d %H:%i:%s') AS ts
  UNION  ALL
  SELECT ts + INTERVAL 15 MINUTE
  FROM   date_range
  WHERE  ts < STR_TO_DATE('2019-10-15 21:00:00','%Y-%m-%d %H:%i:%s')
),
xrange AS
(
  SELECT
    DATE_FORMAT(ts, '%a') AS DOW,
    WEEKDAY(ts), 
    WEEKDAY(ts) % 6,
    ts from date_range
  WHERE CAST(ts AS DATE) >= CAST('2024-10-01 09:00:00' AS DATE) 
  AND   CAST(ts AS DATE) <= CAST('2024-10-15 21:00:00' AS DATE)
  AND DATE_FORMAT(ts, '%H:%i:%s') >= '09:00:00'
  AND DATE_FORMAT(ts, '%H:%i:%s') <= '21:00:00'
  AND DATE_FORMAT(ts, '%a') != 'Sat'
  AND DATE_FORMAT(ts, '%a') != 'Sun'
)
SELECT t1.ts, t2.ts FROM xrange t1
JOIN xrange t2
  ON t1.ts = DATE_ADD(t2.ts, INTERVAL - 15 MINUTE);



