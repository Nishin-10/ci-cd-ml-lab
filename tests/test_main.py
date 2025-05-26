# tests/test_main.py
import os
import sys

import pandas as pd
import pytest

# ensure src/ is on the import path
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)

from main import load_data


def test_load_data_not_empty():
    df = load_data()
    assert not df.empty, "load_data() returned an empty DataFrame"


def test_load_data_shape_and_columns():
    df = load_data()
    # we know the example data is 3 rows × 2 cols: A & B
    assert df.shape == (3, 2), f"Expected shape (3,2), got {df.shape}"
    assert list(df.columns) == ["A", "B"], f"Expected columns ['A', 'B'], got {list(df.columns)}"


def test_load_data_dtypes():
    df = load_data()
    # both columns should be integer dtype
    assert pd.api.types.is_integer_dtype(df["A"]), "Column A must be integer"
    assert pd.api.types.is_integer_dtype(df["B"]), "Column B must be integer"

