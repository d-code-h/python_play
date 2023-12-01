# ReadMe
#
#
#

# Welcome message
print("Welcome to CGPA Calculator\n")

student = {
    "1": [],
    "2": []
  }


def courseDetails():
  name = input("Enter course name: ")
  unit = input("Course unit in numbers: ")
  score = input("Score (Total score over 100 in numbers): ")

  return [name, unit, score]

def start ():
  print(student)
  semester = input('Enter your choice semester. \n\n1 = First Semester \n2 = Second Semester\n')

  print(len(student[semester]))
  try:
    # semester = int(semester)
    print()
    if len(student[semester]) == 0:
   # if semester == 1:
      courseCount = int(input("How many courses did you offer? (Respond with number): "))
      
      for i in range(1,courseCount+1):
        # Get course details
        print("\n=====================")
        print("Details of course " + str(i))
        print("=====================")
        course = courseDetails()
        #print(course)
        try:
          course[1] = int(course[1])
          course[2] = int(course[2])
          index = str(semester)
          student[index].append(course)

        except:
          print("Wrong! You didn't enter a number either on unit or score")
          course = courseDetails()
      print("\n=====================")
        
      print("Done with semester " + semester + "")
      print("=====================\n") 
      
    #elif a == 2:
    elif len(student[semester]) > 0:
        print("Sorry, you have added the courses for this semester. Enter the courses for the other semester now. ")
      #print("Wow! You are almost leaving")
    else:
      print("): You entered the wrong number. Try again")
  except:
    print("Wrong! You didn't enter a number")
    start()
  start()

start()