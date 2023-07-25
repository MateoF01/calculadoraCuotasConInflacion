#Calculadora de precio real en cuotas

def calcula_valor_real(precio, cant_cuotas, inflacion_mensual):

    una_cuota = round(precio / cant_cuotas)
    precio_real = 0

    for i in range(cant_cuotas):
        valor_cuota_mensual = (una_cuota - (una_cuota * (inflacion_mensual/100) * i))
        precio_real += valor_cuota_mensual
        print(f"Cuota {i + 1} - Valor de la cuota pagado: {valor_cuota_mensual}")
        valor_cuota_mensual = 0

    return precio_real

print("Valor total pagado en pesos: " , calcula_valor_real(407699, 18, 3))