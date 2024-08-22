import hashlib

def identify(hash):
    pass

def hash_string(string):
    
    string_in_byte = string.encode()

    hashes = sorted(list(hashlib.algorithms_guaranteed))
    print("Please select a hash")
    
    count = 1
    for i in hashes:
        print(f"{count}: {i}")
        count += 1
    
    hash_selection = int(input("Enter option: "))
    
    h = hashlib.new(hashes[hash_selection - 1])
    h.update(string_in_byte)
    hashed = h.hexdigest()
    
    print(f"Original String is: {string}")
    print(f"{hashes[hash_selection - 1]} is {hashed}")



def crack_hash(hash):
    pass



print("""
 ___  ___  ________  ________  ___  ___  ________  ___       ___          
|\  \ \  \|\   __  \|\   ____\|\  \ \  \|\   __  \|\  \     /\  \         
\ \  \_\  \ \  \ \  \ \  \___|\ \  \_\  \ \  \ \  \ \  \    \ \  \        
 \ \   __  \ \   __  \ \_____  \ \   __  \ \   __  \ \  \    \ \  \       
  \ \  \ \  \ \  \ \  \|____|\  \ \  \ \  \ \  \ \  \ \  \____\ \  \____  
   \ \__\ \__\ \__\ \__\____\_\  \ \__\ \__\ \__\ \__\ \_______\ \_______\,
    \|__|\|__|\|__|\|__|\_________\|__|\|__|\|__|\|__|\|_______|\|_______|
                       \|_________|                                       """)

print("Please select an option:")
user_input = int(input("""1. Identify Hash
2. Hash     
3. Crack Hash
Select an option: """))

match user_input:
    case 1:
        pass
    case 2:
        user_input = input("Please enter a string to be hashed: ")
        hash_string(user_input)
    case 3:
        pass
    case _:
        print("Choose an option above!")

