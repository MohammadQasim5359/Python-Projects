class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptom, family):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.mobile = mobile
        self.postcode = postcode
        self.symptoms = symptom
        self.doctor = 'None'
        self.family = family
       

    
    def full_name(self) :
        """full name is first_name and surname"""
        self.fullname = self.first_name + " " + self.surname
        return self.fullname
        #ToDo2
        
        pass


    def get_doctor(self) :
        #ToDo3
        return self.doctor
        pass

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.doctor = doctor

    def print_symptoms(self):
        print(self.symptoms)
        """prints all the symptoms"""
        #ToDo4
        pass
    def set_doctor(self,doctor):
        self.doctor = doctor
        

    def __str__(self):
        return f'{self.full_name():^26}|{self.doctor:^26}|{self.age:^5}|{self.mobile:^15}|{self.postcode:^10}|{self.symptoms:^11}|{self.family:^16}'
