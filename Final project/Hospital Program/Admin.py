from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.username = username
        self.password = password
        self.address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        
        
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if username == self.username and password == self.password:
            return True
            
        #ToDo1
            pass

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        pass

    def doctor_management(self, doctors,patients):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("\n-----Doctor Management-----\n")

        # menu
        print('Choose the operation:\n')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete\n')

        #ToDo3
        pass
        op = input("Select an option: ")

        # register
        if op == '1':
            print("\n-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:\n')
            doc_firstname = input("First Name: ")
            doc_surname = input("Surname: ")
            doc_spec = input("Speciality: ")
            doc_appoint = input("Appointments: ")
            
            try:
                int(doc_appoint)
            except ValueError:
                print("\nYou did not input a valid number for Appointments")
                return
                
            
            
            #ToDo4
            pass

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if doc_firstname == doctor.get_first_name() and doc_surname == doctor.get_surname():
                    print('\nName already exists.')
                    name_exists = True
                    break
                    #ToDo5
                    pass # save time and end the loop

            #ToDo6
            pass# add the doctor ...
            if name_exists == False:
                doctors.append(Doctor(doc_firstname, doc_surname, doc_spec,int(doc_appoint)))
                                                         # ... to the list of doctors
                print('\nDoctor registered.')

        # View
        elif op == '2':
            print("\n-----List of Doctors-----")
            
            for i in doctors:
                print(i)
            #ToDo7
            pass

        # Update
        elif op == '3':
            while True:
                print("\n-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("\nDoctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('\nThe ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality\n')
            op = int(input('Input: ').lower()) # make the user input lowercase
            
            if op == 1:
                
                new_first_name = input("\nInput New First Name: ").lower()
                new_first_namecapt = new_first_name.capitalize()
                doctor_oldname = doctors[index].full_name()
                doctors[index].set_first_name(new_first_namecapt)
                print("\nDoctor {}'s name has been updated to {}".format(doctor_oldname,doctors[index].full_name()))
                
            elif op == 2:
                new_surname = input("\nInput New Surname: ").lower()
                new_surnamecapt = new_surname.capitalize()
                doctor_oldname = doctors[index].full_name()
                doctors[index].set_surname(new_surnamecapt)
                print("\nDoctor {}'s name has been updated to {}".format(doctor_oldname,doctors[index].full_name()))
            elif op == 3 :
                new_spec = input("\nInput New Speciality ").lower()
                new_speccapt = new_spec.capitalize()
                doctor_oldspec = doctors[index].speciality
                doctors[index].set_speciality(new_speccapt)
                print("\nDoctor {}'s speciality has been updated from {} updated to {}".format(doctors[index].full_name(),doctor_oldspec,doctors[index].get_speciality()))
           
            #ToDo8
            pass

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            while True:
                try:
                    index = int(input('Enter the ID of the doctor: '))- 1
                    doctor_index=self.find_index(index,doctors)
                    
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("\nDoctor not found")
                        return
                    
                        # doctor_index is the ID mines one (-1)
                        
    
                except ValueError: # the entered id could not be changed into an int
                    print('\nThe ID entered is incorrect')
                    
                    return
                
            for i in patients:
                if i.doctor == doctors[index].full_name():
                    i.doctor = "None"
        
            
           
            print('\nDoctor {} has been Successfully Deleted.'.format(doctors[index].full_name()))
            
            del doctors[index]
        
            
        
        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        patient_id = 1
        print("-----View Patients-----")
        print('ID |        Full Name         |    Doctor`s Full Name    | Age |    Mobile     | Postcode | Symptoms  |     Family  ')
       
                
        for i in patients:
            
            print("{}  |{}".format(patient_id,i))
            patient_id += 1
        #ToDo10
        pass

    def assign_doctor_to_patient(self, patients, doctors, patient_index = 0):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |        Full Name         |    Doctor`s Full Name    | Age |    Mobile     | Postcode | Symptoms  |     Family  ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1
            

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                if patients[patient_index].get_doctor() != "None" and doctors[doctor_index].full_name():
                    for i in doctors:
                        if i.full_name() == patients[patient_index].get_doctor():
                            i.patients.remove(patients[patient_index].full_name())
                            i.appointmentsubtract()
                            print("patient removed")
                        else:
                            print("nothing")
                pass
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                doctors[doctor_index].appointmentadd()
                
                print('\n{} is now assigned to Doctor {}.'.format(patients[patient_index].full_name(),doctors[doctor_index].full_name()))
                patients[patient_index].set_doctor(doctors[doctor_index].full_name())

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----\n")
        self.view_patient(patients)
        
        patient_index = input('Please enter the patient ID: ')
        
        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('\nThe id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('\nThe id entered is incorrect')
            return # stop the procedures

       
        print("{} has been discharged".format(patients[patient_index].full_name())) 
       
        discharge_patients.append(patients[patient_index])
        del patients[patient_index]
        theswitch = True
        while theswitch == True:
            op = input('Do you want to discharge another patient(Y/N):').lower()

            if op.lower() == 'yes' or op.lower() == 'y':
                #ToDo3
                self.discharge(patients,discharge_patients)
                return
                

            elif op.lower() == 'no' or op.lower() == 'n':
                return

            # unexpected entry
            else:
                print('Please answer by yes or no.')
        #ToDo12
        pass

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |        Full Name         |    Doctor`s Full Name    | Age |    Mobile     | Postcode | Symptoms  |     Family  ')
        #ToDo13
        dischargeid = 1
        for i in discharged_patients:
            print("{}  |{}".format(dischargeid,i))
            dischargeid += 1
            
        pass
    def set_patient_family(self,patients):
        self.view_patient(patients)
        selection1 = input("Select ID of the patient that has family on the system: ")
        try:
            selection1 = int(selection1) -1
            if selection1 not in range(len(patients)):
                print("The ID entered was incorrect!")
                return
        except ValueError:
            print("Number not input")
            return
        selection2 = input("Input the ID of the family member: ")
        try:
            selection2 = int(selection2) -1
            if selection2 not in range(len(patients)):
                print("The ID entered was incorrect!")
                return
        except ValueError:
            print("Number not input")
            return
        if selection1 == selection2:
            print("\nYou cannot select the same patient twice")
            return
        if patients[selection1].family == patients[selection2].family and patients[selection1].family != "None":
            print("\nPatients already in the same family")
            print("Would you like to change the family name?")
            familychange = input("\nSelection y/n: ")
            if familychange.lower() == "y" or familychange.lower() == "yes":
                print("\nWhat would you like the family name to be?")
                newfamname = input("Family Name: ")
                print("\nWould you like prior family members to be part of the new family")
                otherfamupdate = input("Selection y/n: ")
                familynamecomp = patients[selection1].family
                if otherfamupdate.lower() == "y" or otherfamupdate.lower() == "yes":
                    for i in patients:
                        if i.family == familynamecomp:
                            i.family = newfamname
                    print("All family members have had their family name changed to {}".format(newfamname))
                    return
                    print("not done")
                elif otherfamupdate.lower() == "n" or otherfamupdate.lower() == "no":
                    
                    patients[selection1].family = newfamname
                    patients[selection2].family = newfamname
                    print("{} and {}'s new family name is {}".format(patients[selection1].full_name(),patients[selection2].full_name(),newfamname))
                    return
            elif familychange.lower() == "n" or familychange.lower() == "no":
                return
            else:
                print("\nDid not select a valid option")
                return
        if patients[selection2].family != "None":
            patients[selection1].family = patients[selection2].family
            print("\n{} has been added to {}'s family".format(patients[selection1].first_name,patients[selection2].first_name))
        else:
            
            family_name = input("\nWhat is the family name? ")
            
            patients[selection1].family = family_name
            patients[selection2].family = family_name
            
            print("\nA new family has been created with {} and {} as members".format(patients[selection1].full_name(),patients[selection2].full_name()))
        
        
           
    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = (input('Input: '))
        try:
            op = int(op)
        except:
            pass
        if op == 1:
            
            username = input("Enter the new username: ")
            
            self.username = username 
            print("\nUsername is now {}".format(username))
            #ToDo14
            
            pass

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.password = password
                print("\nPassword is now {}".format(password))

        elif op == 3:
            #ToDo15
            
            address = input("Enter the new address: ")
            
            self.address = address
            print("\Address is now {}".format(address))
            pass

        else:
            print("\nInvalid selection")
            #ToDo16
            pass
    def report(self,doctors,patients):
            sicknesslst = []
            sicknessamount = 0
            print("\nTotal number of doctors in the system are {}".format(len(doctors)))
            for doctor in doctors:
                print("Doctor {} has {} Patients and {} Appointments".format(doctor.full_name(),len(doctor.patients),doctor.appointments))
            for patient in patients:
                sicknesslst.append(patient.symptoms)
            sicknessset = set(sicknesslst)
            sicknesslst = list(sicknessset)
            for i in sicknesslst:
                for j in patients:
                    if j.symptoms == i:
                        sicknessamount += 1
                print("{} patient('s) have the symptom {}".format(sicknessamount,i))
                sicknessamount = 0
                
            
            