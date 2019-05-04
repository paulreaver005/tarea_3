# Para definir la agenda del hospital
agenda_hospital = []
persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')
# agregamos una persona
agenda_hospital.append(persona)
# podemos revisar cual es el estatus de la agenda
#print(agenda_hospital)

# viene otra persona
persona = ('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta')
# agregamos otra persona
agenda_hospital.append(persona)
# podemos revisar cual es el estatus de la agenda
#print(agenda_hospital)

persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]

# Podemos agregar esas personas que vienen todos de una sola vez
agenda_hospital.extend(persona)

#print(agenda_hospital)

for paciente in agenda_hospital:
    print(paciente)



#Cuantos pacientes llegaron en total?
cantidadpacientes = 0
for persona in agenda_hospital:
     cantidadpacientes += agenda_hospital.count(persona)
print('\nLa cantidad de pacientes que llegaron en total son: ', cantidadpacientes)


#Cuantas personas llegaron por dolor?
dolor = 0
for personadolor in agenda_hospital:
     dolor += personadolor.count('dolor')
print('\nLa cantidad de pacientes que llegaron por dolor son: ', dolor)

#Suponga que se atienden con orden de prioridad por edad, empezando por el adulto mayor. Ordene la lista desde el más adulto al más joven
def orden(elem):
    return elem[3]
agenda_hospital.sort(key=orden, reverse=True)

print('\nLa lista ordenada de pacientes de mayor a menor es: ')
for paciente in agenda_hospital:
    print(paciente)

#Cuantos pacientes son mayores de edad? cuantos menores?

edades = []
menor = 0
mayor = 0
for edad in agenda_hospital:
    edades.append(edad[3])

for todasedades in edades:
   menor += todasedades >= 18
   mayor += todasedades <= 18

print('\nLa cantidad de pacientes menores de edad son: ', menor)
print('\nLa cantidad de pacientes mayores de edad son: ', mayor)

#Suponga que se atienden con orden de prioridad por gravedad de consulta, empezando
#por los que tienen dolor y luego por edad (mas viejo al joven), empezando por el
#adulto mayor. Ordene la lista empenzando por los que tienen mayor prioridad.
def estado(elem1):
    return elem1[5]
agenda_hospital.sort(key=estado, reverse=True)
print('\nLa lista ordenada de pacientes por orden de prioridad es: ')
for paciente in agenda_hospital:
    print(paciente)

#Suponga que los que tienen dolor mueren :( Como queda la lista de pacientes vivos por atender ordenados por orden de edad desde el joven al viejo.


for personaFallecida in agenda_hospital:
    fallecido = personaFallecida.count('dolor')
    if fallecido > 1:
        agenda_hospital.remove(personaFallecida)
        fallecido = 0


print('\nLa lista ordenada de pacientes quitando los fallecidos es: ')
for pacientesinFallecidos in agenda_hospital:
    print(pacientesinFallecidos)