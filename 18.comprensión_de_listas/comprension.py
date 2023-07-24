animals = [['pig', 20], ['giraffe', 5], ['seal', 22], ['delfin', 1], ['bear', 2]]

# Queremos que la lista solo contenga los animales. No nos interesan los campos numéricos

kind = [animal[0] for animal in animals]
print(kind)