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
    python manage.py migrate


### Para crear un superusuario para acceder al panel de administración, utilice el siguiente comando:
    python manage.py createsuperuser

# Cargar Datos de Maestros a la Base de Datos
### Para cargar datos iniciales en la base de datos, utilice el siguiente comando:
    # moverse a la carpeta del proyecto (app)

    cd .\ips_salud_vida\
    
    python manage.py loaddata data_inicial.json

Este comando cargará los datos desde el archivo `data_inicial.json` ubicado en el directorio raíz del proyecto a la base de datos configurada.

El archivo `data_inicial.json` contiene datos maestros para las siguientes tablas:

1. Pais
2. Municipio_Residencia_Habitual
3. Ocupacion
4. Etnia
5. Comunidad
6. Causa_Motivo_Atencion
7. Categoria_Discapacidad
8. Tipo_Documento
9. Via_ingreso_Usuario
10. Modalidad_Servicio
11. Clasificacion_CIE-10
12. Entidad_Salud

### Para ejecutar el servidor de desarrollo, utilice el siguiente comando:
    python manage.py runserver




