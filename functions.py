import re
import decor

def total_salary(path): # Перше завдання
    n = 0
    total = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.read()
            for zp in re.finditer(r'\d+', lines):
                zp = int(zp.group())
                total += zp
                n += 1
            if n != 0:
                average = total / n
            else:
                average = 0
    except Exception as e:
        print(f"Error: {e}")
        total = 0
        average = 0
    return (total, average,)

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.read()
            matches = re.findall(r"(\w+),([a-zA-Z]+),(\d+)", lines)
            if matches:
                for match in matches:
                    cat = {"id": match[0], "name": match[1], "age": match[2]}
                    cats_info.append(cat)
    except Exception as e:
        print(f"Error: {e}")
    return cats_info

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@decor.input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact (args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def show_phone (args, contacts):
    name = args[0]
    return f"Pfone {name}: {contacts[name]}"

def show_all (contacts):
    for key, value in contacts.items():
        print(f"{key}: {value}")
    return "These are all contacts"

if __name__ == "__main__":
    total, average = total_salary("documents/monthly_salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:.0f}")

    cats_info = get_cats_info("documents/cats_ident.txt")
    print(cats_info)