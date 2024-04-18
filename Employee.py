class Employee:
    def __init__(self, name, age, department, email, position):
        self.name = name
        self.age = age
        self.department = department
        self.email = email
        self.position = position
        self.performance_scores = []
        self.performance_history = []  # To track performance trends

    def add_performance_score(self, score):
        self.performance_scores.append(score)
        self.performance_history.append(score)

    def calculate_overall_performance(self):
        if not self.performance_scores:
            return 0
        return sum(self.performance_scores) / len(self.performance_scores)

    def evaluate_performance(self):
        overall_performance = self.calculate_overall_performance()
        if overall_performance >= 90:
            return "Outstanding"
        elif overall_performance >= 80:
            return "Excellent"
        elif overall_performance >= 70:
            return "Good"
        elif overall_performance >= 60:
            return "Needs Improvement"
        else:
            return "Poor"

    def generate_performance_report(self):
        report = f"Performance Report for {self.name}:\n"
        report += f"Age: {self.age}\n"
        report += f"Department: {self.department}\n"
        report += f"Email: {self.email}\n"
        report += f"Position: {self.position}\n"
        report += "Performance Scores:\n"
        for i, score in enumerate(self.performance_scores, start=1):
            report += f" - Score {i}: {score}\n"
        report += f"Overall Performance: {self.evaluate_performance()}\n"
        return report


def main():
    employees = []

    while True:
        print("\nEmployee Performance Evaluation System")
        print("1. Add Employee")
        print("2. Add Performance Score")
        print("3. Evaluate Employee")
        print("4. View Performance Trends")
        print("5. Generate Performance Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            age = input("Enter employee age: ")
            department = input("Enter employee department: ")
            email = input("Enter employee email: ")
            position = input("Enter employee position: ")
            employee = Employee(name, age, department, email, position)
            employees.append(employee)
            print("Employee added successfully!")
        elif choice == "2":
            name = input("Enter employee name: ")
            score = float(input("Enter performance score (0-100): "))
            for employee in employees:
                if employee.name.lower() == name.lower():
                    employee.add_performance_score(score)
                    print("Performance score added successfully!")
                    break
            else:
                print("Employee not found!")
        elif choice == "3":
            name = input("Enter employee name: ")
            for employee in employees:
                if employee.name.lower() == name.lower():
                    performance = employee.evaluate_performance()
                    print(f"{employee.name} from {employee.department} department has {performance} performance.")
                    break
            else:
                print("Employee not found!")
        elif choice == "4":
            name = input("Enter employee name: ")
            for employee in employees:
                if employee.name.lower() == name.lower():
                    print(f"Performance trends for {employee.name}: {employee.performance_history}")
                    break
            else:
                print("Employee not found!")
        elif choice == "5":
            name = input("Enter employee name: ")
            for employee in employees:
                if employee.name.lower() == name.lower():
                    print(employee.generate_performance_report())
                    break
            else:
                print("Employee not found!")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()