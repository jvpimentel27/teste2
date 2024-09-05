texto = input("Digite uma string: ")
quant_min = texto.count('a')
quant_mai = texto.count('A')
total = quant_min + quant_mai


print(f"A letra 'A' aparece {quant_mai} vezes em maiúsculo, {quant_min} vezes em minúsculo, totalizando {total} ")
