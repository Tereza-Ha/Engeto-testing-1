tasks = []

# fukce
# spuštění menu
def hlavni_menu():
    if __name__ == "__main__":
        while True:
            print('\nSprávce úkolů - Hlavní menu\n 1. Přidat nový úkol\n 2. Zobrazit všechny úkoly\n 3. Odstranit úkol\n 4. Konec programu')
            user_choice = input('Vyberte možnost (1 - 4): ')

            if user_choice == "1":
                pridat_ukol(tasks)
            elif user_choice == "2":
                zobrazit_ukoly(tasks)
            elif user_choice == "3":
                smazat_ukol(tasks)
            elif user_choice == "4":
                print('Konec programu.')
                break
            else:
                print('Zadejte číslo 1 - 4.')

# 1. přidat úkol
def pridat_ukol(tasks):
    while True:
        task_name = input('Přidat úkol: ').strip()

        if task_name == "":
            print('Úkol musí mít název. Zadejte název úkolu.')
            continue
        if len(task_name) > 100:
            print("Název úkolu je příliš dlouhý (max. 100 znaků). Zadej kratší název.")
            continue
        if ukol_existuje(task_name, tasks):
            print('Úkol již existuje!')
            continue
        else:
            break

# přidání popisu
    description = input('Přidejte popis k úkolu (nepovinné): ').strip()
    if description == "":
        description = 'Úkol nemá popis.'
    elif len(description) > 100:
        print("Popis je příliš dlouhý (max 100 znaků). Bude zkrácen.")
        description = description[:100]

# přidání do tasks
    tasks.append({"task_name": task_name, "description": description})
    print('Úkol byl přidán.\n')
    zobrazit_ukoly(tasks)

# 2. zobrazit úkoly
def zobrazit_ukoly(tasks):
    print('\nTvoje úkoly: ')
    if not tasks:
        print('Žádné úkoly')
    else:
        for index, task in enumerate(tasks):
            print(f'{index + 1}: {task["task_name"]} - {task["description"]}')

# 3. odstranit úkol
def smazat_ukol(tasks):
    if not tasks:
        print("\nŽádné úkoly ke smazání.")
        return
    
    zobrazit_ukoly(tasks)
    task_number = valid_number(tasks)
    deleted_task = tasks.pop(task_number - 1)
    print(f'\nÚkol "{deleted_task["task_name"]}" byl smazán.')

# kontrola inputu 
def valid_number(tasks):
    while True:
        num_input = input('Zadejte číslo úkolu k odstranění: ')
        try:
            number = int(num_input)
            if 1 <= number <= len(tasks):
                return number
            else:
                print("Číslo úkolu není platné.")
        except ValueError:
            print("Zadejte platné číslo.")

# kontrola duplicity 
def ukol_existuje(task_name, tasks):
    for task in tasks:
        if task["task_name"].lower() == task_name.lower():
            return True
    return False

# spuštění programu
hlavni_menu()