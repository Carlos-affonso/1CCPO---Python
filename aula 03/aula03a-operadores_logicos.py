# Lógica E (and)

verifica_senha = True
verifica_email = True

login = verifica_email and verifica_senha
print(login)

if not login:
    print("Loga certo ai mn...")