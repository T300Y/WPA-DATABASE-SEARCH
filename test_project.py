import pytest
from project import database, comparision, table
def test_data():
    assert database(["Men's 100m","T35","M"], 11) is None
    assert database(["Women's 100m","T35","W"], 11) is None
def test_comparision():
    assert comparision('0:11.4', 14.4) == '79.17%'

def test_table():
    assert table([{'first':'test1', 'second':'test2'}]) == '+---------+----------+\n| first   | second   |\n+=========+==========+\n| test1   | test2    |\n+---------+----------+'