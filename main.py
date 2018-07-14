from dog import Dog
from farm import Farm

while 1:
    menu = input('(v)iew farm, (t)eleport animal, (q)uit: ')
    if menu == 'q':
        break
    if menu == 'v':
        farms = Farm.find('farm.db')
        for f in farms:
            print(f)
        fid = int(input('choose a farm id: '))
        farm = list(filter(lambda f: f._id == fid, farms))[0]
        for a in farm.animals:
            print(a)
        print('-' * 50 + '\n')
    elif menu == 't':
        from_fid = int(input('choose a farm id to take animal: '))
        to_fid = int(input('choose a farm id to place animal: '))
        animal_id = int(input('choose a animal id you want to teleport: '))

        from_farm = list(filter(lambda f: f._id == from_fid, farms))[0]
        from_farm.teleport(to_fid, animal_id)
