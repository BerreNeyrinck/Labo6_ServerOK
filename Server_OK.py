import platform #used for ping
import subprocess #used for ping
import json #used to r/w JSON file
import singlePing
import sys

print("----------------------------")
print("Welkom bij de Py-Server Manager")
print("1. Server toevoegen.")
print("2. Server Verwijderen.")
print("3. Servers Weergeven in lijst.")
print("4. CHECK MODUS. \n")

servers = []
jsonServers = []
jsonLog = []
count = 0

with open('data.json') as j:
    jsonServers = json.load(j) 

def server_Toevoegen():
    global count
    with open('data.json') as j:
        jsonServers = json.load(j) 

    invoer = input("Geef de naam/adres in van de server die u wilt toevoegen!: ")
    count += 1  # Increment global count
    jsonServers.append({"Server" + str(count): invoer})
    print(jsonServers)

    with open('data.json', 'w') as f:
        json.dump(jsonServers, f)



def server_Verwijderen():
    global jsonServers
    invoer = input("Geef de naam/adres in van de server die u wilt verwijderen!: ")

    with open('data.json') as j:
        data = json.load(j) 
        data = [item for item in data if invoer not in item.values()] #filer: keeps each element != to invoer.
        print(data)
    
    with open('data.json', 'w') as j:
        json.dump(data, j)



def server_Tonen():
    # Opening JSON file 
    with open('data.json',) as j:
        # returns JSON object as  
        # a dictionary 
        data = json.load(j) 
        # Iterating through the json 
        # list 
        for i in data: 
            print(list(i.values()))


def ping_Servers():
    # for val in jsonServers.values():
    with open('data.json') as j:
        data = json.load(j) 
        for item in data:
            for url in item.values(): #this is hell
                outcome = singlePing.myping(url)  # Pass URL directly to myping
                jsonLog.append({url: outcome})
    with open('logs.json', 'w') as f:   
        json.dump(jsonLog, f)





while True:

    if(len(sys.argv) == 1):
        userInput = input("Keuze(kies tussen: 1, 2, 3 of 4): ")
    else:
        userInput = sys.argv[1]
    match userInput:
        case "1": 
            print("\n u koos voor \"Server toevoegen\".")
            server_Toevoegen()
        case "2": 
            print("\n u koos voor \"Server Verwijderen\".")
            server_Verwijderen()
        case "3": 
            print("\n u koos voor \"Servers Weergeven in lijst\".")
            server_Tonen()
        case "4": 
            print("\n u koos voor \"CHECK MODE\".")
            ping_Servers()
        case _  : 
            print("U koos geen juist antwoord.")
            break

