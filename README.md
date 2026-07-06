# 🏥 Patient Management System

A simple **Patient Management System** built with **Python**, **SQLite3**, and **Object-Oriented Programming (OOP)**.

This project was created to practice database operations (CRUD) and improve backend development skills.

---

## ✨ Features

- ➕ Add new patients
- 📋 Show all patients
- 🔍 Search patients by name
- ✏️ Update patient information
- ❌ Delete patients
- 🗓️ Automatic Persian (Jalali) visit date
- 💾 Data stored in SQLite database
- 🌐 Supports Persian (UTF-8) text

---

## 🛠️ Technologies Used

- Python 3
- SQLite3
- jdatetime
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
Patient Management System/
│
├── main.py          # Main menu and user interaction
├── manager.py       # Database operations (CRUD)
├── patient.py       # Patient class
├── database.py      # Database connection and table creation
├── patients.db      # SQLite database
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/patient-management-system.git
```

### 2. Install the required package

```bash
pip install jdatetime
```

### 3. Run the project

```bash
python main.py
```

---

## 📋 Menu

```text
========== Patient Management System ==========

1. Add Patient
2. Show All Patients
3. Search Patient
4. Update Patient
5. Delete Patient
6. Exit
```

---

## 🗄️ Database Schema

| Column      | Type                  |
| ----------- | --------------------- |
| id          | INTEGER (Primary Key) |
| name        | TEXT                  |
| phone       | TEXT                  |
| disease     | TEXT                  |
| visit_date  | TEXT                  |
| description | TEXT                  |

---

## 📸 Example

```text
========== Patient Management System ==========

1. Add Patient
2. Show All Patients
3. Search Patient
4. Update Patient
5. Delete Patient
6. Exit

Enter a number: 2

ID: 1
Name: Ali
Phone: 09123456789
Disease: HPV
Date: 1405-04-15
Description: First visit
```

---

## 📚 Concepts Practiced

- Python Classes
- Object-Oriented Programming
- SQLite3
- CRUD Operations
- SQL Queries
- Database Design
- Functions & Modules
- Error Handling

---

## 🔮 Future Improvements

- Search by phone number
- Search by disease
- Sort patients
- Statistics dashboard
- Data validation
- Backup & Restore
- GUI with Tkinter or PySide
- Doctor and appointment management
- Foreign Keys & Relationships

---

## 👨‍💻 Author

Mohammad

Backend Developer Student

Learning Python, SQL, and Backend Development 🚀
