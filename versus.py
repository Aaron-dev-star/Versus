#ce programme a pour objectif de créer des duels sur base des éléments qui lui seront transmis

from random import randint

#gestion du nombre de joueur dans chaque liste et nombre de groupes


def nb_big_groups():
    groups_info=[]
    validate = True
    while validate:
        nb_groups = int(input("Entrer le nombre de groupes:"))
        nb_players = int(input("Entrer le nombre de joueurs par groupes:"))
        nb_big = int((nb_players * nb_groups) / 2)
        mod = nb_big % 2
      
        if  mod  == 0:
            validate = True
            groups_info.append(nb_groups)
            groups_info.append(nb_players)
            groups_info.append(nb_big)
            break
                
        else: 
            print("Entrez des valeurs correctes svp!")
    return groups_info

        
def add_players(groups_info):
    a=[]
    b=[]
    nb_big = groups_info[2]

    groups = []
    for i in range(nb_big):
        player_a = str(input("Entrer le nom du joueur:"))
        a.append(player_a)

    for i in range(nb_big):
        player_b = str(input("Entrer le nom du joueur:"))
        b.append(player_b)

    groups.append(a)
    groups.append(b)
    return groups



def generate_pool():
    groups_info = nb_big_groups()
    nb_pool = groups_info[0]
    pools = []
    i=0
    while i < nb_pool:
        pool = list()
        pools.append(pool)
        i += 1
    return print(pools)

def create_pool(groups_info):
    big_pools = add_players(groups_info)
    a = big_pools[0]
    b = big_pools[1]
    
    nb_player = groups_info[1]
    #pools = generate_pool()
    first=[]
    second=[]
    third=[]
    
   
    groups = []

    for i in big_pools:
        while len(first) < nb_player:
            choice_a = a[randint(0, len(a)-1)]
            choice_b = b[randint(0, len(b)-1)]
            first.append(choice_a)
            first.append(choice_b)
            a.remove(choice_a)
            b.remove(choice_b)

        while len(second) < nb_player:
            choice_a = a[randint(0, len(a)-1)]
            choice_b = b[randint(0, len(b)-1)]
            second.append(choice_a)
            second.append(choice_b)
            a.remove(choice_a)
            b.remove(choice_b)
        
        while len(third) < nb_player:
            choice_a = a[randint(0, len(a)-1)]
            choice_b = b[randint(0, len(b)-1)]
            third.append(choice_a)
            third.append(choice_b)
            a.remove(choice_a)
            b.remove(choice_b)
    
    groups.append(first)
    groups.append(second)
    groups.append(third)
    groups.append(a+b)
        
    return groups
# def save(groups):

#     text =" ".join(list(groups))
#     with open('versus.txt', 'a') as file:
#         file.write(text)
#         file.close()

list_info = nb_big_groups()

tirage = create_pool(list_info)
print("Groupe A:", tirage[0],  "\n", "Groupe B:",tirage[1], "\n", "Groupe C", tirage[2], "\n", "Groupe D", tirage[3])

#save(tirage)