# Python Django
## Proyecto Clínica Salud Vida — Sistema de Gestión Clínica
Este proyecto desarrolla un Sistema de Información para la IPS “Salud y Vida”, implementado en Django, orientado a la gestión interoperable de la historia clínica electrónica de los pacientes, conforme a la Resolución 866 de 2021 del Ministerio de Salud de Colombia.
Su propósito es garantizar la interoperabilidad, integridad y trazabilidad de los datos clínicos, siguiendo buenas prácticas de desarrollo de software y principios de Programación Orientada a Objetos (POO).

## Configuración:
### Clonar el repositorio
    git clone https://github.com/VASQUEZVA/interoperabilidad_Clinica_Django.git

### Para instalar las dependencias del proyecto, ejecute el siguiente comando:
    pip install -r requirements.txt

### Configuración de la base de datos
1. Asegúrese de tener MySQL instalado y en funcionamiento en su máquina local.
2. Cree una base de datos llamada `InteroperbilidadClinica` en su servidor MySQL.
3. Cree un archivo `.env` en el directorio raíz del proyecto y agregue las variables de entorno con la configuración de su base de datos:



###  Formato para archivo variables de entorno .env
    DB_NAME= InteroperbilidadClinica
    DB_USER=root
    DB_PASSWORD= Tu contraseña
    DB_HOST=localhost
    DB_PORT=3306
### Aplicar migraciones de la base de datos:

    python manage.py makemigrations
    python manage.py migrat


### Para crear un superusuario para acceder al panel de administración, utilice el siguiente comando:
    python manage.py createsuperuser

### Para ejecutar el servidor de desarrollo, utilice el siguiente comando:
    python manage.py runserver




