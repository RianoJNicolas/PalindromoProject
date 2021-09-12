def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_inver = palabra[::-1]

    if palabra == palabra_inver:
        return True
    else:
        return False

def run():
    palabra = input('Ingresa una palabra: ')
    es_palindromo = palindromo(palabra)
    
    if es_palindromo == True:
        print(palabra + ', es palindroma')
    else:
        print(palabra + ', NO es palindroma')


if __name__ == '__main__':
    run()