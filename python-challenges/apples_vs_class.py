apples = int(input("Number of apples:"))
class_size = int(input("Number of students"))

if apples >= class_size:
    print("There are enough apples for each student to have one")

    if apples >= (class_size * 2):
        print("There are enough apples for each student to have two")
        print("There would be " + str(apples - (class_size * 2)) + " apples left over if each student had two.")

if apples < class_size:
    print("We are short " + str(class_size - apples) + " apples for each person to have one.")

    if apples == (class_size - round(class_size / 3)):
        print("If a third of the class doesn't get an apple, the rest of the class would get one")

print(round(10/3))