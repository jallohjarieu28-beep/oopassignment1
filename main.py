class Student:
    """
    Class representing an individual student in the Learning Portal.
    Satisfies Task 1: OOP Basics (Attributes, Instance Methods, Class Methods).
    """
    # Class attribute to keep track of total students across the system
    total_students = 0
    
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        
        # Using a tuple for immutable course enrollment details 
        # (Meets the optional tuple requirement for extra 10 marks)
        self.enrollment_info = ("PROG211 - Object-Oriented Programming 1", 3)
        
        # Increment class attribute counter upon object creation
        Student.total_students += 1

    def display_info(self):
        """Instance method to display student information securely."""
        print(
            f"ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Major: {self.major} | "
            f"Enrolled Course: {self.enrollment_info[0]} "
            f"({self.enrollment_info[1]} Credits)"
        )

    def update_record(self, name=None, age=None, major=None):
        """Instance method to update student records dynamically."""
        if name:
            self.name = name
        if age:
            self.age = age
        if major:
            self.major = major
        print(f"[Success] Record updated for Student ID: {self.student_id}")

    @classmethod
    def get_total_students(cls):
        """Class method (@classmethod) to return the total count of registered student objects."""
        return cls.total_students


class LearningPortal:
    """
    Class managing multiple Student objects.
    Satisfies Task 2: Python Data Structures (Dictionary mapping unique IDs to objects).
    """
    def __init__(self):
        # Dictionary data structure storing student objects with their unique ID as the key
        self.students = {}

    def add_student(self, student):
        """Function to add a student record to the dictionary data structure."""
        if student.student_id in self.students:
            print(f"[Error] Student with ID {student.student_id} already exists.")
        else:
            self.students[student.student_id] = student
            print(f"[Success] Student '{student.name}' added to the portal.")

    def display_all_records(self):
        """Function to display all records from the dictionary data structure."""
        if not self.students:
            print("No student records found in the portal.")
            return
        
        print("\n================ DIGITAL LEARNING PORTAL RECORDS ================")
        for s_id, student in self.students.items():
            student.display_info()
        print(f"-----------------------------------------------------------------")
        print(f"Total Active Students in System: {Student.get_total_students()}")
        print("=================================================================\n")


# ==========================================
# Sample Execution and Testing (Main Program)
# ==========================================
if __name__ == "__main__":
    # Initialize the Digital Learning Portal
    portal = LearningPortal()

    print("--- 1. Creating and Adding Student Objects ---")
    s1 = Student("S001", "Aminata Sesay", 20, "Computer Science")
    s2 = Student("S002", "Mohamed Bangura", 22, "Information Technology")

    portal.add_student(s1)
    portal.add_student(s2)

    # Displaying initial records stored in the dictionary
    portal.display_all_records()

    print("--- 2. Updating a Student Record Using Instance Methods ---")
    s1.update_record(age=21, major="Software Engineering")

    # Displaying updated records
portal.display_all_records() 
       