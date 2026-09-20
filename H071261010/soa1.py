level_pedas = int(input("Masukkan level pedas: "))
if level_pedas < 0 or level_pedas > 100:
    print("Input tidak valid")
elif level_pedas <= 10:
    print("Level Aman")
elif level_pedas <= 40:
    print("Level Sedang")
elif level_pedas <= 70:
    print("Level Pedas")
else:
    print("Level Ekstrim") 