def test_simple_check():
    assert 1 == 1

def test_pandas_import():
    import pandas as pd
    assert pd.__version__ is not None
