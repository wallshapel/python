users = [['Ruby', 41], ['María', 20], ['Paola', 15], ['Camila', 31], ['Catalina', 100], ['Nathalia', 0], ['Yesli', 52], ['Stephanie', 22], ['Alexandra', 34], ['Andrea', 10], ['Yeimi', 40], ['Karoll', 32], ['Grace', 11], ['Geraldine', 3], ['Tania', 43], ['Thalía', 33]]

names = list(map(lambda user : user[0], users)) # Devuelve los usuarios sin los índices

print(names)


fewer_users = list(filter(lambda user : user[1] > 10, users)) # Devuelve una lista donde los índeces sean mayores que 10. Si ninguno es mayor, no devuelve la lista
print(fewer_users)
