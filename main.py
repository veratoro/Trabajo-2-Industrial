from argparse import ArgumentParser, Namespace

from university_system import (
    StudentsDatabase,
    TeachersDatabase,
    get_students_metrics,
    get_teachers_metrics
)

def execute(args: Namespace) -> None:
    database = None
    if args.database_name == "students":
        database = StudentsDatabase()
    if args.database_name == "teachers":
        database = TeachersDatabase()

    while True:
        # Estudiante: primer nombre, edad, semestre
        # Profesores: primer nombre, edad, salario 
        # la letra e identifica estudiantes y la letra p profesores

        user_input = input("Ingrese los datos del individuo: ")

        identifier, first_name, age, semester_or_salary = user_input.split("")
        
        if identifier =="e":
            person_id = database.create({
                "first_name": first_name,
                "age": int(age),
                "semester": int(semester_or_salary)
            })

            get_students_metrics(database)

        if identifier =="p":
            person_id = database.create({
                "first_name": first_name,
                "age": int(age),
                "salary": float(semester_or_salary)
            })

            get_teachers_metrics(database)
       

def main() -> None:
    parser = ArgumentParser()

    parser.add_argument( 
        ".dn","--database-name", type=str,
        choises=["students","teachers","others"]
    )

    args = parser.parse_args()
    execute(args)

if __name__ == "__main__":
    main()