
employeers = [{'name': 'Oscar', 'role': 'Dev'},    
              {'name': 'Carlos', 'role': 'Dev'},] 

def add_employeer(name: str, role: str):    
    employeers.append({"name": name, "role": role}) 
    
def delete_employeers(name: str):    
    for employeer in employeers:        
        if(employeer["name"] == name):            
            employeers.remove(employeer) 
            
if __name__ == "__main__":    #con esto podemos buscar esos datos desde la terminal de vsc y ver lo que retorna el codigo
    print(employeers)    
    add_employeer("pedro", "admin")    
    print(employeers)    
    delete_employeers("Carlos")    
    print(employeers)