from application.codigo_muestra import calcular_score_riesgo, clasificar_riesgo


def main():
    score = calcular_score_riesgo(120, 10)
    riesgo = clasificar_riesgo(score)
    print(f"Score: {score} | Riesgo: {riesgo}")


if __name__ == "__main__":
    main()
