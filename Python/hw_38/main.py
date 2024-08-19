from hw_38.get_config import get_db_config

from hw_38.Connector import connector

columns = {"users": ["id", "name", "age"],
           "product": ["pid", "prod", "quantity"],
           "sales": ["sid", "pid", "id"]}


def input_columns(table):
    fields = input(
        f"Выберите одно или несколько полей {columns[table]} этой таблицы или введите * для выбора всех: ").strip().split()

    if fields == ["*"]:
        return f"SELECT * FROM {table}"

    if not set(fields).issubset(columns[table]):
        print("Введено некорректное значение. Будет использовано значение * ")
        return f"SELECT * FROM {table}"
    if len(fields) == 1:
        field = fields[0]

        value = input(
            f"Введите искомое значение поля {field} таблицы {table} или '0', если нужно вывести все значения: ")
        if value != "0":
            if field == 'name':
                sign = 'LIKE'
                value = '%' + value + '%'
            elif field == 'age':
                sign = input(f"Введите знак -больше, меньше или равно: ").strip()
                if sign not in ["<", ">", ">=", "<=", "="]:
                    print("Введено некорректное значение. Будет использовано значение = ")
                    sign = "="
            return f"SELECT * FROM {table} WHERE {field} {sign} '{value}';"

        else:
            return f"SELECT * FROM {table}"
    return f"SELECT {','.join(fields)} FROM {table};"


if __name__ == '__main__':
    conection, cursor = connector(get_db_config())
    while True:
        table_name = "users"
        query = input_columns(table_name)
        print(query)

        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)

    cursor.close()
    connection.close()
