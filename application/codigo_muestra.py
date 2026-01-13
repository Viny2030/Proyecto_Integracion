def calcular_score_riesgo(monto: float, frecuencia: int) -> float:
    """
    Calcula un score de riesgo simple.
    """
    if monto < 0 or frecuencia < 0:
        raise ValueError("Los valores no pueden ser negativos")

    score = monto * 0.6 + frecuencia * 0.4
    return round(score, 2)


def clasificar_riesgo(score: float) -> str:
    if score < 100:
        return "BAJO"
    elif score < 300:
        return "MEDIO"
    return "ALTO"
