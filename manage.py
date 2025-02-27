#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'page_permisos.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Inicializar Django antes de ejecutar cualquier consulta a la base de datos
    django.setup()

    # Crear superusuario si no existe
    from django.contrib.auth import get_user_model

    SUPERUSER_USERNAME = "fdiaz"
    SUPERUSER_EMAIL = "pepe@gmail.com"
    SUPERUSER_PASSWORD = "C1D1M3C.imt"

    User = get_user_model()
    
    if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
        User.objects.create_superuser(SUPERUSER_USERNAME, SUPERUSER_EMAIL, SUPERUSER_PASSWORD)
        print("✅ Superusuario creado correctamente.")
    else:
        print("⚠️ El superusuario ya existe.")

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
