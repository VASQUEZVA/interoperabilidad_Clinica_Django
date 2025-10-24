"""
Este módulo define la configuración principal de la aplicación 'pacientes' dentro del proyecto Salud y Vida.
Contiene la clase de configuración que permite registrar la aplicación y definir su comportamiento base.
"""
from django.apps import AppConfig


class PacientesConfig(AppConfig):
    """
    Clase de configuración para la aplicación 'pacientes'.

    Define el campo automático por defecto para los modelos y el nombre
    interno de la aplicación que Django utiliza para su registro.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pacientes'
