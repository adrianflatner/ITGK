
my_family = {}

def add_family_member(role,name):
    #my_family[role] = name
    my_family.setdefault(role, []).append(name)

#def lister(key,dic):

    #liste.append(dic[key])
    #if key in dic:
    #return dic[key]
       #bror.append(dic[key])

def main():
    add_family_member('bror','Arne')
    add_family_member('bror','Geir')
    add_family_member('mor','Anne')

    print(my_family)

main()
