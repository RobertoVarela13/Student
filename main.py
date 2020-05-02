from student import student
edades=[12,15,13,20,17]
nombres=[["Jose", 2], ["Andres", 2], ["Diana" , 1], ["Elsy", 1], ["Nicole", 1]]
estudiantes=[ edades]

lista_muj=[]
lista_hom=[]

def Menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Que opcion deseas?....: "))
            correcto=True
        except ValueError:
            print('Esa no es una opcion, intenta de nuevo')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("\n \n1. Imprimir la lista de estudiantes")
    print ("2. Separar por generos a los estudiantes")
    print ("3. Ver la lista de edades de mayor a menor")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = Menu()
 
    if opcion == 1:
      for element in nombres:
       estudiantes.append(element[0])
      print("La lista de estudiantes es\n")
      print(estudiantes)
    elif opcion == 2:
        for element in nombres:
          if element[1]==1:
           lista_muj.append(element[0])
          else: lista_hom.append(element[0]) 
        print("Hombres", lista_hom)
        print("\nMujeres", lista_muj)
    elif opcion == 3:
        print (sorted(edades, reverse=True))
         

    elif opcion == 4:
        salir = True
    else:
        print ("Esa no es una opcion, intenta de nuevo")
 
print ("Fin")

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
