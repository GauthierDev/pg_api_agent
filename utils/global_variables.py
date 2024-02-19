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
            os_value = os.environ.get(variable)
            if os_value is not None and os_value != '':
                setattr(self, "_" + variable.lower(), os_value)
            else:
                setattr(self, "_" + variable.lower(), default_value)

    def reset_global_variables(self):
        # Mettre à jour les variables globales avec les nouvelles valeurs des variables d'environnement
        self._initialize_global_variables()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
