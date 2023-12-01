# ReadMe
#
#
#

# Welcome message
print("Welcome to CGPA Calculator\n")

def courseDetails():
  name = input("Enter course name: ")
  unit = input("Course unit in numbers: ")
  score = input("Score (Total score over 100 in numbers): ")

  return [name, unit, score]

def start ():
  semester = input('Enter your choice semester. \n\n1 = First Semester \n2 = Second Semester\n')

  student = {
    "1": [],
    "2": []
  }

  try:
    semester = int(semester)
    if semester == 1:
      courseCount = int(input("How many courses did you offer? (Respond with number): "))
      
      for i in range(1,courseCount):
        # Get course details
        print("Details of course " + str(i))
        course = courseDetails()
        print(course)
        try:
          course[1] = int(course[1])
          course[2] = int(course[2])
          index = str(semester)
          student[index].append(course)

          print(index)
          print(student)
        except:
          print("Wrong! You didn't enter a number either on unit or score")
          course = courseDetails()


    elif a == 2:
      print("Wow! You are almost leaving")
    else:
      print("): You entered the wrong number. Try again")
  except:
    print("Wrong! You didn't enter a number")
    start()

start()