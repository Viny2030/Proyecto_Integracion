import pytest
from application.codigo_muestra import (
    calcular_score_riesgo,
    clasificar_riesgo,
)


def test_calcular_score_riesgo_ok():
    score = calcular_score_riesgo(100, 10)
    assert score == 64.0


def test_calcular_score_riesgo_negativo():
    with pytest.raises(ValueError):
        calcular_score_riesgo(-1, 5)


def test_clasificar_riesgo_bajo():
    assert clasificar_riesgo(50) == "BAJO"


def test_clasificar_riesgo_medio():
    assert clasificar_riesgo(150) == "MEDIO"


def test_clasificar_riesgo_alto():
    assert clasificar_riesgo(500) == "ALTO"
