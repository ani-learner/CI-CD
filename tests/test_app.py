from app import index
from app import about

def test_index():
    assert index() == "Hello Folks!"

def test_about():
    assert about() == "Hi my name is Aniruddh Singh"


