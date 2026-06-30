class Student:
    def __init__(self,name,age,roll_no,field_of_study):
        self.name=name
        self.age=age
        self.roll_no=roll_no
        self.field_of_study=field_of_study
        self.subjects=[]
        self.grades={}

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Field of Study: {self.field_of_study}")
        for subject,grade in self.grades.items():
            print(subject,grade)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "roll_no": self.roll_no,
            "field_of_study": self.field_of_study,
            "subjects": self.subjects,
            "grades": self.grades
        }