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

def getGradePoint(score):
	if (score >= 70):
		return 5
	elif (score >= 60):
		return 4
	elif (score >= 50):
		return 3
	elif (score >= 45):
		return 2
	elif (score >= 40):
		return 1
	else:
		return 0

# Calculate eavh semester SGPA
def SGPA(courses):
	aggregate = 0
	units = 0
	for each in courses:
		units += each[1]
		point = getGradePoint(each[2])
		if (point != 0): aggregate += point * each[1]
		
	return aggregate / units
	#print(each)

def CGPA(sgpa1, sgpa2):
	return (sgpa1 + sgpa2)/2

def start ():
	if (len(student["1"]) > 0 and len(student["2"]) > 0):
		sgpa1 = SGPA(student["1"])
		sgpa2 = SGPA(student["2"])
		cgpa = CGPA(sgpa1, sgpa2)
		
		# Display results
		print("\n=====================================")
		print("Your SGPA for first semester is " + str(sgpa1))
		print("Your SGPA for second semester is " + str(sgpa2))
		print("Your CGPA is " + str(cgpa))
		print("=====================================/n")
		return
	
	
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
		else :
			print("): You entered the wrong number. Try again")
	except:
		print("Wrong! You didn't enter a number")
		start()
	start()

start()