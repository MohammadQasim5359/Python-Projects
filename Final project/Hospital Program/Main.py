# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
import tkinter

class gui:
    def __init__(self, patients, doctors,discharge):
        self.patients = patients
        self.doctors = doctors
        self.discharge = discharge
        self.mw = tkinter.Tk()
        #self.admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
        #self.doctors = [Doctor('John','Smith','Internal Med.',2), Doctor('Jone','Smith','Pediatrics',10), Doctor('Jone','Carlos','Cardiology',7)]
        #self.patients = [Patient('Sara','Smith', 20, '07012345678','B1 234',"Fever","None"), Patient('Mike','Jones', 37,'07555551234','L2 2AB',"Headache","None"), Patient('Daivd','Smith', 15, '07123456789','C1 ABC',"Sad","None")]
        #self.discharged_patients = []
        
        self.label1 = tkinter.Label(self.mw, text="Hospital Management")
        self.spacelabel = tkinter.Label(self.mw, text="")
        self.doctorbutton = tkinter.Button(self.mw, text="Doctor Management", command=self.doctor_management)
        self.patientbutton = tkinter.Button(self.mw, text="Patient Management", command=self.patient_management)
        self.discharge_list = tkinter.Button(self.mw, text="Discharged Patients", command=self.discharge_list)
        self.doctorassign = tkinter.Button(self.mw, text="Assign Doctor To Patient", command=self.doctorassign)
        self.adminupdate = tkinter.Button(self.mw, text="Update Admin Details", command=self.adminupdate)
        self.report = tkinter.Button(self.mw, text="Management Report", command=self.report)
        self.quit = tkinter.Button(self.mw, text="Quit", command=self.quit_program)
        
        self.label1.grid(row=0, column=2)
        self.spacelabel.grid(row=1,column=2)
        self.doctorbutton.grid(row=2,column=2)
        self.patientbutton.grid(row=3,column=2)
        self.discharge_list.grid(row =4, column=2)
        self.doctorassign.grid(row=5,column=2)
        self.adminupdate.grid(row=6,column=2)
        self.report.grid(row=7,column=2)
        self.quit.grid(row=8,column=2)
        
        tkinter.mainloop()
        
    def doctor_management(self):
        labels = []
        increment = 30
        xc = 10
        yc = 10
        self.doctormw = tkinter.Tk()
        self.doctormw.geometry("1000x1000")
        
        self.doctormanlab= tkinter.Label(self.doctormw, text="Doctor Management")
        yc += increment
        self.spacelabel2 = tkinter.Label(self.doctormw, text="")
        
        #---------------------start of labels and entry for doctor input----------------#
        self.doctorfirstnamelab = tkinter.Label(self.doctormw, text="Doctor's First Name")
        
        
        yc += increment
        self.doctorfirstnameent = tkinter.Entry(self.doctormw)
        
        self.doctorsecondnamelab = tkinter.Label(self.doctormw, text="Doctor's Second Name")
        self.doctorsecondnameent = tkinter.Entry(self.doctormw)
        
        
        self.doctorspeciallab = tkinter.Label(self.doctormw, text="Doctor's Speciality Name")
        self.doctorspecialent = tkinter.Entry(self.doctormw)
        
        self.doctorappointmentlab = tkinter.Label(self.doctormw, text="Doctor's Appointments")
        self.doctorappoinmentent = tkinter.Entry(self.doctormw)
        #---------------------end of labels and entry for doctor input----------------#
        
        
        #--------------------------------the buttons-----------------------------#
        self.registerdocbutton = tkinter.Button(self.doctormw, text="Register a new Doctor", command= self.registerdoctor)
        
        self.updatedocbutton = tkinter.Button(self.doctormw, text="Update Doctor Details", command=self.updatedocbutton)
        self.deletedocbutton = tkinter.Button(self.doctormw, text="Delete a Doctor")
        #--------------------------------the buttons-----------------------------#
        
        #------------------------------PACKING IT-------------------------------#
        
        #self.doctormanlabel.grid(row=0,column=1)
        
        for i,v in enumerate(self.doctors):
            labels.append(tkinter.Label(self.doctormw, text= f"{i + 1} {v}"))
            labels[len(labels)-1].place(x= xc +700,y= yc -50+(30*i))
        #self.doctorslist = tkinter.Label(self.doctormw, text= )
        
        
            
        self.doctormanlab.grid(row=4, column=1)
        self.doctorfirstnamelab.grid(row=5,column=0)
        self.doctorfirstnameent.grid(row=6,column=0)
        
        self.doctorsecondnamelab.grid(row=5,column=1)
        self.doctorsecondnameent.grid(row=6,column=1)
        
        self.doctorspeciallab.grid(row=5,column=2)
        self.doctorspecialent.grid(row=6,column=2)
        
        self.doctorappointmentlab.grid(row=5, column=3)
        self.doctorappoinmentent.grid(row=6,column=3)
        
        
        
        self.registerdocbutton.grid(row=7,column=1)
        
        
        self.updatedocbutton.grid(row=8,column=1)
        
        
        self.deletedocbutton.grid(row=9,column=1)
        
        
        #------------------------------PACKING IT-------------------------------#
        tkinter.mainloop()
    def registerdoctor(self):
        print(1)
        firstname = self.doctorfirstnameent.get()
        surname = self.doctorsecondnameent.get()
        speciality = self.doctorspecialent.get()
        appointments = self.doctorappoinmentent.get()
        self.doctors.append(Doctor(firstname,surname ,speciality,appointments))
    
    def updatedocbutton(self):
        pass
    def patient_management(self):
        pass
    def discharge_list(self):
        self.dischargemw = tkinter.Tk()
        
        self.disvar = tkinter.StringVar(self.dischargemw,self.discharge)
        self.dislab = tkinter.Label(self.dischargemw,textvariable=self.disvar)
        
        self.dislab.grid(row=0,column=0)
        tkinter.mainloop()
    def doctorassign(self):
        pass
    def adminupdate(self):
        pass
    def report(self):
        self.reportmw = tkinter.Tk()
        totdoctor = 0
        for i in self.doctors:
            totdoctor +=1
        self.totdoclab = tkinter.Label(self.reportmw, text="Total Doctors in the system")
        
        self.docvar = tkinter.StringVar(self.reportmw, totdoctor)
        self.totaldocsvar = tkinter.Label(self.reportmw, textvariable=self.docvar)
        
        docmsglst = []
        for i in self.doctors:
            docmsglst.append("Doctor {} has {} patients and {} appointments".format(i.full_name(),len(i.patients),i.appointments))
        self.docpatvar = tkinter.StringVar(self.reportmw,docmsglst)
        self.docpatlab = tkinter.Label(self.reportmw,textvariable=self.docpatvar)
        
        sicknesslst = []
        for patient in self.patients:
            sicknesslst.append(patient.symptoms)
        sicknessset = set(sicknesslst)
        sicknesslst = list(sicknessset)
        sicknessamount = 0
        sicknessvar = []
        for i in sicknesslst:
            for j in self.patients:
                if j.symptoms == i:
                    sicknessamount += 1
            sicknessvar.append("{} patient('s) have the symptom {}".format(sicknessamount,i))
            sicknessamount = 0
        
        self.sickvar = tkinter.StringVar(self.reportmw,sicknessvar)
        self.sicklab = tkinter.Label(self.reportmw, textvariable=self.sickvar) 
        
        
        self.totdoclab.grid(row=0,column=0)
        self.totaldocsvar.grid(row=1,column=0)
        self.docpatlab.grid(row=2,column=0)
        self.sicklab.grid(row=3,column=0)
        tkinter.mainloop()
        pass
    def quit_program(self):
        self.mw.destroy()


def main():
    """
    the main function to be ran when the program runs
    """
    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.',2), Doctor('Jone','Smith','Pediatrics',10), Doctor('Jone','Carlos','Cardiology',7)]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234',"Fever","None"), Patient('Mike','Jones', 37,'07555551234','L2 2AB',"Headache","None"), Patient('Daivd','Smith', 15, '07123456789','C1 ABC',"Sad","None")]
    discharged_patients = []
    
    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')
    patient_file = open("patient_file.txt", "r")
    
    patientline = patient_file.readline()
    patientdata = []
    finalpatientlst = []
    overridecheck = 0
    while patientline != "":
        
        overridecheck += 1
        patienttemp = patientline.split("|")
        for i in patienttemp:
            if i != "\n":
               patientdata.append(i)
            if '' in patientdata:
                del patientdata[-1]
        
        
        finalpatientlst.append(patientdata[:])
        patientdata.clear()
        

        
        patientline = patient_file.readline()
    
        
    patient_file.close()
    
    if overridecheck >= 1:
        print("\nThere are updated patient records avaliable containing {} patients".format(overridecheck))
        print("Would you like to load them and overwrite current data?\n")
        
        
        overwriteswitch = True
        while overwriteswitch == True:
            
            overwriteselect = input("Selection (y/n): ")
            
            if overwriteselect.lower() == "y" or overwriteselect.lower() =="yes":
                patients.clear()
                for i in finalpatientlst:
                    patients.append(Patient(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
                overwriteswitch = False
                print("\nRecords Loaded")
                
            elif overwriteselect.lower() == "n" or overwriteselect.lower() == "no":
                print("\nRecords Not Loaded")
                overwriteswitch = False
                
            else:
                print("\nInvalid Input Please select y or n")
        
    while running:
        
        # print the menu
        print('\nChoose the operation:\n')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- View/Discharge/Setfamily patients')
        print(' 3- View Discharged patients')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- Management Report')
        print(' 7- Open GUI')
        print(" 8- Quit\n")

        # get the option
        op = input('Option: \n')

        if op == '1':
            
            admin.doctor_management(doctors,patients)

        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            
            print("Choose the Operation\n")
            print("1 - View Patient")
            print("2 - Discharge Patient")
            print("3 - Set Patient Family")
            patientoperation = int(input("Option: "))
            
            if patientoperation == 1:
                admin.view_patient(patients)
            
            elif patientoperation == 2:
                admin.discharge(patients, discharged_patients)
                
            elif  patientoperation == 3:
                admin.set_patient_family(patients)
                pass
        
        elif op == '3':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)
            pass

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()
        elif op =="6":
            admin.report(doctors,patients)
        elif op == '7':
            thegui = gui(patients, doctors,discharged_patients)
            thegui()
        elif op == '8':
            
            print("Would you like to Upload Patient Data?")
            filewritecheck = input("Selection (y/n)")
            if filewritecheck.lower() == "y" or filewritecheck.lower() == "yes":
                
                writelist = []
                
                filewrite = open("patient_file.txt","w")
                for i in patients:
                    filewrite.write(("{}|{}|{}|{}|{}|{}|{}|\n".format(i.first_name,i.surname,i.age,i.mobile,i.postcode,i.symptoms,i.family)))
            else:
                print("Data not uploaded")
                
            
            running = False
            # 6 - Quit
            #ToDo5
            pass

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

    

if __name__ == '__main__':
    main()
