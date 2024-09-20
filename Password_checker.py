import os, re, time, math, random
os.system("CLS")

#Password Generetor
nummer = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&?"
längd = 20
aba =  "".join(random.sample(nummer,längd)) #Genererar ett random lörsenord 


from colorama import Fore, Back, Style, init #Från Colorama importar följande. 

print("Lörsenords krav: 15 bokstäver är minimun för ett säkert lörsenord, stora och små bokstäver, siffror från 0-9 och täcken som [$#@]")
time.sleep(2)
print("Här är ett exempel på hur ett starkt lörsenord ska se ut, om du vill så kan du använda detta som ditt egna lörsenord istället för att komma på egna.")
time.sleep(1)
print("Genererar...")
time.sleep(3)
os.system("CLS")
print(Fore.GREEN + aba)
time.sleep(2)
print(Fore.RESET + "Om du fortfarande vill använda ditt lörsenord så kan du kolla säkerheten nu") 
time.sleep(2)

x = True 

while x: #Loopen
    password = input("Vad är ditt lörsenord: ")
    if (len(password)<15 or len(password)>float("inf")): #om längden av lörsenordet är kortare än 15 skriv då ut error texten eller om lörsenordet är över 15 fortsätt. len = returnar (lenght) i en variabel.
        print(Fore.RED + "Lörsenordet måsta ha mer än 15 tecken.") #Fore.RED = Texten kommer vara färgen röd. 
        time.sleep(2)
    

    if not re.search("[a-z]",password): #Kollar om lörsenordet innehåller små tecken från a-z. Annars skriv ut error texten. 
        print(Fore.RED +"Lörsenordet måste innehålla små bokstäver.")
        time.sleep(2)
        

    if not re.search("[A-Z]",password): #Kollar om lörsenordet har stora bokstäver A-Z. Annars skriv ut error texten. 
        print(Fore.RED +"Lörsenordet måste innehålla stora bokstäver.")
        time.sleep(2)
        

    if not re.search("[0-9]",password): #Om lörsenordet inte innehåller siffror skriv då ut error texten nedan. 
        print(Fore.RED + "Lörsenordet måste innehålla nummer från 0-9.")
        time.sleep(2)
        

    if not re.search("[$#@%&]",password): #Om lörsenordet inte innehåller speciella karaktärer 
        print(Fore.RED + "Lörsenordet måste innehålla special karaktärer som $#@%&")
        time.sleep(2)

    elif re.search("\s", password): #Kollar efter om lörsenordet innehåller mellanrum. 
        print(Fore + "Lörsenordet får inte innehålla mellanrum")
        time.sleep(2)
        


    else:
        print(Fore.GREEN +"Ditt lörsenord är stark")
        
    x = input(Fore.RESET + "Vill du fortsätta y/n?: ")

    password == None #Password variabeln återställs

    if x == "y": #Om sant fortsätt.
        x=True

    elif x == "n": #Om falskt avsluta programmet. 
        x=False 

    else:
        print("Svara bara y/n, Ja eller Nej. Avslutar...")
        time.sleep(2)
        x=False

        
        

