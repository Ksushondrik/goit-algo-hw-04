import re

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

total, average = total_salary("documents/monthly_salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:.0f}")

cats_info = get_cats_info("documents/cats_ident.txt")
print(cats_info)