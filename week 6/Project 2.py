admitted = []
not_admitted = []


def check_admission():
    name = input("Enter candidate's name: ")
    department = input(
        "Enter department (Computer Science / Mass Communication): ").strip().lower()
    jamb_score = int(input("Enter JAMB score: "))
    credits = int(input("Enter number of credits in key subjects: "))
    interview = input(
        "Did the candidate pass the interview? (yes/no): ").strip().lower()

    if department == "computer science":
        if jamb_score >= 250 and credits >= 5 and interview == "yes":
            admitted.append(name)
            print(f"{name} has been admitted into the Computer Science department.")
        else:
            not_admitted.append(name)
            print(f"{name} was NOT admitted into the Computer Science department.")

    elif department == "mass communication":
        if jamb_score >= 230 and credits >= 5 and interview == "yes":
            admitted.append(name)
            print(f"{name} has been admitted into the Mass Communication department.")
        else:
            not_admitted.append(name)
            print(f"{name} was NOT admitted into the Mass Communication department.")

    else:
        print("Invalid department entered. Please try again.")


# Allow multiple entries
while True:
    check_admission()
    more = input(
        "Do you want to check another candidate? (yes/no): ").strip().lower()
    if more != "yes":
        break

print("\n=== ADMISSION RESULTS ===")
print("Admitted candidates:", admitted)
print("Not admitted candidates:", not_admitted)
