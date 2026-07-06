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
            print(f"ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Phone: {row[2]}")
            print(f"Disease: {row[3]}")
            print(f"Date: {row[4]}")
            print(f"Description: {row[5]}")
            print()
        connection.close()

    def search_patient(self, name):
        connection, cursor = get_connection()
        cursor.execute("""SELECT * FROM patients WHERE name=?""", (name,))

        row = cursor.fetchone()
        if not row:
            print("Patient not found.")
            connection.close()
            return
        else:
            print(f"ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Phone: {row[2]}")
            print(f"Disease: {row[3]}")
            print(f"Date: {row[4]}")
            print(f"Description: {row[5]}")
            print()

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
