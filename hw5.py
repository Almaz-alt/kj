GEEKS = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del GEEKS['bag']

GEEKS['address'] = 'Ибраимова 103, БЦ Victory!'

GEEKS['Адрес'] = GEEKS.pop('address')

GEEKS['Телефон'] = '+996 507 052 018'

GEEKS['Instagram'] = '@geeks_edu'

GEEKS['Курсы'] = GEEKS.pop('courses')

GEEKS['Дата основание'] = '2018-08-06'

num_courses = len(GEEKS['Курсы'])
print(f"Количество курсов: {num_courses}!")

print("Вот наш словарь GEEKS: ")
for key, value in GEEKS.items():
    print(f"{key}: {value}")