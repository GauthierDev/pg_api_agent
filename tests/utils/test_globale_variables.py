# test_global_variables.py

import os
import pytest
from unittest.mock import patch
from utils.global_variables import GlobalVariables


# Fixture to reinit environment variables between tests
@pytest.fixture
def clean_environment():
    original_environ = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(original_environ)


def test_default_values(clean_environment):
    # Teste si les valeurs par défaut sont correctement initialisées
    global_vars = GlobalVariables()
    assert global_vars.variable1 == "Valeur par défaut"
    assert global_vars.variable2 == 123


def test_environment_variables(clean_environment):
    # Teste si les valeurs sont correctement récupérées à partir des variables d'environnement
    os.environ["VARIABLE1"] = "Custom value"
    os.environ["VARIABLE2"] = "456"
    global_vars = GlobalVariables()
    assert global_vars.variable1 == "Custom value"
    assert global_vars.variable2 == 456


def test_reset_global_variables(clean_environment):
    # Teste si les variables globales sont réinitialisées correctement
    os.environ["NEW_VARIABLE1"] = "New custom value"
    os.environ["NEW_VARIABLE2"] = "789"
    global_vars = GlobalVariables()
    global_vars.reset_global_variables()
    assert global_vars.variable1 == "New custom value"
    assert global_vars.variable2 == 789


@patch('os.environ', {})
def test_default_values_after_reset():
    # Teste si les valeurs par défaut sont réinitialisées après avoir vidé les variables d'environnement
    global_vars = GlobalVariables()
    assert global_vars.variable1 == "Valeur par défaut"
    assert global_vars.variable2 == 123
