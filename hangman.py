from audioop import add
import random
import time
import pyodbc
import requests
from bs4 import BeautifulSoup

def api():
    api_key ="df103dedc52382f2b61d6845b7c4f120"                            
    form_id ="241565311751048"                               

    url = f"http://eu-api.jotform.com/form/{form_id}/submissions?apiKey={api_key}"

    api_words = []
    response = requests.get(url)
    data = response.json()
    submissions = data.get('content', [])

    for submission in submissions:
        answers = submission.get('answers', {})

    name_answer = answers.get('8',{}).get('answer', 'No name provided')   
    api_words.append(name_answer)
    words = api_words

    return words


def add_crud():
    global words
    words=[]
    
    userInput = input('Enter words seperated by a commma: ').replace(" ","")
    userList = userInput.split(",")
    file = open("words.csv", "w")
    for word in userList:                        
        file.write(word+'\n')  
    file.close()            
    
    file=open("words.csv","r")
    for word in file:
        words.append(word.strip("\n"))
    file.close()
    
    print("Words added to list and file: ",words)
    input("Press ENTER to continue...")


def update_crud():
    # Update with new word 
    userInput = input('Enter words seperated by a commma: ').replace(" ","")
    userList = userInput.split(",")
    file = open("words.csv", "r")
    words = []
    for word in file:
        words.append(word.strip("\n"))
    file.close()

    i = 0
    while i <= len(words) - 1:
        if words[i] == userList[0]:
            words[i] = userList[1]
        i += 1 
    
    # Write to file
    file = open("words.csv", "w")
    for word in words:
        file.write(word + '\n')
    file.close()
    print(words)

def delete_crud():
    file = open("words.csv", "w")
    userInput = input("Enter word to Delete: ").replace(" ","")  
    
    file = open("words.csv","r")     
    words = []
    
    for word in file:
        words.append(word.strip("\n"))
    file.close()    

 


def file_github():
    wordList = []

    url = "https://raw.githubusercontent.com/Zymiva/hangman_file/main/Github_hangman.html"
    response = requests.get(url)
    response = response.content 
    soup = BeautifulSoup(response, "html.parser")

    ol = soup.find('ol')
    if ol:
        words = ol.find_all('li')
        for tag in words:
            word = tag.text.strip()
            wordList.append(word)

    if not wordList:
        print("No 'ol' found")
        
    return wordList
        
  

 
def splash():
    # Introduction to game 
    delay = 3 
    while delay:
        print("  ==================")
        print(" LET'S PLAY HANGMAN")
        print("  ", delay, "secs to start")
        print("  ==================\n\n")
        print('''
        _________
        |/      |      
        |       O
        |     \_|_/
        |       |
        |      / \\
        |     /   \\
    ____|_____
    ''')
        print("  ==================")
        time.sleep(1)
        delay = delay - 1 


def game():
    #Randomly choose a word from the list 
    global secret 
    secret = random.choice(words)
    secret = secret.upper()
    guessed = ''
    turns = 7
    placed = '_' * len(secret)
    l = list(placed)
    done = 0

    while turns:
        while True:

            hang(turns)
            print("\n\nSecret Word....:", ' '.join(l))
            print("\n\nLetters Used....:",guessed)
            print("\n\nTries to go.....:",turns)
            typed = input("\n\nGuess a Letter......: ")
            if typed not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or len(typed) >1:
                input ("Single Upper Case Letter ONLY! Press ENTER to continue......")
            else:
                break
        turns = 7
        
        if typed not in guessed:
            guessed = guessed + typed 
        g = list(guessed)
        s = list(secret)

        for k in range(len(g)):
            kstr = guessed[k]
            if kstr in s:
                for i in range(len(s)):
                    if kstr == s[i]:
                        l[i] = kstr
            else:
                turns = turns - 1 

        if l == s:

            hang(turns)
            print("=============================================")
            print("CONGRATULATIONS! YOU GUESSED: ", ''.join(secret))
            print("=============================================")
            input("Press ENTER to continue...")
            break 

        if turns == 0:

            hang(turns)
            print("=============================================")
            print("GAME OVER! SECRET WORD: ", ''.join(secret))
            print("=============================================")
            input("Press ENTER to continue...")
            break

def main():

    print("==================")
    print("WELCOME TO HANGMAN")
    print("==================\n\n")
    print("    Main Menu \n\n")
    print(" 1) Play Game")
    print(" 2) Add New Word")
    print(" 3) Use Other Lists\n\n")
    print(" 9) EXIT\n\n")
    
    print("==================\n\n")
    Choice = input("Input An Option: ")
    if Choice == "1":
        splash()
        game()
    elif Choice == "2":
        add_word()
    elif Choice == "3":
        other_options()
    elif Choice == "9":
        exit(0)
    else:
        input("Please Input Valid Option")
    main()

# List of words
words = ["variable", "string", "integer", "selection"]


def other_options():

   print("==================")
   print(" Pick Your List! ")
   print("==================\n\n")
   print(" 1) SQL List")
   print(" 2) GitHub List")
   print(" 3) API List")
   print(" 4) CRUD List\n\n")
   print(" 9) EXIT\n\n")


   choice= input("Input An Option: ")
   if choice == "1":
        global words
        words = sql_list()
        game()    
   elif choice == "2":
        words = file_github()
        game()
   elif choice == "3":
        words = api()
        game()     
   elif choice == "4":
        words = crud_options()   
   elif choice == "9":
       exit(0)
   else:
       input("Please Input Valid Option...")
        
def crud_options():
    print("==================")
    print(" CRUD List: ")
    print("==================\n\n")
    print(" 1) Add Your Own Words")
    print(" 2) Update Word In List")
    print(" 3) Delete List\n\n")
    print(" 9) EXIT\n\n")


    choice= input("Input An Option: ")
    if choice == "1":
        add_crud()
        game()    
    elif choice == "2":
        update_crud()
    elif choice == "3":
        words = delete_crud()
    elif choice == "9":
       exit(0)
    else:
       input("Please Input Valid Option...")
    
def sql_list():
    SERVER = "DESKTOP-AGPK6AM"
    DATABASE = "hangman"
    connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Integrated Security=True;'
    conn = pyodbc.connect(connectionString)
    cursor= conn.cursor()
    cursor.execute("SELECT Word FROM tWords")
    records = cursor.fetchall()
    
    words_from_sql = []
    for r in records:
        word = r[0]  
        words_from_sql.append(word)

    return words_from_sql

#def cursor.execute("INSERT INTO tWords (Word) VALUES (?)", (New_word,))

def add_word():

    print("Old word list:", ", ".join(words))
    new_word = input("Input New Word: ")
    if len(new_word) > 0:
        words.append(new_word)

    print("New word list", ", ".join(words))
    input("Press ENTER to continue...")

def hang(turn):
    
    if turn < 7:
        print(" _________")
        print(" |/      |")
    else:
        print(" _________")
        print(" |/       ")
        
    if turn < 6:
         print(" |       O")
    else:
        print(" |         ")

    if turn < 5:
         print(" |     \_|_/")
    else: 
        print(" |          ")

    if turn < 4:
         print(" |       |")
    else:
        print(" |          ")

    if turn < 3:
         print(" |      / \\")
    else:
        print(" |          ")

    if turn < 2:
         print("|     /   \\")
    else:
        print(" |          ")
    if turn < 1:
         print("|           ")
    else:    
        print(" |_______")

if __name__ == "__main__":
    main()

