class Patient:
    def __init__(self, name, phone, disease, visit_date, description):
        self.name = name
        self.phone = phone
        self.disease = disease
        self.visit_date = visit_date
        self.description = description

    def __str__(self):
        return f"Name: {self.name}\nPHONE: {self.phone}\nDisease: {self.disease}\nVisit Date: {self.vissit_data}\nDescription: {self.description}"
