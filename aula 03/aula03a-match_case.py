# 0 --> sair do programa
# 1 --> entrar no programa
#   --> ERRO!


escolha_usuario = 0

match escolha_usuario:
    case 0:
        print("Sair do Programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("ERRO!!!")