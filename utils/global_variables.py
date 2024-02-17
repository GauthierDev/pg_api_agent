import os

class GlobalVariables:
    _instance = None
    _initialized = False
    _variable_defaults = {
        "VARIABLE1": "Valeur par défaut",
        "VARIABLE2": 123,
        "POSTGRESQL_URL": "postgres://user:password@localhost:5432/database"
    }

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            if not cls._initialized:
                cls._instance._initialize_global_variables()
                cls._initialized = True
        return cls._instance

    def _initialize_global_variables(self):
        # Initialisation des variables globales à partir de l'OS ou autre source
        for variable, default_value in self._variable_defaults.items():
            setattr(self, "_" + variable.lower(), os.environ.get(variable, default_value))

    def reset_global_variables(self):
        # Réinitialisation des variables globales avec les nouvelles valeurs des variables d'environnement
        self._initialize_global_variables()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
