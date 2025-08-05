estudiantes={}

def registrar_estudiante():
    global estudiantes

    id_est=input("Ingrese la id del estudiante: ")
    nom_est=str(input("Ingrese el nombre del estudiante: "))
    carrera_progra=input("Ingrese la carrera/programa académico: ")
    estudiantes[id_est]={
        "ID":id_est,
        "Nombre":nom_est,
        "Carrera":carrera_progra,
    }

def agregar_notas():
    global estudiantes
    notas={}
    id_buscar=input("Ingrese su ID de estudiante: ")
    if id_buscar in estudiantes:
        aprobado="Perdido"
        curso_nom=str(input("Ingrese del curso a añadir: "))
        nota_curso=int(input(f"Ingrese la nota de {curso_nom}: : "))

        if nota_curso>=61:
            aprobado="Aprobado"

        notas[curso_nom]={
            "Nota:":nota_curso,
            "Aprobado":aprobado,
        }

        estudiantes[id_buscar]={
            "Curso":notas,
        }

print("---PORTAL ACADÉMICO---")
print("\n1. Agregar estudiante")
print("2. Agregar curso con nota")
print("3. Consultar estudiante")
print("4. Calcular promedio")
print("5. Verificación de aprobación")
print("6. Mostrar todos los registros")
print("7. Salir")

opcion=input("Seleccione una opción: ")

match opcion:
    case "1":
        print("\nEscogio 'Agregar estudiantes' ")
        registrar_estudiante()
    case "2":
        print("\nEscogio 'Agregar cursos con nota' ")
        agregar_notas()
    case "3":
        print("\nEscogio 'Consultar estudiantes' ")



