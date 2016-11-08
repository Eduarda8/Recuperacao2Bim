def ValorPagamento(ValorPrestacao, DiasAtraso):
    PercentualMulta = 3
    ValorMulta = (ValorPrestacao * PercentualMulta)/100
    PercentualJurosDias = 0.1
    ValorJurosDia = (ValorPrestacao * PercentualJurosDias)/ 100
    ValorTotalJurosDia = ValorJurosDia * DiasAtraso
    ValorTotal = ValorPrestacao + ValorMulta + ValorTotalJurosDia
    return ValorTotal
ValorTotalPagamento = ValorPagamento(29963,35)
print("O valor total do pagamento é :",ValorTotalPagamento)
