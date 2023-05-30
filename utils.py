import csv


def get_csv_data(data_path):
    user_data_list: list = []

    with open(data_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_data_list.append({
                "nombre": row["nombre"],
                "apellido": row["apellido"],
                "ciudad": row["ciudad"],
                "pais": row["pais"],
                "edad": row["edad"],
                "carrera": row["carrera"]
                })

    return user_data_list
