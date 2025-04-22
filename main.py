import tkinter as tk
import pyperclip

class CipherCraftApp:
    def __init__(self, root): # Program starting Landing screen
        self.root = root
        self.root.title("CipherCraft")
        self.root.geometry("800x500")#box size 
        self.root.config(bg="black")  # Set background color
        self.root.resizable(False, False)  # Disable window resizing
        
        # Logo and slogan
        self.logo_label = tk.Label(root, text="CipherCraft", font=("Times New Roman", 36), fg="white", bg="black")
        self.logo_label.place(relx=0.5, rely=0.1, anchor="center")
        self.slogan_label = tk.Label(root, text="Fun with Ciphers", font=("Times New Roman", 18), fg="white", bg="black")
        self.slogan_label.place(relx=0.5, rely=0.2, anchor="center")
        # Encrypt button
        self.encrypt_button = tk.Button(root, text="Start", command=self.start, width=20, height=3, font=("Times New Roman", 18), bg="gray", fg="white")
        self.encrypt_button.place(relx=0.5, rely=0.5, anchor="center")
                     
    def start(self):    #Main program starting button
        # Clear the root window
        self.clear_screen()   
           
        # Logo and slogan
        self.logo_label = tk.Label(root, text="CipherCraft", font=("Times New Roman", 36), fg="white", bg="black")
        self.logo_label.place(relx=0.5, rely=0.1, anchor="center")
        self.slogan_label = tk.Label(root, text="Fun with Ciphers", font=("Times New Roman", 18), fg="white", bg="black")
        self.slogan_label.place(relx=0.5, rely=0.2, anchor="center")
            
        # Encrypt button
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.cipher_types_encrypt, width=20, height=3, font=("Times New Roman", 20), bg="gray", fg="white")
        self.encrypt_button.place(relx=0.30, rely=0.5, anchor="center")
        
        # Decrypt button
        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.cipher_types_decrypt, width=20, height=3, font=("Times New Roman", 20), bg="gray", fg="white")
        self.decrypt_button.place(relx=0.70, rely=0.5, anchor="center")
            
       
    def cipher_types_encrypt(self): #Encrypt It screen
        # Clear the root window
        self.clear_screen()
        
        # New screen for encryption
        encrypt_label = tk.Label(self.root, text="Encrypt It", font=("Times New Roman", 30), fg="white", bg="black")
        encrypt_label.place(relx=0.5, rely=0.2, anchor="center")
        
        # Caesar Cipher button
        caesar_button = tk.Button(self.root, text="Caesar Cipher", command=self.caesar_cipher,width=15, height=3, font=("Times New Roman", 16), bg="gray", fg="white")
        caesar_button.place(relx=0.35, rely=0.4, anchor="center")

        # Atbash Cipher button
        atbash_button = tk.Button(self.root, text="Atbash Cipher", command=self.atbash_cipher,width=15, height=3, font=("Times New Roman", 16), bg="gray", fg="white")
        atbash_button.place(relx=0.65, rely=0.4, anchor="center")
        
        # Rail Fence Cipher button
        rail_fence_button = tk.Button(self.root, text="Rail Fence Cipher", command=self.rail_fence_cipher,width=15, height=3, font=("Times New Roman", 16), bg="gray", fg="white")
        rail_fence_button.place(relx=0.35, rely=0.7, anchor="center")
        
        # keyword Cipher button
        keyword_button = tk.Button(self.root, text="Keyword Cipher", command=self.keyword_cipher,width=15, height=3, font=("Times New Roman", 16), bg="gray", fg="white")
        keyword_button.place(relx=0.65, rely=0.7, anchor="center")
        
        # Previous button
        previous_button = tk.Button(self.root, text="Previous", command=self.start, font=("Times New Roman", 12), bg="gray", fg="white")
        previous_button.place(relx=0.1, rely=0.1, anchor="center")
       
    def caesar_cipher(self):    # caesar cipher encrypt screen
        # Clear the root window
        self.clear_screen()
        
        # New screen for Caesar Cipher
        caesar_label = tk.Label(self.root, text="Caesar Cipher", font=("Times New Roman", 28), fg="white", bg="black")
        caesar_label.place(relx=0.5, rely=0.2, anchor="center")
        
       # Input box label
        input_label = tk.Label(self.root, text="Input Text to be Encrypted:", font=("Times New Roman", 14), fg="white", bg="black")
        input_label.place(relx=0.3, rely=0.4, anchor="center")

        # Input text box
        self.input_entry = tk.Text(self.root, width=40, height=5)
        self.input_entry.place(relx=0.5, rely=0.5, anchor="center")
      
        # Encrypt button
        encrypt_button = tk.Button(self.root, text="Encrypt", command=self.caesar_encrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        encrypt_button.place(x=400,y=350, anchor="center")
        
        # Previous button
        previous_button = tk.Button(self.root, text="Previous", command=self.cipher_types_encrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        previous_button.place(relx=0.1, rely=0.1, anchor="center")      
    def caesar_encrypt(self):   #caesar cipher encryption button and funcitonality code
        # Get text from the input entry in the text box 
        caesar_text = self.input_entry.get("1.0", "end-1c")
        self.input_entry.delete("1.0", "end") 
        
        shift = 10  # fixing the shift value to 10
        encrypted_text = ""
        for char in caesar_text:
            if char.isalpha():  # Check if the character is a letter
                shifted_ascii = ord(char) + shift  # Shift the ASCII value
                if char.islower():
                    if shifted_ascii > ord('z'):
                        shifted_ascii -= 26  # Wrap around if needed
                    elif shifted_ascii < ord('a'):
                        shifted_ascii += 26  # Wrap around if needed
                elif char.isupper():
                    if shifted_ascii > ord('Z'):
                        shifted_ascii -= 26  # Wrap around if needed
                    elif shifted_ascii < ord('A'):
                        shifted_ascii += 26  # Wrap around if needed
                encrypted_text += chr(shifted_ascii)
            else:
                encrypted_text += char  # Keep non-alphabetic characters unchanged
        
        
        # Open a new window to display output
        output_window = tk.Toplevel(self.root)
        output_window.title("Encryption Output")
        output_window.geometry("400x200")
        output_window.config(bg="black")
        
        output_label = tk.Label(output_window, text="Encrypted Text", font=("Times New Roman", 20), fg="white", bg="black")
        output_label.place(relx=0.5, rely=0.3, anchor="center")
        
        output_text = tk.Label(output_window, text=encrypted_text, font=("Times New Roman", 14), fg="white", bg="black")
        output_text.place(relx=0.5, rely=0.5, anchor="center")
        
        copy_button = tk.Button(output_window, text="Copy", command=lambda: self.copy_to_clipboard(encrypted_text), font=("Times New Roman", 12), bg="gray", fg="white")
        copy_button.place(relx=0.5, rely=0.8, anchor="center")
        
    def atbash_cipher(self):    # atbash cipher encrypt screen
        # Clear the root window
        self.clear_screen()
        
        # New screen for Substitutional Cipher
        substitution_label = tk.Label(self.root, text="Atbash Cipher", font=("Times New Roman", 28), fg="white", bg="black")
        substitution_label.place(relx=0.5, rely=0.2, anchor="center")
        
        # Input box label
        input_label = tk.Label(self.root, text="Input Text to be Encrypted:", font=("Times New Roman", 14), fg="white", bg="black")
        input_label.place(relx=0.3, rely=0.4, anchor="center")

        # Input text box
        self.input_entry = tk.Text(self.root, width=40, height=5)
        self.input_entry.place(relx=0.5, rely=0.5, anchor="center")
      
        # Encrypt button
        encrypt_button = tk.Button(self.root, text="Encrypt", command=self.atbash_encrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        encrypt_button.place(x=400,y=350, anchor="center")
        
        # Previous button
        previous_button = tk.Button(self.root, text="Previous", command=self.cipher_types_encrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        previous_button.place(relx=0.1, rely=0.1, anchor="center")      
    def atbash_encrypt(self):   #atbash cipher encryption button and funcitonality code
        # Get text from the input entry in the text box 
        atbash_text = self.input_entry.get("1.0", "end-1c")
        self.input_entry.delete("1.0", "end") 
        
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        reversed_alphabet = alphabet[::-1]
        
        # Convert text to lowercase
        atbash_text = atbash_text.lower()
        
        # Initialize an empty string to store the encrypted text
        encrypted_text = ''
        
        # Encrypt each character in the text
        for char in atbash_text:
            if char.isalpha():
                # Find the index of the character in the alphabet
                index = alphabet.find(char)
                # Replace the character with its counterpart in the reversed alphabet
                encrypted_char = reversed_alphabet[index]
                encrypted_text += encrypted_char
            else:
                # Keep non-alphabetic characters unchanged
                encrypted_text += char
                
        # Open a new window to display output
        output_window = tk.Toplevel(self.root)
        output_window.title("Encryption Output")
        output_window.geometry("400x200")
        output_window.config(bg="black")
        
        output_label = tk.Label(output_window, text="Encrypted Text", font=("Times New Roman", 20), fg="white", bg="black")
        output_label.place(relx=0.5, rely=0.3, anchor="center")
        
        output_text = tk.Label(output_window, text=encrypted_text, font=("Times New Roman", 14), fg="white", bg="black")
        output_text.place(relx=0.5, rely=0.5, anchor="center")
        
        copy_button = tk.Button(output_window, text="Copy", command=lambda: self.copy_to_clipboard(encrypted_text), font=("Times New Roman", 12), bg="gray", fg="white")
        copy_button.place(relx=0.5, rely=0.8, anchor="center")
        
    def rail_fence_cipher(self):    # rail fence cipher encrypt screen
        # Clear the root window
        self.clear_screen()
        
        # New screen for Substitutional Cipher
        substitution_label = tk.Label(self.root, text="Rail Fence Cipher", font=("Times New Roman", 28), fg="white", bg="black")
        substitution_label.place(relx=0.5, rely=0.2, anchor="center")
        
        # Input box label
        input_label = tk.Label(self.root, text="Input Text to be Encrypted:", font=("Times New Roman", 14), fg="white", bg="black")
        input_label.place(relx=0.3, rely=0.4, anchor="center")

        # Input text box
        self.input_entry = tk.Text(self.root, width=40, height=5)
        self.input_entry.place(relx=0.5, rely=0.5, anchor="center")
      
        # Encrypt button
        encrypt_button = tk.Button(self.root, text="Decrypt", command=self.rail_fence_encrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        encrypt_button.place(x=400,y=350, anchor="center")
        
        # Previous button
        previous_button = tk.Button(self.root, text="Previous", command=self.cipher_types_encrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        previous_button.place(relx=0.1, rely=0.1, anchor="center")
    def rail_fence_encrypt(self):   #rail fence cipher encryption button and functionality code
        # Get text from the input entry in the text box 
        rail_fence_text = self.input_entry.get("1.0", "end-1c")
        self.input_entry.delete("1.0", "end") 
        
        key = 3  # Number of rails
        # Matrix to hold the rail fence cipher
        rail = [['\n' for i in range(len(rail_fence_text))] for j in range(key)]  
        
        # Direction flag
        down = False
        row, col = 0, 0
        
        # Fill the rail matrix
        for char in rail_fence_text:
            # Change direction if at the top or bottom rail
            if (row == 0) or (row == key - 1):
                down = not down
            
            # Fill the rail matrix
            rail[row][col] = char
            col += 1
            
            # Move to the next row
            if down:
                row += 1
            else:
                row -= 1
        
        # Construct the cipher text
        encrypted_text = ''
        for i in range(key):
            for j in range(len(rail_fence_text)):
                if rail[i][j] != '\n':
                    encrypted_text += rail[i][j]
            
        # Open a new window to display output
        output_window = tk.Toplevel(self.root)
        output_window.title("Encryption Output")
        output_window.geometry("400x200")
        output_window.config(bg="black")
        
        output_label = tk.Label(output_window, text="Encrypted Text", font=("Times New Roman", 20), fg="white", bg="black")
        output_label.place(relx=0.5, rely=0.3, anchor="center")
        
        output_text = tk.Label(output_window, text=encrypted_text, font=("Times New Roman", 14), fg="white", bg="black")
        output_text.place(relx=0.5, rely=0.5, anchor="center")
        
        copy_button = tk.Button(output_window, text="Copy", command=lambda: self.copy_to_clipboard(encrypted_text), font=("Times New Roman", 12), bg="gray", fg="white")
        copy_button.place(relx=0.5, rely=0.8, anchor="center")
          
    def keyword_cipher(self):   #keyword cipher encrypt screen
        # Clear the root window
        self.clear_screen()
        
        # New screen for Substitutional Cipher
        substitution_label = tk.Label(self.root, text="Keyword Cipher", font=("Times New Roman", 28), fg="white", bg="black")
        substitution_label.place(relx=0.5, rely=0.2, anchor="center")
        
        # Input box label
        input_label = tk.Label(self.root, text="Input Text to be Encrypted:", font=("Times New Roman", 14), fg="white", bg="black")
        input_label.place(relx=0.3, rely=0.4, anchor="center")

        # Input text box
        self.input_entry = tk.Text(self.root, width=40, height=5)
        self.input_entry.place(relx=0.5, rely=0.5, anchor="center")
      
        # Encrypt button
        encrypt_button = tk.Button(self.root, text="Encrypt", command=self.keyword_encrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        encrypt_button.place(x=400,y=350, anchor="center")
        
        # Previous button
        previous_button = tk.Button(self.root, text="Previous", command=self.cipher_types_encrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        previous_button.place(relx=0.1, rely=0.1, anchor="center")
    def keyword_encrypt(self):  #keyword cipher encryption button and functionality code
        def generate_keyword_alphabet(keyword):
            keyword_alphabet = ''
            for char in keyword:
                if char not in keyword_alphabet:
                    keyword_alphabet += char
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char not in keyword_alphabet:
                    keyword_alphabet += char
            return keyword_alphabet

        def keyword_cipher_encrypt(plaintext, keyword):
            # Generate the keyword alphabet
            keyword_alphabet = generate_keyword_alphabet(keyword.lower())
            # Create a dictionary to map each character to its corresponding character in the keyword alphabet
            mapping = {char: keyword_alphabet[i] for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
            # Encrypt the plaintext
            ciphertext = ''.join(mapping[char] if char.isalpha() else char for char in plaintext.lower())
            return ciphertext

        # Fixed Keyword
        keyword = "liveproject"   
        
        # Get text from the input entry in the text box 
        keyword_cipher_text = self.input_entry.get("1.0", "end-1c")
        self.input_entry.delete("1.0", "end") 

        # Encrypt text
        encrypted_text =keyword_cipher_encrypt(keyword_cipher_text, keyword)
            
        # Open a new window to display output
        output_window = tk.Toplevel(self.root)
        output_window.title("Encryption Output")
        output_window.geometry("400x200")
        output_window.config(bg="black")
        
        output_label = tk.Label(output_window, text="Encrypted Text", font=("Times New Roman", 20), fg="white", bg="black")
        output_label.place(relx=0.5, rely=0.3, anchor="center")
        
        output_text = tk.Label(output_window, text=encrypted_text, font=("Times New Roman", 14), fg="white", bg="black")
        output_text.place(relx=0.5, rely=0.5, anchor="center")
        
        copy_button = tk.Button(output_window, text="Copy", command=lambda: self.copy_to_clipboard(encrypted_text), font=("Times New Roman", 12), bg="gray", fg="white")
        copy_button.place(relx=0.5, rely=0.8, anchor="center")
        
        
    def cipher_types_decrypt(self): # Decrypt It screen
        # Clear the root window
        self.clear_screen()
        
        # New screen for encryption
        encrypt_label = tk.Label(self.root, text="Decrypt It", font=("Times New Roman", 30), fg="white", bg="black")
        encrypt_label.place(relx=0.5, rely=0.2, anchor="center")
        
        # Caesar Cipher button
        caesar_button = tk.Button(self.root, text="Caesar Cipher", command=self.caesar_cipher_2,width=15, height=3, font=("Times New Roman", 16), bg="gray", fg="white")
        caesar_button.place(relx=0.35, rely=0.4, anchor="center")

        # Atbash Cipher button
        atbash_button = tk.Button(self.root, text="Atbash Cipher", command=self.atbash_cipher_2,width=15, height=3, font=("Times New Roman", 16), bg="gray", fg="white")
        atbash_button.place(relx=0.65, rely=0.4, anchor="center")
        
        # Rail Fence Cipher button
        rail_fence_button = tk.Button(self.root, text="Rail Fence Cipher", command=self.rail_fence_cipher_2,width=15, height=3, font=("Times New Roman", 16), bg="gray", fg="white")
        rail_fence_button.place(relx=0.35, rely=0.7, anchor="center")
        
        # keyword Cipher button
        keyword_button = tk.Button(self.root, text="Keyword Cipher", command=self.keyword_cipher_2,width=15, height=3, font=("Times New Roman", 16), bg="gray", fg="white")
        keyword_button.place(relx=0.65, rely=0.7, anchor="center")
        
        # Previous button
        previous_button = tk.Button(self.root, text="Previous", command=self.start, font=("Times New Roman", 12), bg="gray", fg="white")
        previous_button.place(relx=0.1, rely=0.1, anchor="center")
        
    def caesar_cipher_2(self):  #caesar cipher decrypt screen
        # Clear the root window
        self.clear_screen()
        
        # New screen for Caesar Cipher
        caesar_label = tk.Label(self.root, text="Caesar Cipher", font=("Times New Roman", 28), fg="white", bg="black")
        caesar_label.place(relx=0.5, rely=0.2, anchor="center")
        
       # Input box label
        input_label = tk.Label(self.root, text="Input Text to be Decrypted:", font=("Times New Roman", 14), fg="white", bg="black")
        input_label.place(relx=0.3, rely=0.4, anchor="center")

        # Input text box
        self.input_entry = tk.Text(self.root, width=40, height=5)
        self.input_entry.place(relx=0.5, rely=0.5, anchor="center")
      
        # Decrypt button
        encrypt_button = tk.Button(self.root, text="Decrypt", command=self.caesar_decrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        encrypt_button.place(x=400,y=350, anchor="center")
        
        # Previous button
        previous_button = tk.Button(self.root, text="Previous", command=self.cipher_types_decrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        previous_button.place(relx=0.1, rely=0.1, anchor="center")                      
    def caesar_decrypt(self):   #caesar cipher decryption button and funcitonality code
        # Get text from the input entry in the text box 
        caesar_text = self.input_entry.get("1.0", "end-1c")
        self.input_entry.delete("1.0", "end") 
        
        shift = 10  # fixing the shift value to 10
        decrypted_text = ""
        for char in caesar_text:
            if char.isalpha():  # Check if the character is a letter
                shifted_ascii = ord(char) - shift  # Shift the ASCII value backward
                if char.islower():
                    if shifted_ascii < ord('a'):
                        shifted_ascii += 26  # Wrap around if needed
                elif char.isupper():
                    if shifted_ascii < ord('A'):
                        shifted_ascii += 26  # Wrap around if needed
                decrypted_text += chr(shifted_ascii)
            else:
                decrypted_text += char  # Keep non-alphabetic characters unchanged        
        
        # Open a new window to display output
        output_window = tk.Toplevel(self.root)
        output_window.title("Encryption Output")
        output_window.geometry("400x200")
        output_window.config(bg="black")
        
        output_label = tk.Label(output_window, text="Decrypted Text", font=("Times New Roman", 20), fg="white", bg="black")
        output_label.place(relx=0.5, rely=0.3, anchor="center")
        
        output_text = tk.Label(output_window, text=decrypted_text, font=("Times New Roman", 14), fg="white", bg="black")
        output_text.place(relx=0.5, rely=0.5, anchor="center")
        
        copy_button = tk.Button(output_window, text="Copy", command=lambda: self.copy_to_clipboard(decrypted_text), font=("Times New Roman", 12), bg="gray", fg="white")
        copy_button.place(relx=0.5, rely=0.8, anchor="center")  
          
    def atbash_cipher_2(self):  #atbash cipher decrypt screen-
        # Clear the root window
        self.clear_screen()
        
        # New screen for atbash Cipher
        atbash_label = tk.Label(self.root, text="atbash Cipher", font=("Times New Roman", 28), fg="white", bg="black")
        atbash_label.place(relx=0.5, rely=0.2, anchor="center")
        
       # Input box label
        input_label = tk.Label(self.root, text="Input Text to be Decrypted:", font=("Times New Roman", 14), fg="white", bg="black")
        input_label.place(relx=0.3, rely=0.4, anchor="center")

        # Input text box
        self.input_entry = tk.Text(self.root, width=40, height=5)
        self.input_entry.place(relx=0.5, rely=0.5, anchor="center")
      
        # Decrypt button
        encrypt_button = tk.Button(self.root, text="Decrypt", command=self.atbash_decrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        encrypt_button.place(x=400,y=350, anchor="center")
        
        # Previous button
        previous_button = tk.Button(self.root, text="Previous", command=self.cipher_types_decrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        previous_button.place(relx=0.1, rely=0.1, anchor="center")
    def atbash_decrypt(self):   #atbash cipher decryption button and funcitonality code
        # Get text from the input entry in the text box 
        atbash_text = self.input_entry.get("1.0", "end-1c")
        self.input_entry.delete("1.0", "end") 
        
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        reversed_alphabet = alphabet[::-1]
        
        # Convert text to lowercase
        atbash_text = atbash_text.lower()
        
        # Initialize an empty string to store the decrypted text
        decrypted_text = ''
        
        # Decrypt each character in the text
        for char in atbash_text:
            if char.isalpha():
                # Find the index of the character in the reversed alphabet
                index = reversed_alphabet.find(char)
                # Replace the character with its counterpart in the regular alphabet
                decrypted_char = alphabet[index]
                decrypted_text += decrypted_char
            else:
                # Keep non-alphabetic characters unchanged
                decrypted_text += char
                
        # Open a new window to display output
        output_window = tk.Toplevel(self.root)
        output_window.title("Encryption Output")
        output_window.geometry("400x200")
        output_window.config(bg="black")
        
        output_label = tk.Label(output_window, text="Decrypted Text", font=("Times New Roman", 20), fg="white", bg="black")
        output_label.place(relx=0.5, rely=0.3, anchor="center")
        
        output_text = tk.Label(output_window, text=decrypted_text, font=("Times New Roman", 14), fg="white", bg="black")
        output_text.place(relx=0.5, rely=0.5, anchor="center")
        
        copy_button = tk.Button(output_window, text="Copy", command=lambda: self.copy_to_clipboard(decrypted_text), font=("Times New Roman", 12), bg="gray", fg="white")
        copy_button.place(relx=0.5, rely=0.8, anchor="center")

    def rail_fence_cipher_2(self):  #rail_fence cipher decrypt screen
        # Clear the root window
        self.clear_screen()
        
        # New screen for rail_fence Cipher
        rail_fence_label = tk.Label(self.root, text="Rail Fence Cipher", font=("Times New Roman", 28), fg="white", bg="black")
        rail_fence_label.place(relx=0.5, rely=0.2, anchor="center")
        
       # Input box label
        input_label = tk.Label(self.root, text="Input Text to be Decrypted:", font=("Times New Roman", 14), fg="white", bg="black")
        input_label.place(relx=0.3, rely=0.4, anchor="center")

        # Input text box
        self.input_entry = tk.Text(self.root, width=40, height=5)
        self.input_entry.place(relx=0.5, rely=0.5, anchor="center")
      
        # Decrypt button
        encrypt_button = tk.Button(self.root, text="Decrypt", command=self.rail_fence_decrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        encrypt_button.place(x=400,y=350, anchor="center")
        
        # Previous button
        previous_button = tk.Button(self.root, text="Previous", command=self.cipher_types_decrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        previous_button.place(relx=0.1, rely=0.1, anchor="center")
    def rail_fence_decrypt(self):   #rail_fence cipher decryption button and funcitonality code
        # Get text from the input entry in the text box 
        rail_fence_text = self.input_entry.get("1.0", "end-1c")
        self.input_entry.delete("1.0", "end") 
        
        key=3
        # Create a matrix to store the rail fence cipher
        rail = [['\n' for i in range(len(rail_fence_text))] for j in range(key)]
        
        # Initialize variables for traversal
        dir_down = None
        row, col = 0, 0
        
        # Mark the places with '*'
        for i in range(len(rail_fence_text)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
            
            # Place the marker
            rail[row][col] = '*'
            col += 1
            
            # Move to the next row using the direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
                
        # Fill the rail matrix
        index = 0
        for i in range(key):
            for j in range(len(rail_fence_text)):
                if (rail[i][j] == '*') and (index < len(rail_fence_text)):
                    rail[i][j] = rail_fence_text[index]
                    index += 1
        
        # Construct the resultant text by reading the matrix in a zig-zag manner
        decrypted_text = []
        row, col = 0, 0
        for i in range(len(rail_fence_text)):
            # Check the direction of flow
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
            
            # Append the character if it's not a marker
            if rail[row][col] != '*':
                decrypted_text.append(rail[row][col])
                col += 1
                
            # Move to the next row using the direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
        
        decrypted_text= "".join(decrypted_text)
        
        # Open a new window to display output
        output_window = tk.Toplevel(self.root)
        output_window.title("Encryption Output")
        output_window.geometry("400x200")
        output_window.config(bg="black")
        
        output_label = tk.Label(output_window, text="Decrypted Text", font=("Times New Roman", 20), fg="white", bg="black")
        output_label.place(relx=0.5, rely=0.3, anchor="center")
        
        output_text = tk.Label(output_window, text=decrypted_text, font=("Times New Roman", 14), fg="white", bg="black")
        output_text.place(relx=0.5, rely=0.5, anchor="center")
        
        copy_button = tk.Button(output_window, text="Copy", command=lambda: self.copy_to_clipboard(decrypted_text), font=("Times New Roman", 12), bg="gray", fg="white")
        copy_button.place(relx=0.5, rely=0.8, anchor="center")

    def keyword_cipher_2(self):  #keyword cipher decrypt screen
        # Clear the root window
        self.clear_screen()
        
        # New screen for keyword Cipher
        keyword_label = tk.Label(self.root, text="Keyword Cipher", font=("Times New Roman", 28), fg="white", bg="black")
        keyword_label.place(relx=0.5, rely=0.2, anchor="center")
        
       # Input box label
        input_label = tk.Label(self.root, text="Input Text to be Decrypted:", font=("Times New Roman", 14), fg="white", bg="black")
        input_label.place(relx=0.3, rely=0.4, anchor="center")

        # Input text box
        self.input_entry = tk.Text(self.root, width=40, height=5)
        self.input_entry.place(relx=0.5, rely=0.5, anchor="center")
      
        # Decrypt button
        encrypt_button = tk.Button(self.root, text="Decrypt", command=self.keyword_decrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        encrypt_button.place(x=400,y=350, anchor="center")
        
        # Previous button
        previous_button = tk.Button(self.root, text="Previous", command=self.cipher_types_decrypt, font=("Times New Roman", 12), bg="gray", fg="white")
        previous_button.place(relx=0.1, rely=0.1, anchor="center")
    def keyword_decrypt(self):   #keyword cipher decryption button and funcitonality code
        def generate_keyword_alphabet(keyword):
            keyword_alphabet = ''
            for char in keyword:
                if char not in keyword_alphabet:
                    keyword_alphabet += char
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char not in keyword_alphabet:
                    keyword_alphabet += char
            return keyword_alphabet

        def keyword_cipher_decrypt(ciphertext, keyword):
            # Generate the keyword alphabet
            keyword_alphabet = generate_keyword_alphabet(keyword.lower())
            
            # Create a dictionary to map each character in the keyword alphabet to its corresponding 
            # character in the standard alphabet
            mapping = {keyword_alphabet[i]: char for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
            
            # Decrypt the ciphertext
            plaintext = ''.join(mapping[char] if char.isalpha() else char for char in ciphertext.lower())
            
            return plaintext 
        
        # Fixed Keyword
        keyword = "liveproject"        
               
        # Get text from the input entry in the text box 
        keyword_cipher_text = self.input_entry.get("1.0", "end-1c")
        self.input_entry.delete("1.0", "end") 

        # Encrypt text
        decrypted_text =keyword_cipher_decrypt(keyword_cipher_text, keyword)
            
        # Open a new window to display output
        output_window = tk.Toplevel(self.root)
        output_window.title("Encryption Output")
        output_window.geometry("400x200")
        output_window.config(bg="black")
        
        output_label = tk.Label(output_window, text="Encrypted Text", font=("Times New Roman", 20), fg="white", bg="black")
        output_label.place(relx=0.5, rely=0.3, anchor="center")
        
        output_text = tk.Label(output_window, text=decrypted_text, font=("Times New Roman", 14), fg="white", bg="black")
        output_text.place(relx=0.5, rely=0.5, anchor="center")
        
        copy_button = tk.Button(output_window, text="Copy", command=lambda: self.copy_to_clipboard(decrypted_text), font=("Times New Roman", 12), bg="gray", fg="white")
        copy_button.place(relx=0.5, rely=0.8, anchor="center")
                
                                   
    def copy_to_clipboard(self, text):  #function to copy resultant text 
        pyperclip.copy(text)
    
    def clear_screen(self): #function to clear the screen
        # Clear the root window
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
app = CipherCraftApp(root)
root.mainloop()