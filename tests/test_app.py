import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))
from app import *

def test_add():
    assert add(5,6) == 11

def test_add2():
    assert add(5,6) != 10

def test_mul():
    assert multiply(6,10) == 60

def test_mul2():
    assert multiply(3,4) != 10

def test_sub():
    assert subtract(5,4) == 1

def test_div():
    assert divide(10,2) == 5

def test_sq():
    assert square(4) == 16

def test_log():
    assert log(1) == 0

def test_sin():
    assert sin(0) == 0

def test_cos():
    assert cos(0) == 1

def test_sqrt():
    assert square_root(25) == 5

def test_percentage():
    assert percentage(10,4) == 40
