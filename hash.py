import hashlib

def get_hash(input_string, algorithm):
    # Create a hash object using specified algorithm 
    hash_object = hashlib.new(algorithm)
    # Encode the input string to bytes and update the hash object
    hash_object.update(input_string.encode('utf-8'))
    # Get the hexadecimal representation of the hash 
    hash_hex = hash_object.hexdigest()
    return hash_hex

# Common algorithms include 'md5','sha1','sha224','sha256','sha384','sha512'
algoList = ('md5','sha1','sha224','sha256','sha384','sha512')

input_string="Hello, world!"
for algo in algoList:
    hash_value = get_hash(input_string,algo)
#    print(f"The '{algo:<10}' hash of '{input_string}' is : {hash_value}")
    
getString = lambda inputString: "Hello, World!" if inputString == "" else inputString
stringToHash = getString(str(input("Enter text: "))) 

hashDict={}
choose_algo = input("Choose a hash algorithm (md5, sha1, sha224, sha256, sha384, sha512): ")

for letter in stringToHash:
    if letter not in hashDict:
        hashDict[letter] = True
        letter_hash = get_hash(letter,choose_algo)
        print(f"Letter: '{letter}' Hash: '{letter_hash}")


    # print_hash = lambda letter: print(f"{letter}: {get_hash(letter, chosen_algo)}")
    # [print_hash(letter) for letter in stringToHash if letter not in hashDict.setdefault(letter, True)]