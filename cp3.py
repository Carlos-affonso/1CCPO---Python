from streamlit.web.cli import main_run

temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

valores = []
contador = 0
maior_ocorrencias = 0

for sala in temperaturas:
    contador += 1
    soma = 0
    media = 0
    maior_33 = 0
    for temperatura in sala:
        soma += temperatura
        if temperatura > 33:
            maior_33 += 1
    media = soma / len(sala)
    valores.append([contador, media, maior_33])

for sala in valores:
    numero_sala = sala[0]
    media = sala[1]
    maior_33 = sala[2]
    if maior_33 > maior_ocorrencias:
       maior_ocorrencias = numero_sala

    print(f"Sala: {numero_sala}")
    print(f"Média: {media}")
    print(f"Registros Críticos: {maior_33}")
    print()

print(f"Sala com maior risco: Sala {maior_ocorrencias}")



