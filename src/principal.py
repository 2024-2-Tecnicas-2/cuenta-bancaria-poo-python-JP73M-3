from src.cuenta_bancaria import CuentaBancaria


if __name__ == '__main__':
    # TODO: Adiciona aquí el código que deseas para la Cuenta Bancaria.

    cuenta = CuentaBancaria("Juan Melo", "506222062", 150000)

    assert cuenta.get_titular() == "Juan Melo"

    cuenta.set_titular("Carmen Pulido")
    assert cuenta.get_titular() == " Carmen Pulido"

    assert cuenta.get_numero_cuenta() == "506222062"

    assert cuenta.get_saldo() == 150000

    cuenta.ingresar(50000)
    assert cuenta.get_saldo == 200000

    cuenta.ingresar(-20000)
    assert cuenta.get_saldo == 200000

    cuenta.retirar(80000)
    assert cuenta.get_saldo() == 120000

    cuenta.retirar(150000)
    assert cuenta.get_saldo == 120000

    assert cuenta.calcular_interes() == 121800

    cuenta.set_tipo_interes(5,0)
    assert cuenta.calcular_interes() == 126000

    cuenta.set_tipo_interes(-2.0)
    assert cuenta.calcular_interes() == 126000

    cuenta.set_tipo_interes(12.0)
    assert cuenta.calcular_interes() == 126000

    print("Todas las pruebas fueron correctas")




