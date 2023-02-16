# -*- coding: utf-8 -*-
"""
Script para hacer testing sobre una función

"""

from src import carga_datos
import pandas as pd
from pandas.testing import assert_frame_equal

datos = pd.read_csv("data/test.csv")



def test_carga_datos():
    assert_frame_equal(carga_datos.obtener_datos('test'), datos)
    
