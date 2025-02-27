import tkinter as tk
from tkinter import ttk, messagebox

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        if not self.grades:
            return 0.0
        total = sum(self.grades.values())
        return total / len(self.grades)

    def determine_letter_grade(self, average):
        if average >= 90:
            return 'A+'
        elif average >= 80:
            return 'A'
        elif average >= 70:
            return 'B+'
        elif average >= 60:
            return 'B'
        elif average >= 50:
            return 'C'
        elif average >= 40:
            return 'D'
        elif average >= 33:
            return 'E'
        else:
            return 'F'

    def determine_gpa(self, average):
        if average >= 90:
            return 10.0
        elif average >= 80:
            return 9.0
        elif average >= 70:
            return 8.0
        elif average >= 60:
            return 7.0
        elif average >= 50:
            return 6.0
        elif average >= 40:
            return 5.0
        elif average >= 33:
            return 4.0
        else:
            return 0.0

class GradeManager:
    def __init__(self, root):
        self.students = {}
        
        self.root = root
        self.root.title("Student Grade Manager")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Student name input
        self.student_name_label = tk.Label(self.root, text="Student Name:")
        self.student_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.student_name_entry = tk.Entry(self.root)
        self.student_name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Subject input
        self.subject_label = tk.Label(self.root, text="Subject:")
        self.subject_label.grid(row=1, column=0, padx=10, pady=10)
        self.subject_entry = tk.Entry(self.root)
        self.subject_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Grade input
        self.grade_label = tk.Label(self.root, text="Grade:")
        self.grade_label.grid(row=2, column=0, padx=10, pady=10)
        self.grade_entry = tk.Entry(self.root)
        self.grade_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Buttons
        self.add_grade_button = tk.Button(self.root, text="Add Grade", command=self.add_grade)
        self.add_grade_button.grid(row=3, column=0, padx=10, pady=10)
        self.show_report_button = tk.Button(self.root, text="Show Report Card", command=self.show_report)
        self.show_report_button.grid(row=3, column=1, padx=10, pady=10)
        
        # Report display
        self.tree = self.student_name_entry.get().strip()
        self.tree = ttk.Treeview(self.root, columns=("Subject", "Grade", "Average", "Letter Grade", "GPA"), show="headings")
        self.tree.heading("Subject", text="Subject")
        self.tree.heading("Grade", text="Grade")
        self.tree.heading("Average", text="Average")
        self.tree.heading("Letter Grade", text="Letter Grade")
        self.tree.heading("GPA", text="GPA")
        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
    def add_grade(self):
        student_name = self.student_name_entry.get().strip()
        subject = self.subject_entry.get().strip()
        try:
            grade = float(self.grade_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid input", "Grade must be a number.")
            return

        if not student_name or not subject:
            messagebox.showerror("Invalid input", "Student name and subject are required.")
            return
        
        if student_name not in self.students:
            self.students[student_name] = Student(student_name)
        
        self.students[student_name].add_grade(subject, grade)
        messagebox.showinfo("Success", f"Added grade for {student_name} in {subject}.")
        
    def show_report(self):
        for student_name, student in self.students.items():
            self.tree.insert("", "end", values=("Student", student_name, "", "", ""))
            average = student.calculate_average()
            letter_grade = student.determine_letter_grade(average)
            gpa = student.determine_gpa(average)
            for subject, grade in student.grades.items():
                self.tree.insert("", "end", values=(subject, grade, average, letter_grade, gpa))
            self.tree.insert("", "end", values=("", "", "", "", ""))
        

def main():
    root = tk.Tk()
    app = GradeManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
