

# test_app.py
from app import add
def test_add():        # NB : 1 seule ligne vide avant -> flake8 va râler !
    assert add(2, 3) == 5
