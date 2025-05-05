#   Tereza Hanáková 
#   tereza_h. 

task = []
descriptions = {}
number = None

# fukce
# spuštění menu
def hlavni_menu():
    while True:
        print('\nSprávce úkolů - Hlavní menu\n 1. Přidat nový úkol\n 2. Zobrazit všechny úkoly\n 3. Odstranit úkol\n 4. Konec programu')
        user_choice = input('Vybete možnost (1 - 4): ')

        if user_choice == "1":
            pridat_ukol(task, descriptions)
        elif user_choice == "2":
            zobrazit_ukoly(task, descriptions)
        elif user_choice == "3":
            smazat_ukol(task, descriptions)
        elif user_choice == "4":
            print('Konec programu.')
            exit()
        else:
            print('Zadejte číslo 1 - 4.')
        

# 1. přidat úkol
def pridat_ukol(all_tasks, descriptions):
    while True:
        new_task = input('Přidat úkol: ').strip()

        if new_task == "":
            print('Úkol musí mít název. Zadejte název úkolu.')
            continue
        if len(new_task) > 100:
            print("Název úkolu je příliš dlouhý (max 100 znaků). Zadej kratší název.")
            continue
        if ukol_existuje(new_task, all_tasks):
            print('Úkol už existuje!')
            continue
        else:
            break

    all_tasks.append(new_task)
    new_descriptions = pridat_popis(new_task, descriptions) 
    print('Úkol byl přidán.\n')
    zobrazit_ukoly(all_tasks, descriptions)


# 2. zobrazit úkoly
def zobrazit_ukoly(all_tasks, descriptions):
    print('\nTvoje úkoly: ')

    if len(all_tasks) <= 0:
        print('Žádné úkoly')
    else:
        for index, task in enumerate(all_tasks):
            print(f'{index + 1}: {task} - {descriptions[task]}')

# 3. odstranit úkol
def smazat_ukol(all_tasks, descriptions):
    print('\nTvoje úkoly: ')
    for index, task in enumerate(all_tasks):
        print(f'{index + 1}: {task}')
    
    task_number = valid_number(task)
    del descriptions[all_tasks[task_number-1]]
    all_tasks.remove(all_tasks[task_number-1])
    
    print(f'\nÚkol číslo {task_number} smazán.')

# přidání popisu
def pridat_popis(task, descriptions):
    description = input('Přidejte popis k úkolu (nepovinné): ')

    if description == '':
        description = 'Úkol nemá popis.'

    descriptions[task] = description
    return descriptions

# kontrola inputu 
def valid_number(all_tasks):
    task_number = input('Zadejte číslo úkolu k odstranění: ')
    valid = False
    while not valid:
        try:
            number = int(task_number)
            valid = True
        except:
            task_number = input('Zadejte číslo úkolu k odstranění:  ')

    if not (0 < number <= len(all_tasks)):
        print('Úkol nenalezen!')
        return valid_number(all_tasks)
    else:
        return number

# kontrola duplicity 
def ukol_existuje(new_task, all_tasks):
    for task in all_tasks:
        if task == new_task:
            return True
    return False

# spuštění programu
hlavni_menu()