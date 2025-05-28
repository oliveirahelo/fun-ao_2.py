def reserva():
    numero_de_mesas = 20
    mesas_alugadas = 0
    while mesas_alugadas < numero_de_mesas :
        nome = input("Nome da reserva: ")
        mesas =  int(input("quantas mesas voce precisa? "))
        mesas_alugadas += mesas
        print(f"mesa reservada para o cliente: {nome}, restam:{numero_de_mesas-mesas_alugadas}")
    print("reservas recusadas! ")

reserva()