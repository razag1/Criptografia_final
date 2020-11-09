#Lista de caracteres a serem utilizados para a criptografia
ListaCaracteres = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
 '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', 
 '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95', '\x96', '\x97', '\x98', 
 '\x99', '\x9a', '\x9b', '\x9c', '\x9d', '\x9e', '\x9f', '\xa0', '¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '\xad', '®', '¯', 
 '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 
 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 
 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ']

#Opção para o usuário de o que fazer
print ('Para criptografar uma mensagem digite "1"')
print ('Para descriptografar uma mensagem digite "2"')
print ('Para sair digite "0"')
iniciar = input()

#Loop que limitara as opções do usuário para as
while iniciar != "0" and iniciar != "1" and iniciar != "2":
    print ('\nINVALIDO')
    print ('\nPara criptografar uma mensagem digite "1"')
    print ('Para descriptografar uma mensagem digite "2"')
    print ('Para sair digite "0"')
    iniciar = input()

iniciar = int(iniciar)
'''################################################################'''

#Loop para o código reiciar caso o usuário deseje
while iniciar >= 0 and iniciar <= 2:

    #condição para o usuário criptografar uma mensagem
    if iniciar == 1:
        n1 = int (input ("Digite um numero inteiro maior que 0 para a 1 chave: "))
        n2 = int (input ("Digite um numero inteiro maior que 0 para a 2 chave: "))
        n3 = n2
        print ('\nAs chaves devem ser compartilhadas apenas com as pessoas que irão receber as mensagens')

        #loop caso o usuario digite um numero invalido
        while n1 < 1 or n2 < 1:
            print ('\nNumero invalido')
            n1 = int (input ("Digite um numero inteiro diferente de 0 para a 1 chave: "))
            n2 = int (input ("Digite um numero inteiro diferente de 0 para a 2 chave: "))
            n3 = n2


        #condição para fazer n1 sempre ser maior que n2
        if n2 > n1:
            n3  = n1 
            n1  = n2 
            n2  = n3
        
        #Calculo para encontrar as condições para a criptografia
        while n1 % n3 != 0:
            n3 = n1 % n3

        mdc = n3
        mmc = (n1*n2)/mdc
        mdc = int(mdc)
        mmc =int(mmc)
        
        #Mensagem a ser criptografada
        mensagem = input ('\nDigite a mensagem a ser criptografada: ')

        #definir a quantidade de caracteres da tabela a ser utilizada
        n = 222

        #calculo para obter a mensagem criptografada
        cifrada = ""
        for caractere in mensagem:
            indice = ListaCaracteres.index(caractere)
            Novo_Caractere = ListaCaracteres[((indice + mmc)-mdc)%n]
            cifrada = cifrada + Novo_Caractere

        print ("\nA mensagem criptografada é: ")
        print (f"\n{cifrada}")
        print ("\n")

    '''################################################################'''

    #condição para o usuário descriptografar uma mensagem
    if iniciar == 2:
        print ("Para poder decifrar uma mensagem é necessario ter as chaves do usuário que a criptografou")
        n1 = int (input ("\nDigite a 1 chave: "))
        n2 = int (input ("Digite a 2 chave: "))
        n3 = n2

        #condição para fazer n1 sempre ser maior que n2
        if n2 > n1:
            n3  = n1 
            n1  = n2 
            n2  = n3
        
        #Calculo para encontrar os valores necessarios para a decriptografar da mensagem
        while n1 % n3 != 0:
            n3 = n1 % n3

        mdc = n3
        mmc = (n1*n2)/mdc
        mdc = int(mdc)
        mmc =int(mmc)
        
        #Mensagem a ser decriptografada
        mensagem = input ('\nDigite a mensagem a ser decifrada: ')

        #definir a quantidade de caracteres da tabela a ser utilizada 
        n = 222

        #calculo para decifrar a mensagem criptografada
        decifrada = ""
        for caractere in mensagem:
            indice = ListaCaracteres.index(caractere)
            Novo_Caractere = ListaCaracteres[(((indice + mdc) - mmc)%n)]
            decifrada = decifrada + Novo_Caractere

        print ("A mensagem descriptografada é: ")
        print (f"\n{decifrada}")
        print ('\n')

    '''################################################################'''

    print ('Para criptografar uma mensagem digite "1"')
    print ('Para descriptografar uma mensagem digite "2"')
    print ('Para sair digite "0"')
    iniciar = input()
    
    #Loop que limitara as opções do usuário para as
    while iniciar != "0" and iniciar != "1" and iniciar != "2":
        print ('\nINVALIDO')
        print ('\nPara criptografar uma mensagem digite "1"')
        print ('Para descriptografar uma mensagem digite "2"')
        print ('Para sair digite "0"')
        iniciar = input()
    iniciar = int(iniciar)
    
    #opção caso o usuário deseje sair termina o programa
    if iniciar == 0:
        break