from database import get_connection


class PatientManager:
    def add_patient(self, patient):
        connection, cursor = get_connection()
        cursor.execute(
            """INSERT INTO patients (name,phone,disease,visit_date,description)
            VALUES (?,?,?,?,?)""",
            (
                patient.name,
                patient.phone,
                patient.disease,
                patient.visit_date,
                patient.description,
            ),
        )
        connection.commit()
        connection.close()

    def print_patient(self, patient):
        print(f"ID: {patient[0]}")
        print(f"Name: {patient[1]}")
        print(f"Phone: {patient[2]}")
        print(f"Disease: {patient[3]}")
        print(f"Date: {patient[4]}")
        print(f"Description: {patient[5]}")
        print()

    def show_all_patients(self):
        connection, cursor = get_connection()
        sql = """SELECT * FROM patients"""
        cursor.execute(sql)
        records = cursor.fetchall()
        if not records:
            print("Not found.")
            connection.close()
            return
        for row in records:
            self.print_patient(row)
        connection.close()

    def search_patient(self, name):
        connection, cursor = get_connection()
        cursor.execute(
            """SELECT * FROM patients WHERE name LIKE ?""", ("%" + name + "%",)
        )

        rows = cursor.fetchall()
        if len(rows) == 0:
            print("Patient not found.")
            connection.close()
            return
        else:
            for patient in rows:
                self.print_patient(patient)

        connection.close()

    def delete_patient(self, patient_id):
        connection, cursor = get_connection()
        cursor.execute("""DELETE  FROM patients WHERE id=?""", (patient_id,))
        if cursor.rowcount == 0:
            print("Patient not found.")
            connection.close()
            return
        else:
            print("Patient deleted successfully.")
            connection.commit()
            connection.close()

    def update_patient(self, patient_id, choice, new_value):
        connection, cursor = get_connection()
        if choice == "1":
            column = "name"
        elif choice == "2":
            column = "phone"
        elif choice == "3":
            column = "disease"
        elif choice == "4":
            column = "description"
        else:
            print("Invalid choice.")
            connection.close()
            return
        sql = f"UPDATE patients SET {column}=? WHERE id=?"
        cursor.execute(
            sql,
            (
                new_value,
                patient_id,
            ),
        )
        if cursor.rowcount == 0:
            print("Patient not found.")
        else:
            connection.commit()
            print("Patient updated successfully.")
        connection.close()

    def total_patients(self):
        connection, cursor = get_connection()
        cursor.execute("""SELECT COUNT(*) FROM patients""")
        number = cursor.fetchone()
        print("=" * 30)
        print(f"Total Patients: {number[0]}")
        print("=" * 30)
        connection.close()

    def disease_report(self):
        connection, cursor = get_connection()
        cursor.execute(
            """SELECT disease,COUNT(*) FROM  patients GROUP BY disease ORDER BY COUNT(*) DESC; """
        )
        rows = cursor.fetchall()
        print("=" * 30)
        print("Disease Report")
        for item in rows:
            print(f"{item[0]}= {item[1]}")
        print("=" * 30)
        connection.close()

    def last_5_patients(self):
        connection, cursor = get_connection()
        cursor.execute("SELECT * FROM patients ORDER BY id DESC LIMIT 5;")
        row = cursor.fetchall()
        if not row:
            print("No patients found.")
            connection.close()
            return
        for patient in row:
            self.print_patient(patient)
        connection.close()

    def search_by_disease(self, disease):
        connection, cursor = get_connection()
        cursor.execute(
            "SELECT * FROM patients WHERE disease LIKE ?", ("%" + disease + "%",)
        )
        row = cursor.fetchall()
        if not row:
            print("No patients found.")
            connection.close()
            return
        for patient in row:
            self.print_patient(patient)
        connection.close()

    def sort_name(self):
        connection, cursor = get_connection()
        cursor.execute("SELECT * FROM patients ORDER BY name ASC;")
        row = cursor.fetchall()
        if not row:
            print("No patients found.")
            connection.close()
            return
        for patient in row:
            self.print_patient(patient)
        connection.close()

    def sort_by_visit_date(self):
        connection, cursor = get_connection()
        cursor.execute("SELECT * FROM patients ORDER BY visit_date DESC;")
        row = cursor.fetchall()
        if not row:
            print("No patients found.")
            connection.close()
            return
        for patient in row:
            self.print_patient(patient)
        connection.close()
