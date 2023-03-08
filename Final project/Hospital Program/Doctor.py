class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality, appointments):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.first_name = first_name
        self.surname = surname
        self.speciality = speciality
        self.patients = []
        self.appointments = appointments

    
    def full_name(self) :
        full_name = self.first_name + " " + self.surname
        return full_name
                    
        #ToDo1
        pass

    def get_first_name(self) :
        return self.first_name
        #ToDo2
        pass

    def set_first_name(self, new_first_name):
        #ToDo3
        self.first_name = new_first_name
        pass

    def get_surname(self) :
        #ToDo4
        return self.surname
        pass

    def set_surname(self, new_surname):
        #ToDo5
        self.surname = new_surname
        pass

    def get_speciality(self) :
        #ToDo6
        return self.speciality
        pass

    def set_speciality(self, new_speciality):
        #ToDo7
        self.speciality = new_speciality
        pass

    def add_patient(self, patient):
        self.patients.append(patient)

    def patientlist(self):
        return self.patients

    def appointmentadd(self):
        self.appointments +=1
        
        
    def appointmentsubtract(self):
        self.appointments -=1
        
    def patientdelete(self):
        self.patients.pop()
    def __str__(self) :
        return f'{self.full_name():^30}|{self.speciality:^15}'
