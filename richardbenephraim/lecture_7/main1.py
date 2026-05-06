
class SchoolForm:
    def __init__(self):
        self.name = "Software Development"
        self.year = "1 year"



class StudentForm(SchoolForm):
    def __init__(self):
        super().__init__()



openlabsapp = SchoolForm()
openlabsweb = SchoolForm()

print(openlabsapp.name)


software = StudentForm()
network = StudentForm()



