while True:
    login1 = input("qual o seu login? ")
    senha1 = input("qual a sua senha? ")

    if login1 != senha1:
        login2 = input("qual o login da pessoa 2? ")
        senha2 = input("qual a senha da pessoa 2? ")

        while True:
            
            if login2 != login1 and login2 != senha2:        
                break 

            else:
                print("login e sennha iguais ou o login é o mesmo dda 1º pessoa")

        break
    else:
        print("login e senha iguais\n")