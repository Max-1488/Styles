import os
from pyfiglet import Figlet


def print_cool(text):
    #Instancia de figlet con ajuste de fuente inclinado

   
    
    """Styles text disponibles 
    bubble
    circle, digital, embos, block
    emboss2, future, ivrit, lean
    letter, mini, mnemonic, pagga
    script, shadow, slant, small
    smblock, smbraille, smscript, smshadow
    smslant
    standard
    term
    wideterm"""
    cool_text = Figlet(font="future")
    #limpia la ventana de la terminal
    # Establecer ventana de terminal a un tamaño fijo
    
    return str(cool_text.renderText(text))    

if __name__ == "__main__":

    
    print("\033[1;33m"  +   "╺┳╸┏━╸╻ ╻╺┳╸   ┏┓ ┏━┓┏┓╻┏┓╻┏━╸┏━┓"+'\033[0;m')
    print("\033[1;33m"  +   " ┃ ┣╸ ┏╋┛ ┃ ╺━╸┣┻┓┣━┫┃┗┫┃┗┫┣╸ ┣┳┛"+'\033[0;m')
    print("\033[1;33m"  +   " ╹ ┗━╸╹ ╹ ╹    ┗━┛╹ ╹╹ ╹╹ ╹┗━╸╹┗╸"+'\033[0;m')
    
    print ("\n>>> Code Text Terminal")
    print (">>> Coded By MaxWice ")
    print (">>> www.instagram/marcoshtb_\n\n")

    print("\033[4;35m"+"Enter Text username"+'\033[0;m')
    text = input(" >> " )
    print(print_cool(text))
    print()
    print()
    print("--------------------------------------------------\n\n")
    os.system("python3 Styles.py")
    os.system("clear")
    
    
    
    
    
    
    
