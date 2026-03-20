print("=== Sistema de Suporte Técnico ===")

problema = input("Descreva seu problema: ")

if "internet" in problema.lower():
    print("Solução: Reinicie o roteador e verifique os cabos.")
elif "lento" in problema.lower():
    print("Solução: Feche programas abertos e reinicie o computador.")
elif "erro" in problema.lower():
    print("Solução: Tente reinstalar o programa.")
else:
    print("Solução: Entre em contato com o suporte técnico.")

print("Chamado registrado com sucesso!")
