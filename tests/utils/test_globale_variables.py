import os
import pytest

from utils.global_variables import GlobalVariables


@pytest.fixture
def clean_environment():
    original_environ = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(original_environ)


def test_initialization(clean_environment):
    os.environ["VARIABLE1"] = "Custom Value"
    os.environ["VARIABLE2"] = "456"  # Convertit l'entier en chaîne de caractères
    os.environ["POSTGRESQL_URL"] = "New Variable"

    global_vars = GlobalVariables()

    assert global_vars._variable1 == "Custom Value"
    assert global_vars._variable2 == "456"  # Utilise la valeur par défaut car "VARIABLE2" n'est pas défini dans os.environ
    assert global_vars._postgresql_url == "New Variable"  # Nouvelle variable définie dans os.environ


def test_reset(clean_environment):
    os.environ["VARIABLE1"] = "Custom Value"
    os.environ["VARIABLE2"] = "456"  # Convertit l'entier en chaîne de caractères
    os.environ["POSTGRESQL_URL"] = "New Variable"

    global_vars = GlobalVariables()

    os.environ["VARIABLE1"] = "Reset value"
    os.environ["VARIABLE2"] = "1212"   # Convertit l'entier en chaîne de caractères
    os.environ["POSTGRESQL_URL"] = "PG est fantastique"


    assert global_vars._variable1 == "Custom Value"
    assert global_vars._variable2 == "456"
    assert global_vars._postgresql_url == "New Variable"  # La variable a été réinitialisée car reset_global_variables() est appelée

    global_vars.reset_global_variables()

    assert global_vars._variable1 == "Reset value"
    assert global_vars._variable2 == "1212"
    assert global_vars._postgresql_url == "PG est fantastique"
