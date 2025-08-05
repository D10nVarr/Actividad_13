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
        curso_nom=str(input("Ingrese del curso a añadir: "))
        nota_curso=int(input(f"Ingrese la nota de {curso_nom}: : "))

        notas[curso_nom]={
            "Nota:":nota_curso,
        }

        estudiantes[id_buscar]={
            "Curso":notas,
        }

print("---PORTAL ACADÉMICO---")
print("1. Agregar estudiante")
print("2. Agregar curso con nota")



