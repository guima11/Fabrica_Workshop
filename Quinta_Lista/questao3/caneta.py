def caneta(Azul, Preto, PriceAz, PricePre):
    if Azul > 0 and Preto > 0:
        Valor = Azul * PriceAz + Preto * PricePre
    elif Azul > 0 and Preto <= 0:
        Valor = Azul * PriceAz
    elif Azul <= 0 and Preto >= 0:
        Valor = Preto * PricePre
    else:
        Valor = 0
    return Valor
