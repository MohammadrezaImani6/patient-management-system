from manager import *
import jdatetime
from patient import *
from database import create_tables

create_tables()
manager = PatientManager()

while True:
    print("""========== Patient Management System ==========

1. Add Patient
2. Show All Patients
3. Search Patient
4. Update Patient
5. Delete Patient
6. Statistics  
7. Disease Report  
8. Last 5 Patients 
9. Search by Disease     
10. Sort By Name
11. Sort By Visit Date                                        
12. Exit

""")
    choice = input("Enter a number:")
    if choice == "1":
        name = input("Fullname: ").capitalize()
        phone = input("Phone: ")
        disease = input("Disease: ")
        date = str(jdatetime.date.today())
        description = input("Description: ")
        patient = Patient(name, phone, disease, date, description)
        manager.add_patient(patient)
    elif choice == "2":
        manager.show_all_patients()
    elif choice == "3":
        name = input("Fullname: ").capitalize()
        manager.search_patient(name)
    elif choice == "4":
        patient_id = int(input("Patient ID: "))
        print("""What do you want to update?

1. Name
2. Phone
3. Disease
4. Description
              """)
        number = input("Choice: ")
        new_value = input("New value: ")
        manager.update_patient(patient_id, number, new_value)
    elif choice == "5":
        try:
            patient_id = int(input("Patient ID: "))
        except ValueError:
            print("Invalid input.")
            continue
        manager.delete_patient(patient_id)

    elif choice == "6":
        manager.total_patients()
    elif choice == "7":
        manager.disease_report()
    elif choice == "8":
        manager.last_5_patients()
    elif choice == "9":
        disease_name = input("Disease name: ")
        manager.search_by_disease(disease_name)
    elif choice == "10":
        manager.sort_name()
    elif choice == "11":
        manager.sort_by_visit_date()
    elif choice == "12":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
