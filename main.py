from nameProcessing import numeScurte

nume=input("Scrie numele (separate prin ;): ")

lista=nume.split(";")

print(";".join(numeScurte(lista)))
