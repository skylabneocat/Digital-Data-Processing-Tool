from tkinter import *
from tkinter import messagebox, simpledialog
from collections import deque
import os

# New fix ↓↓↓↓↓↓

filename = "students.txt"

# Check if the file exists
if not os.path.isfile(filename):
    with open(filename, "w") as f:
        print(f"{filename} not found. Creating new file.")
        # Optionally write initial content here
        # f.write("ID,Name,Age\n")
else:
    print(f"{filename} found.")

# Continue with the rest of your program
# For example, reading from students.txt
with open(filename, "r") as f:
    data = f.read()
    print("File contents:")
    print(data)


def number_system_converter(decimal):
	try:	
		# Handle special case for zero
		if decimal == 0:
			return {
				"binary": "0",
				"octal": "0",
				"hexadecimal": "0"
			}

		# Binary conversion
		binary_result = ""
		temp = decimal
		while temp > 0:
			bit = temp % 2
			binary_result = str(bit) + binary_result
			temp = temp // 2

		# Octal conversion
		octal_result = ""
		temp = decimal
		while temp > 0:
			digit = temp % 8
			octal_result = str(digit) + octal_result
			temp = temp // 8

		# Hexadecimal conversion
		hex_digits = "0123456789ABCDEF"
		hex_result = ""
		temp = decimal
		while temp > 0:
			digit = temp % 16
			hex_result = hex_digits[digit] + hex_result
			temp = temp // 16

		# Return everything in a dictionary
		return {
			"binary": binary_result,
			"octal": octal_result,
			"hexadecimal": hex_result
		}
	except ValueError:
		print(f'Invalid input')

def floating_point_representation(decimal):
	# Here, the sign bit is determined
	if decimal >= 0:
		sign = 0
	else:
		sign = 1
		decimal = abs(decimal)

	# Special case for zero
	if decimal == 0:
		return {
			"ieee754": "0" * 32,
			"int_binary": "0",
			"frac_binary": "0"
		}

	# Seperated into integer and fractional parts
	int_part = int(decimal)
	frac_part = decimal - int_part

	# Converting integer part into binary
	int_binary = bin(int_part)[2:]

	# Converting fractional part into binary
	frac_binary = ''
	f = frac_part
	while len(frac_binary) < 23 and f != 0:
		f *= 2
		bit = int(f)
		frac_binary += str(bit)
		f -= bit

	# Calculate exponent, the bias is 127
	exp = len(int_binary) - 1
	exponent = bin(127 + exp)[2:].zfill(8)

	# Construct mantissa
	mantissa = (int_binary[1:] + frac_binary).ljust(23, '0')[:23]
	
	# Return everything in a dictionary
	return {
		"ieee754": str(sign) + exponent + mantissa,
		"int_binary": int_binary,
		"frac_binary": frac_binary
	}


def recursive_calculations(num):
    # Recursive function to calculate the factorial
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
	
	# Another recursive function that generates the fibonnaci number
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
	
	# Return results
    print(f"\nFactorial of {num} is:", factorial(num))
    
    print(f"Fibonacci sequence up to {num}:")
    for i in range(num):
        print(fibonacci(i), end=" ")

def student_records_management():
    #This reads records from a file into a list of dictionaries
    students = []
    with open("students.txt", "r") as file:
        for line in file:
            name, student_id, grade = line.strip().split(',')
            students.append({"name": name, "id": student_id, "grade": float(grade)})

    #Should search by name or ID
    def search_student(key):
        for student in students:
            if student["name"] == key or student["id"] == key:
                return student
        return "Student not found."

    #Funcionality to sort by grade
    def sort_by_grade():
        for i in range(1, len(students)):
            key = students[i]
            j = i - 1
            while j >= 0 and students[j]["grade"] > key["grade"]:
                students[j + 1] = students[j]
                j -= 1
            students[j + 1] = key

    # Updates student information
    def update_student(student_id, new_name=None, new_grade=None):
        for student in students:
            if student["id"] == student_id:
                if new_name:
                    student["name"] = new_name
                if new_grade is not None:
                    student["grade"] = float(new_grade)
                return "Student updated."
        return "Student not found."

    # Removes student from database
    def delete_student(student_id):
        for i, student in enumerate(students):
            if student["id"] == student_id:
                del students[i]
                return "Student deleted."
        return "Student not found."


def student_records_management_enhancement():
    # Head of this linked list
    first_student = None

    # Recently accessed students stack
    recent_access = []

    # Adds a wating queue for student-related requests
    student_queue = deque()

    # This creates a new student record
    def make_record(name, student_id, grade):
        return {"name": name, "id": student_id, "grade": grade, "next": None}

    # Load student data from a file line by line
    def read_from_file(file_name):
        nonlocal first_student
        try:
            with open(file_name, 'r') as f:
                lines = f.readlines()
                for info in lines:
                    parts = info.strip().split(',')
                    if len(parts) == 3:
                        name, sid, grade = parts[0], parts[1], float(parts[2])
                        node = make_record(name, sid, grade)
                        node["next"] = first_student
                        first_student = node
        except FileNotFoundError:
            print("File not found.")

    # Simple search using either ID or name
    def find_student(search_key):
        current = first_student
        while current:
            if current["name"] == search_key or current["id"] == search_key:
                recent_access.append(current)
                return current
            current = current["next"]
        return None

    # Add a request to the previous queue
    def enqueue_request(task):
        student_queue.append(task)

    def handle_next_request():
        if student_queue:
            return student_queue.popleft()
        return "No pending requests."

    # All results are returned into one dictionary from outside
    return {
        "load": read_from_file,
        "search": find_student,
        "add_request": enqueue_request,
        "process_request": handle_next_request,
        "stack": recent_access,
        "queue": student_queue
    }


# Full GUI setup

def main_gui():
    def on_choice(choice):
        if choice == "1":
            # Number system conversion dialog and result display
            try:
                value = int(simpledialog.askstring("Input", "Enter a decimal number:"))
                results = number_system_converter(value)
                output = f"Binary: {results['binary']}\nOctal: {results['octal']}\nHexadecimal: {results['hexadecimal']}"
                messagebox.showinfo("Number System Conversion", output)
            except:
                messagebox.showerror("Error", "Invalid input. Please enter an integer.")

        elif choice == "2":
            # Floating-point representation dialog and result display
            try:
                value = float(simpledialog.askstring("Input", "Enter a decimal number:"))
                results = floating_point_representation(value)
                output = (f"IEEE 754: {results['ieee754']}\n"
                          f"Integer Binary: {results['int_binary']}\n"
                          f"Fractional Binary: {results['frac_binary']}")
                messagebox.showinfo("Floating-Point Representation", output)
            except:
                messagebox.showerror("Error", "Invalid input. Please enter a number.")

        elif choice == "3":
            # Recursive calculations: factorial and Fibonacci
            try:
                value = int(simpledialog.askstring("Input", "Enter a number for recursion functions:"))
                top = Toplevel()
                top.title("Recursive Calculations")
                top.configure(bg="#f0f5f9")
                result_text = Text(top, width=60, height=10, bg="#e6f2ff", fg="#003366", font=("Courier", 11))
                result_text.pack(padx=10, pady=10)

                def factorial(n):
                    if n == 0 or n == 1:
                        return 1
                    return n * factorial(n - 1)

                def fibonacci(n):
                    if n == 0:
                        return 0
                    elif n == 1:
                        return 1
                    return fibonacci(n - 1) + fibonacci(n - 2)

                result_text.insert(END, f"Factorial of {value}: {factorial(value)}\n")
                result_text.insert(END, f"Fibonacci sequence up to {value}: ")
                for i in range(value):
                    result_text.insert(END, str(fibonacci(i)) + " ")
            except:
                messagebox.showerror("Error", "Please enter a valid integer.")

        elif choice == "4":
            # Enhanced Student Records Management GUI
            try:
                top = Toplevel()
                top.title("Student Records Management")
                top.configure(bg="#f0f5f9")

                # Text widget to show records
                text = Text(top, width=80, height=20, bg="#e6ffe6", fg="#003300", font=("Courier", 11))
                text.pack(padx=10, pady=10)

                students = []
                with open("students.txt", "r") as file:
                    for line in file:
                        name, student_id, grade = line.strip().split(',')
                        students.append({"name": name, "id": student_id, "grade": float(grade)})

                def refresh_display():
                    text.delete(1.0, END)
                    text.insert(END, f"Loaded {len(students)} student(s):\n\n")
                    for s in students:
                        text.insert(END, f"Name: {s['name']}, ID: {s['id']}, Grade: {s['grade']}\n")

                def save_to_file():
                    with open("students.txt", "w") as f:
                        for s in students:
                            f.write(f"{s['name']},{s['id']},{s['grade']}\n")

                def add_student():
                    name = simpledialog.askstring("Add Student", "Enter name:")
                    sid = simpledialog.askstring("Add Student", "Enter ID:")
                    grade = simpledialog.askfloat("Add Student", "Enter grade:")
                    if name and sid and grade is not None:
                        students.append({"name": name, "id": sid, "grade": grade})
                        save_to_file()
                        refresh_display()

                def update_student():
                    sid = simpledialog.askstring("Update Student", "Enter ID to update:")
                    for s in students:
                        if s["id"] == sid:
                            new_name = simpledialog.askstring("Update Student", f"Enter new name (current: {s['name']}):")
                            new_grade = simpledialog.askfloat("Update Student", f"Enter new grade (current: {s['grade']}):")
                            if new_name:
                                s["name"] = new_name
                            if new_grade is not None:
                                s["grade"] = new_grade
                            save_to_file()
                            refresh_display()
                            return
                    messagebox.showinfo("Update", "Student ID not found.")

                def delete_student():
                    sid = simpledialog.askstring("Delete Student", "Enter ID to delete:")
                    for i, s in enumerate(students):
                        if s["id"] == sid:
                            del students[i]
                            save_to_file()
                            refresh_display()
                            return
                    messagebox.showinfo("Delete", "Student ID not found.")

                def search_student():
                    key = simpledialog.askstring("Search", "Enter name or ID to search:")
                    result = [s for s in students if s["name"] == key or s["id"] == key]
                    if result:
                        msg = "\n".join([f"Name: {s['name']}, ID: {s['id']}, Grade: {s['grade']}" for s in result])
                        messagebox.showinfo("Search Results", msg)
                    else:
                        messagebox.showinfo("Search", "Student not found.")

                # Add control buttons
                frame = Frame(top, bg="#f0f5f9")
                frame.pack(pady=10)

                Button(frame, text="Add", width=10, command=add_student).grid(row=0, column=0, padx=5)
                Button(frame, text="Update", width=10, command=update_student).grid(row=0, column=1, padx=5)
                Button(frame, text="Delete", width=10, command=delete_student).grid(row=0, column=2, padx=5)
                Button(frame, text="Search", width=10, command=search_student).grid(row=0, column=3, padx=5)

                refresh_display()
                
            except FileNotFoundError:
                messagebox.showerror("Error", "students.txt not found.")


        elif choice == "5":
            root.destroy()

    root = Tk()
    root.title("Digital Data Processing Tool")
    root.geometry("420x400")
    root.configure(bg="#d9edf7")

    Label(root, text="Welcome to the Digital Data Processing Tool!", font=("Helvetica", 14, "bold"), bg="#d9edf7", fg="#31708f").pack(pady=15)

    options = [
        ("1", "Number System Conversion"),
        ("2", "Integer & Floating-Point Representation"),
        ("3", "Recursive Calculations"),
        ("4", "Student Records Management"),
        ("5", "Exit")
    ]

    for val, text_label in options:
        Button(root, text=text_label, width=35, font=("Helvetica", 11), bg="#31708f", fg="white", activebackground="#5bc0de", command=lambda v=val: on_choice(v)).pack(pady=6)

    root.mainloop()

# Launch the GUI
main_gui()

