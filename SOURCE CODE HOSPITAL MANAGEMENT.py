import mysql.connector
from mysql.connector import Error
from sys import exit
from datetime import datetime

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_phone(prompt):
    while True:
        try:
            phone = input(prompt)
            if not phone.isdigit():
                raise ValueError("Phone number must contain only digits.")
            if len(phone) != 10:
                raise ValueError("Phone number must be exactly 10 digits.")
            return int(phone)
        except ValueError as e:
            print(f"Invalid phone number: {e}")

try:
    # Establishing connection to MySQL
    conn = mysql.connector.connect(host='localhost', user='root', password='computer')
    if conn.is_connected():
        print('Successfully connected to MySQL')
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
    exit()

# Creating a cursor object
c1 = conn.cursor()

# Creating the database if it doesn't exist
c1.execute('CREATE DATABASE IF NOT EXISTS apollo1')
c1.execute('USE apollo1')

# Creating tables if they don't exist
c1.execute('''
CREATE TABLE IF NOT EXISTS patient_details (
    p_name VARCHAR(25) PRIMARY KEY,
    p_age INT(3),
    p_problems VARCHAR(40),
    p_phono BIGINT
)
''')

c1.execute('''
CREATE TABLE IF NOT EXISTS doctor_details (
    d_name VARCHAR(25) PRIMARY KEY,
    d_age INT(3),
    d_department VARCHAR(40),
    d_phono BIGINT
)
''')

c1.execute('''
CREATE TABLE IF NOT EXISTS worker_details (
    w_name VARCHAR(25) PRIMARY KEY,
    w_age INT(3),
    w_workname VARCHAR(40),
    w_phono BIGINT
)
''')

# Main program loop
print('---------------------------------------------')
print("HOSPITAL MANAGEMENT SYSTEM")
print('---------------------------------------------')
print('"GOD WISHES YOU"')  # START LOGIN YOURSELF
print("1. LOGIN")
print("2. EXIT")
choice = int(input("ENTER YOUR CHOICE: "))

if choice == 1:
    u1 = input("Enter user name: ")
    pwd1 = input("Enter the password: ")

    if u1 == 'APOLLO' and pwd1 == 'DINAKARAN':  # USER ID AND PASSWORD
        print('Connected')
        print("WELCOME TO APOLLO HOSPITAL")  # SUCCESSFULLY CONNECTED

        while True:
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Current Date and Time: {current_time}")
            print('1. Registering Patient details')  # NEW PATIENT REGISTRATION
            print('2. Registering Doctor details')  # NEW DOCTOR REGISTRATION
            print('3. Registering Worker details')  # NEW WORKER REGISTRATION
            print("4. Total patient details")  # DETAILS ABOUT ALL PATIENTS
            print("5. Total doctor details")  # DETAILS ABOUT ALL DOCTORS
            print("6. Total worker details")  # DETAILS ABOUT ALL WORKERS
            print('7. Patient detail')  # SELECTED PATIENT DETAILS
            print('8. Doctor detail')  # SELECTED DOCTOR DETAILS
            print('9. Worker detail')  # SELECTED WORKER DETAILS
            print('10. Exit')  # EXIT

            try:
                choice = int(input('ENTER YOUR CHOICE: '))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 1:
                p_name = input('Enter Patient Name: ')
                p_age = input_int('Enter Age: ')
                p_phono = input_phone('Enter Phone number (10 digits): ')
                p_problems = input('Enter the Problem/Disease: ')
                sql_insert = "INSERT INTO patient_details (p_name, p_age, p_problems, p_phono) VALUES (%s, %s, %s, %s)"
                try:
                    c1.execute(sql_insert, (p_name, p_age, p_problems, p_phono))
                    conn.commit()
                    print('SUCCESSFULLY REGISTERED')
                except mysql.connector.Error as err:
                    print(f"Error: {err}")

            elif choice == 2:
                d_name = input('Enter Doctor Name: ')
                d_age = input_int('Enter Age: ')
                d_phono = input_phone('Enter Phone number (10 digits): ')
                d_department = input('Enter the Department: ')
                sql_insert = "INSERT INTO doctor_details (d_name, d_age, d_department, d_phono) VALUES (%s, %s, %s, %s)"
                try:
                    c1.execute(sql_insert, (d_name, d_age, d_department, d_phono))
                    conn.commit()
                    print('SUCCESSFULLY REGISTERED')
                except mysql.connector.Error as err:
                    print(f"Error: {err}")

            elif choice == 3:
                w_name = input('Enter Worker Name: ')
                w_age = input_int('Enter Age: ')
                w_phono = input_phone('Enter Phone number (10 digits): ')
                w_workname = input('Enter type of work: ')
                sql_insert = "INSERT INTO worker_details (w_name, w_age, w_workname, w_phono) VALUES (%s, %s, %s, %s)"
                try:
                    c1.execute(sql_insert, (w_name, w_age, w_workname, w_phono))
                    conn.commit()
                    print('SUCCESSFULLY REGISTERED')
                except mysql.connector.Error as err:
                    print(f"Error: {err}")

            elif choice == 4:
                c1.execute('SELECT * FROM patient_details')
                patients = c1.fetchall()
                if not patients:
                    print("No patient records found.")
                for patient in patients:
                    print(patient)

            elif choice == 5:
                c1.execute('SELECT * FROM doctor_details')
                doctors = c1.fetchall()
                if not doctors:
                    print("No doctor records found.")
                for doctor in doctors:
                    print(doctor)

            elif choice == 6:
                c1.execute('SELECT * FROM worker_details')
                workers = c1.fetchall()
                if not workers:
                    print("No worker records found.")
                for worker in workers:
                    print(worker)

            elif choice == 7:
                h = input("Enter patient name: ")
                sql_w = 'SELECT * FROM patient_details WHERE p_name = %s'
                c1.execute(sql_w, (h,))
                patients = c1.fetchall()
                if not patients:
                    print("No patient found with that name.")
                for patient in patients:
                    print(patient)

            elif choice == 8:
                d = input("Enter doctor name: ")
                sql_d = 'SELECT * FROM doctor_details WHERE d_name = %s'
                c1.execute(sql_d, (d,))
                doctors = c1.fetchall()
                if not doctors:
                    print("No doctor found with that name.")
                for doctor in doctors:
                    print(doctor)

            elif choice == 9:
                f = input("Enter worker name: ")
                sql_f = 'SELECT * FROM worker_details WHERE w_name = %s'
                c1.execute(sql_f, (f,))
                workers = c1.fetchall()
                if not workers:
                    print("No worker found with that name.")
                for worker in workers:
                    print(worker)

            elif choice == 10:
                print("Exiting program.")
                c1.close()
                conn.close()
                exit()

            else:
                print("Invalid choice. Please try again.")

    else:
        print('Wrong username & password')

elif choice == 2:
    print("Exiting program.")
    exit()
else:
    print("Invalid choice. Exiting.")

