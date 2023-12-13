import random

# vytvoření seznamu českých předpon

predpony = ["do", "na", "nad", "o", "ob", "od", "po", "pod", "pro", "pře", "před", "při", "roz", "s", "u", "v", "vy", "vz", "z", "za"]

# vytvoření seznamu českých přípon

pripony = ["ák", "al", "an", "ař", "ář", "as", "át", "ava", "č", "čka", "čtina", "ctví", "ctvo", "cký", "dlo", "ec", "ečný", "ičelý", "ičitý", "ička", "ický", "ičný", "ina", "istý", "itý", "ium", "jedy", "ka", "ová", "krát", "na", "natý", "né", "ní", "ník", "ný", "o", "ol", "ost", "oun", "ova", "ovi", "oví", "ovec", "ovka", "ovné", "ovo", "ovský", "ovy", "ový", "plný", "s", "sko", "ský", "ština", "ství", "stvo", "tel", "telný", "tva", "utý", "ův", "ýr", "ýř"]

# vytvoření seznamu českých koncovek

koncovky = ["a", "e", "ě", "i", "o", "u", "y", "ou", "é", "í", "ů", "ech", "ách", "ích", "em", "ám", "ím", "ům", "mi", "ami", "emi", "ími", "ovi", "ové"]

# vytvoření seznamu, který nám do textu promítne tzv. slovní vatu - slovní vycpávky, zbytečné pro význam věty, text bude zajímavější

slovni_vata = ["jakoby", "vlastně", "čili", "prostě", "jako", "takové to", "jaksi", "de facto", "nějakým způsobem", "právě"]

# vytvoříme si také seznamy samohlásek a souhlásek, které nám budou tvořit slabiky, se kterými budeme dále pracovat

samohlasky = ["i", "í", "e", "a", "á", "o", "u"]

souhlasky = ["b", "c", "č", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "ř", "s", "š", "t", "v", "z", "ž"]

# vytvoříme si ještě seznam, ve kterém budeme mít popletené spojky, před kterými bude čárka

rozdeleni_vety = [",", ", abyby", ", ča", ", koliač", ", ťa", ", ža", ", ťyb", ", kožjeli", ", jestželi", ", koja", ", bykdy", ", kdyžkdy", ", čel", ", kupdo", ", něvadžpo", ", tožepro", ", tožepro", ", tvaso", ", batřeže", ", zdalizda"]

# pro zajímavost si ještě do textu zakomponujeme pár českých citoslovců

citoslovce = ["abrakadabra", "ách", "aj", "auvajs", "amen", "bác", "baf", "blé", "brnk", "brum", "bů", "buch", "bzum", "chramst", "crnk", "cvrnk", "drnc", "ejhle", "fuj", "hačí", "hop", "hudry", "hyjé", "jáj", "jauvajs", "juchú", "jupí", "kiš", "klep", "kristepane"]

# uživatel zadá, kolik vět chce naším generátorem vytvořit

pocet_vet = int(input("Kolik vět chcete vygenerovat? (Zadejte číslem)\n"))

pocet_vet_vystup = pocet_vet # proměnná pro uložení počtu vět zadaných uživatelem - použití ve výstupním souboru .txt

# vytvoříme si také seznamy pro slovesa (příčestí minulé)

slovesa_koncovky = ["l", "la", "lo", "li", "ly"]

# tvorba samotného generátoru

kompletni_text = "" # proměnná, do které budeme ukládat jednotlivé věty

pripona = "" # proměnná na uložení přidávané přípony

while pocet_vet != 0:
    
    # vytvoříme si do našeho programu podstatná jména

    podstatna_jmena = []

    # počet vygenerovaných podstatných jmen určíme náhodou, řekněme od 2 do 7 (upravitelná hodnota)

    pocet_podstatnych_jmen = 0

    podstatne_jmeno = ""

    while pocet_podstatnych_jmen < random.randint(2, 7):

        # výskyt předpony v podstatném jménu bude určen náhodně

        predpona_ano_ne = random.choice([True, False])

        if predpona_ano_ne == True:
           
            podstatne_jmeno += random.choice(predpony)

        # vygenerování kořene podstatnému jménu - vždy bude nějaký

        pocet_slabik = 0

        # počet slabik bude náhodně - řekněme od 2 po 4 (upravitelná hodnota)

        koren = ""

        while pocet_slabik < random.randint(2, 4):

            koren += (random.choice(souhlasky) + random.choice(samohlasky))

            pocet_slabik += 1

        podstatne_jmeno += koren

        # náhodně můžeme přidat příponu, řekněme šance 1 : 3 (upravitelná hodnota)

        pripona_ano_ne = random.randint(1, 3)

        if pripona_ano_ne == 1:

            pripona = random.choice(pripony)

            podstatne_jmeno += pripona

        # náhodně přidáme koncovku

        koncovka_ano_ne = random.choice([True, False])

        # nebudeme přidávat koncovku ke konkrétnějším (zavedenějším) příponám

        if pripona == "čtina" or pripona == "ctví" or pripona == "ctvo" or pripona == "cký" or pripona == "ečný" or pripona == "ičelý" or pripona == "ičitý" or pripona == "ický" or pripona == "ičný" or pripona == "istý" or pripona == "itý" or pripona == "ium" or pripona == "ová" or pripona == "krát" or pripona == "plný" or pripona == "ství" or pripona == "stvo" or pripona == "telný":

            koncovka_ano_ne = False

        if koncovka_ano_ne == True:

            podstatne_jmeno += random.choice(souhlasky) # z kořene podstatné jméno končí samohláskou, přidejme ještě souhlásku před přidáním samohláskové koncovky, dvě samohlásky vedle sebe nejsou pro češtinu příliš typické

            podstatne_jmeno += random.choice(koncovky)

        podstatna_jmena.append(podstatne_jmeno)

        podstatne_jmeno = ""

        pocet_podstatnych_jmen += 1

    # vygenerujeme si také nějaká slovesa

    slovesa = []

    # náhodně určíme jejich počet

    pocet_sloves = 0

    sloveso = ""

    while pocet_sloves < random.randint(1, 3): # (upravitelná hodnota)

        # náhodně určíme výskyt předpony slovesa

        predpona_ano_ne = random.randint(1, 3) # (upravitelná hodnota)

        if predpona_ano_ne == 1:

            sloveso += random.choice(predpony)

        # náhodně určíme kořen slovesa

        pocet_slabik = 0

        koren = ""

        while pocet_slabik < random.randint(2, 4):
    
            koren += (random.choice(souhlasky) + random.choice(samohlasky))

            pocet_slabik += 1

        sloveso += koren

        # určíme koncovku slovesa - buď příčestí minulé, samohláska nebo nic
    
        koncovka_slovesa = random.choice(["příčestí minulé", "samohláska", "nic"])
    
        if koncovka_slovesa == "příčestí minulé":

            sloveso += random.choice(slovesa_koncovky)
    
        elif koncovka_slovesa == "samohláska":

            sloveso += random.choice(souhlasky) # opět přidáním souhlásky zabráníme výskytu dvou samohlásek vedle sebe (pro češtinu méně přirozené)

            sloveso += random.choice(samohlasky)

        slovesa.append(sloveso)
    
        sloveso = ""

        pocet_sloves += 1

    # Teď už budeme kompletovat celé věty

    # V naší věte budeme chtít využít všechny podstatná jména a slovesa, mezi ně budeme náhodně vkládat ostatní slova

    veta = ""

    while True:

        if bool(podstatna_jmena) == False and bool(slovesa) == False:
            
            break

        volba_slova = random.choices(["podstatné jméno", "sloveso", "slovní vata", "rozdělení věty", "citoslovce", "nic"], weights=(10, 7, 4, 5, 3, 1)) # weights - (upravitelná hodnota)

        volba_slova = "".join(volba_slova) # převod na string, random choices vrací list

        if volba_slova == "podstatné jméno" and bool(podstatna_jmena) == True:

            volba_podstatneho_jmena = random.choice(podstatna_jmena)

            veta += (volba_podstatneho_jmena + " ")

            podstatna_jmena.remove(volba_podstatneho_jmena)

        elif volba_slova == "sloveso" and bool(slovesa) == True:

            volba_slovesa = random.choice(slovesa)

            slovesa.remove(volba_slovesa)

            veta += (volba_slovesa + " ")

        elif volba_slova == "slovní vata":
            
            veta += (random.choice(slovni_vata) + " ")

        elif volba_slova == "rozdělení věty" and bool(veta) == True:

            veta = veta[:-1] # vymaže mezeru (poslední prvek stringu), bude vkládat čárku

            veta += (random.choice(rozdeleni_vety) + " ")

        elif volba_slova == "citoslovce":

            veta += (random.choice(citoslovce) + " ")

    volba_poslední_interpunkce = random.choices([".", "!", "?"], weights=(13, 3, 5))
    
    volba_poslední_interpunkce = "".join(volba_poslední_interpunkce) # převod na string jako předtím

    veta = veta[:-1] # vymazání mezery před připojením poslední interpunkce

    veta += volba_poslední_interpunkce

    veta = veta.capitalize() # zvětšíme první písmeno věty tak, jak je v jazyce zvykem

    kompletni_text += (veta + " ") # před další větou potřebujeme mezeru

    pocet_vet -= 1

# finální zkompletování celého textu

kompletni_text = kompletni_text[:-1] # vymazání poslední mezery za interpunkcí

# mužete si příkaz pod tímto sdělením odkomentovat a vygenerovaný text zobrazit do konzole

# print(kompletni_text)

# vypsání vygenerovaného textu do textového dokumentu

with open('lorem_ipsum_generator.txt', 'w') as file:

    if pocet_vet_vystup == 1:

        print(f"Tady je vaše {pocet_vet_vystup} náhodně vygenerovaná věta:\n", file = file)

    elif pocet_vet_vystup > 1 and pocet_vet_vystup < 5:

        print(f"Tady jsou vaše {pocet_vet_vystup} náhodně vygenerované věty:\n", file = file)

    else:

        print(f"Tady je vašich {pocet_vet_vystup} náhodně vygenerovaných vět:\n", file = file)

    print(kompletni_text, file = file)