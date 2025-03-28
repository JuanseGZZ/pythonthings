
def calcular(mensual,tasa, años):
    meses = años * 12
    total = 0
    for i in range(meses):
        #print("mes: ", i+1)
        if i == 0:
            total = mensual * (1 + tasa)
        else:
            total = (total * (1 + tasa)) + mensual
        #print("total: ", total)

    totalTasa = 1
    for i in range(meses):
        #porsentaje total ganado anualmente
        totalTasa *= (tasa + 1)
    print("total tasa: ", "{:.2f}".format((totalTasa - 1)*100), "%")    
    print("total: ", "{:.2f}".format(total))
    return total


calcular(100, 0.00375, 35)