from student import student


def crea_estudiantes(count_estudiantes):
	count = 0
	list_students = []
	
	while count < int(count_estudiantes):

		student_code = input("dame la matricula: ")
		student_name = input("dame el nombre: ")
		student_age = input("dame la edad: ")
		student_gender = input("dame el genero: ")
		student_carreer = input("dame la carrera: ")
		
		list_students.append(student(student_code,student_name,student_age,student_gender,student_carreer))
		
		count = count + 1
	return list_students

    
def ordena_edades(list_students):
    
	print ("metodo vacio")

def separa_generos(list_students):
    list_male = []
    list_female=[]
    
    for student in list_students:
        
        	if student.gender==m:
            list_male.append(student())
         return list_male
    
        else:
            
            list_female.append(student())
         return list_female

def main():
	
	options = 1
	list_stud = []

	while options != "0":
		options = input("menu opciones 1. crea estudiantes - 2.ordena edades - 3.separa generos - 0. salir: ")

		if options == "1":
			print("crea estudiantes")
			count_x = input("cuantos estudiantes daremos de alta: ")
			list_stud = crea_estudiantes(count_x)

		if options == "2":
			print("ordena edades")
            

		if options == "3":
			print("separa generos")
            fm=input("M es para masculino, f es para femenino")
            list_stud=separa_generos(fm)

if __name__ == "__main__":
	main()
