# Rekent het verwachte percentage om naar een factor (bijv. 2% = 1.02).
def rendementOmrekenen(rendementPercentage):
    rendementFactor = 1 + (rendementPercentage / 100)
    return rendementFactor

# Berekent de verwachte waarde van een vast bedrag aan de hand van een looptijd in jaren en een percentage.
def vastBedrag(bedragVast, duurJaren, rendementFactor):
    bedragVastWaarde = bedragVast * (rendementFactor ** duurJaren)
    return bedragVastWaarde

# Berekent de verwachte waarde van een periodiek bedrag aan de hand van een looptijd in jaren en een percentage.
def periodeBedrag(duurJaren, bedragPeriode, rendementFactor, periodeJaren = False):
    bedragPeriodeTotaal_lijst = []
    bedragPeriodeWaarde_lijst = []
    if periodeJaren == True:
        while duurJaren >= 0:
            # Berekent de totale oorspronkelijke waarde van een periodiek bedrag.
            bedragPeriodeTotaal = bedragPeriodeTotaal + bedragPeriode
            # Berekent de totale verwachte waarde van een periodiek bedrag.
            bedragPeriodeWaarde = bedragPeriodeWaarde + bedragPeriode
            rendementPeriode = (bedragPeriodeWaarde * rendementFactor - bedragPeriodeWaarde) / 12
            bedragPeriodeWaarde = bedragPeriodeWaarde + rendementPeriode
            # Houdt lists bij van het totale bedrag en de totale waarde.
            bedragPeriodeTotaal_lijst.append(bedragPeriodeTotaal)
            bedragPeriodeWaarde_lijst.append(bedragPeriodeWaarde)
            # Telt af tot periode afgelopen is.
            duurJaren = duurJaren - 1

    else:
        duurMaanden = duurJaren * 12
        while duurMaanden >= 0:
            # Berekent de totale oorspronkelijke waarde van een periodiek bedrag.
            bedragPeriodeTotaal = bedragPeriodeTotaal + bedragPeriode
            # Berekent de totale verwachte waarde van een periodiek bedrag.
            bedragPeriodeWaarde = bedragPeriodeWaarde + bedragPeriode
            rendementPeriode = (bedragPeriodeWaarde * rendementFactor - bedragPeriodeWaarde) / 12
            bedragPeriodeWaarde = bedragPeriodeWaarde + rendementPeriode
            # Houdt lists bij van het totale bedrag en de totale waarde.
            bedragPeriodeTotaal_lijst.append(bedragPeriodeTotaal)
            bedragPeriodeWaarde_lijst.append(bedragPeriodeWaarde)
            # Telt af tot periode afgelopen is.
            duurMaanden = duurMaanden - 1
    return bedragPeriodeTotaal, bedragPeriodeWaarde, bedragPeriodeTotaal_lijst, bedragPeriodeWaarde_lijst

