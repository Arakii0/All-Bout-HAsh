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



def crack_hash(hash, dictionary=None):
    
    hashes = sorted(list(hashlib.algorithms_guaranteed))
    count = 1
    for i in hashes:
        print(f"{count}: {i}")
        count += 1
    hash_selection = int(input("Select the hash type: "))

    print("Cracking hash...")

    cracked = False

    

    if dictionary:
        with open(dictionary, "r") as f:
            for password in f:
                password = password.strip()
                encoded = password.encode()

                h = hashlib.new(hashes[hash_selection - 1])
                h.update(encoded)
                
                if hash == h.hexdigest():
                    cracked = True
                    print(f"Hash cracked: {password}")
                    break


    else:
        dictionary = ['123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', '111111', '1234567', 'dragon', '123123', 'baseball', 'abc123', 'football', 'monkey', 'letmein', '696969', 'shadow', 'master', '666666', 'qwertyuiop', '123321', 'mustang', '1234567890', 'michael', '654321', 'pussy', 'superman', '1qaz2wsx', '7777777', 'fuckyou', '121212', '000000', 'qazwsx', '123qwe', 'killer', 'trustno1', 'jordan', 'jennifer', 'zxcvbnm', 'asdfgh', 'hunter', 'buster', 'soccer', 'harley', 'batman', 'andrew', 'tigger', 'sunshine', 'iloveyou', 'fuckme', '2000', 'charlie', 'robert', 'thomas', 'hockey', 'ranger', 'daniel', 'starwars', 'klaster', '112233', 'george', 'asshole', 'computer', 'michelle', 'jessica', 'pepper', '1111', 'zxcvbn', '555555', '11111111', '131313', 'freedom', '777777', 'pass', 'fuck', 'maggie', '159753', 'aaaaaa', 'ginger', 'princess', 'joshua', 'cheese', 'amanda', 'summer', 'love', 'ashley', '6969', 'nicole', 'chelsea', 'biteme', 'matthew', 'access', 'yankees', '987654321', 'dallas', 'austin', 'thunder', 'taylor', 'matrix', 'minecraft']
        for password in dictionary:
            encoded = password.encode()

            h = hashlib.new(hashes[hash_selection - 1])
            h.update(encoded)

            if hash == h.hexdigest():
                cracked = True
                print(f"Hash cracked: {password}")
                break
    
    if not cracked:
        print("Exhausted wordlist")

                



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
        hash_string(input("Please enter a string to be hashed: "))
    case 3:
        crack_hash(input("Enter the hash: "))
    case _:
        print("Choose an option above!")

