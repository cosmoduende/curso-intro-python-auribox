
# Generador de ataques elegantes

import random

eres = ["Horrendo", "Fastidioso", "Odioso", "Apestoso", "Detestable", "Fuchi"]
partesDelCuerpo = ["Cabeza", "Pie", "Boca", "Mano", "Oreja", "Ojo"]
adjetivos = ["Grande", "Feo", "Rápido", "Lento", "Desabrido", "Bobo"]
animales = ["Vaca", "Gaviota", "Delfín", "Tortuga", "Liebre", "Jirafa"]
    
randomEres = random.choice(eres)
randomParteCuerpo = random.choice(partesDelCuerpo)
randomAdjetivo = random.choice(adjetivos)
randomAnimal = random.choice(animales)
    
print(f"Eres {randomEres}, tu {randomParteCuerpo} es {randomAdjetivo} como de {randomAnimal}")