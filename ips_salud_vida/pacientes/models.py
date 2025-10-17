import uuid
from django.db import models

# CAMPOS CON CHOICES

SEXO_CHOICES = [
    ("01", "Hombre"),
    ("02", "Mujer"),
    ("03", "Indeterminado / Intersexual"),
]

IDENTIDAD_GENERO_CHOICES = [
    ("01", "Masculino"),
    ("02", "Femenino"),
    ("03", "Transgénero"),
    ("04", "Neutro"),
    ("05", "No lo declara"),
]

ZONA_TERRITORIAL_CHOICES = [
    ("01", "Urbana"),
    ("02", "Rural"),
]


ENTORNO_ATENCION_CHOICES = [
    ("01", "Hogar"),
    ("02", "Comunitario"),
    ("03", "Escolar"),
    ("04", "Laboral"),
    ("05", "Institucional"),
]

GRUPO_SERVICIOS_CHOICES = [
    ("01", "Consulta externa"),
    ("02", "Apoyo diagnóstico y complementación"),
    ("03", "Internación"),
    ("04", "Quirúrgico"),
    ("05", "Atención inmediata"),
]

TRIAGE_CHOICES = [
    ("01", "Triage I"),
    ("02", "Triage II"),
    ("03", "Triage III"),
    ("04", "Triage IV"),
    ("05", "Triage V"),
]

TIPO_DIAGNOSTICO_CHOICES = [
    ("01", "Impresión diagnóstica"),
    ("02", "Confirmado nuevo"),
    ("03", "Confirmado repetido"),
]


# MODELOS ENTIDADES BÁSICAS

class Ocupacion(models.Model):
    codigo_ocupacion = models.CharField(max_length=4, primary_key=True, null=False)
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Ocupación"
        verbose_name_plural = "Ocupaciones"
        ordering = ["codigo_ocupacion"]
        db_table = "ocupacion"

    def __str__(self):
        return self.nombre


class Etnia(models.Model):
    id_etnia = models.CharField(max_length=2, primary_key=True, null=False)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Etnia"
        verbose_name_plural = "Etnias"
        ordering = ["id_etnia"]
        db_table = "etnia"

    def __str__(self):
        return self.descripcion


class Comunidad(models.Model):
    id_comunidad = models.CharField(max_length=3, primary_key=True, null=False)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Comunidad"
        verbose_name_plural = "Comunidades"
        ordering = ["id_comunidad"]
        db_table = "comunidad"

    def __str__(self):
        return self.descripcion

class MunicipioResidenciaHabitual(models.Model):
    codigo_municipio_RH = models.CharField(max_length=5, primary_key=True, null=False)
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Municipio de residencia habitual"
        verbose_name_plural = "Municipios de residencia habitual"
        ordering = ["codigo_municipio_RH"]
        db_table = "municipio_residencia_habitual"

    def __str__(self):
        return self.nombre

class EntidadSalud(models.Model):
    codigo_entidad_salud = models.CharField(max_length=12, primary_key=True, null=False)
    nombre = models.CharField(max_length=200)
    eps = models.BooleanField(default=False)
    ips = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Entidad de salud"
        verbose_name_plural = "Entidades de salud"
        ordering = ["codigo_entidad_salud"]
        db_table = "entidad_salud"

    def __str__(self):
        return self.nombre


class TipoDocumento(models.Model):
    tipo_documento = models.CharField(max_length=2, primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documento"
        ordering = ["tipo_documento"]
        db_table = "tipo_documento"

    def __str__(self):
        return self.descripcion


class Pais(models.Model):
    id_pais = models.CharField(max_length=3, primary_key=True, null=False)
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ["id_pais"]
        db_table = "pais"

    def __str__(self):
        return self.nombre


class CIE10(models.Model):
    codigo_CIE10 = models.CharField(max_length=4, primary_key=True, null=False)
    descripcion = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Clasificación CIE-10"
        verbose_name_plural = "Clasificaciones CIE-10"
        ordering = ["codigo_CIE10"]
        db_table = "clasificacion_cie10"

    def __str__(self):
        return f"{self.codigo_CIE10} - {self.descripcion}"


class EnfermedadHuerfana(models.Model):
    codigo_enfermedades_huerfanas = models.CharField(max_length=4, primary_key=True, null=False)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Enfermedad huérfana"
        verbose_name_plural = "Enfermedades huérfanas"
        ordering = ["codigo_enfermedades_huerfanas"]
        db_table = "enfermedad_huerfana"

    def __str__(self):
        return self.descripcion


class CausaMotivoAtencion(models.Model):
    codigo_causa_atencion = models.CharField(max_length=2, primary_key=True)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Causa / Motivo de atención"
        verbose_name_plural = "Causas / Motivos de atención"
        ordering = ["codigo_causa_atencion"]
        db_table = "causa_motivo_atencion"

    def __str__(self):
        return self.descripcion


class ModalidadServicio(models.Model):
    codigo_modalidad_servicio = models.CharField(max_length=4, primary_key=True)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Modalidad de servicio"
        verbose_name_plural = "Modalidades de servicio"
        ordering = ["codigo_modalidad_servicio"]
        db_table = "modalidad_servicio"

    def __str__(self):
        return self.descripcion


class ViaIngresoUsuario(models.Model):
    codigo_via_ingreso = models.CharField(max_length=4, primary_key=True, null=False)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Vía de ingreso"
        verbose_name_plural = "Vías de ingreso"
        ordering = ["descripcion"]
        db_table = "via_ingreso_usuario"

    def __str__(self):
        return self.descripcion


# ENTIDAD CENTRAL: PACIENTE


class Paciente(models.Model):
    paciente_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    documento = models.CharField(max_length=20, unique=True, null=False)
    primero_apellido = models.CharField(max_length=60, null=False)
    segundo_apellido = models.CharField(max_length=60, blank=True, null=True)
    primero_nombre = models.CharField(max_length=60, null=False)
    segundo_nombre = models.CharField(max_length=60, blank=True, null=True)
    fecha_nacimiento = models.DateTimeField(null=True)

    sexo_biologico = models.CharField(max_length=2, choices=SEXO_CHOICES, null=False)
    identidad_genero = models.CharField(max_length=2, choices=IDENTIDAD_GENERO_CHOICES, blank=True, null=False)
    zona_territorial = models.CharField(max_length=2, choices=ZONA_TERRITORIAL_CHOICES, blank=True, null=False)

    codigo_ocupacion = models.ForeignKey(Ocupacion, on_delete=models.SET_NULL, null=True, blank=True)
    id_etnia = models.ForeignKey(Etnia, on_delete=models.SET_NULL, null=True, blank=True)
    id_comunidad = models.ForeignKey(Comunidad, on_delete=models.SET_NULL, null=True, blank=True)
    id_pais_residencia = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    codigo_municipio_RH = models.ForeignKey(MunicipioResidenciaHabitual, on_delete=models.SET_NULL, null=True, blank=True)
    codigo_entidad_salud = models.ForeignKey(EntidadSalud, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["documento"]
        db_table = "paciente"

    def __str__(self):
        return f"{self.primero_apellido} {self.segundo_apellido or ''}, {self.primero_nombre} ({self.documento})"


# RELACIONES PACIENTE

class CategoriaDiscapacidad(models.Model):
    codigo_discapacidad = models.CharField(max_length=2, primary_key=True, null=False)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Categoría de discapacidad"
        verbose_name_plural = "Categorías de discapacidad"
        ordering = ["codigo_discapacidad"]
        db_table = "categoria_discapacidad"

    def __str__(self):
        return self.descripcion


class PacienteDiscapacidad(models.Model):
    paciente_uuid = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    codigo_discapacidad = models.ForeignKey(CategoriaDiscapacidad, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Paciente - Discapacidad"
        verbose_name_plural = "Pacientes - Discapacidades"
        unique_together = ("paciente_uuid", "codigo_discapacidad")
        db_table = "paciente_discapacidad"

    def __str__(self):
        return f"{self.paciente_uuid} → {self.codigo_discapacidad}"

# TABLA INTERMEDIA PARA RELACIÓN MUCHOS A MUCHOS

class PacienteNacionalidad(models.Model):
    paciente_uuid = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Paciente - Nacionalidad"
        verbose_name_plural = "Pacientes - Nacionalidades"
        unique_together = ("paciente_uuid", "id_pais")
        db_table = "paciente_nacionalidad"

    def __str__(self):
        return f"{self.paciente_uuid} - {self.id_pais}"


class DocumentoVoluntadAnticipada(models.Model):
    paciente_uuid = models.OneToOneField(Paciente, on_delete=models.CASCADE, primary_key=True)
    voluntad = models.CharField(max_length=2)
    fecha = models.DateTimeField(null=False)
    codigo_entidad = models.ForeignKey(EntidadSalud, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Documento de voluntad anticipada"
        verbose_name_plural = "Documentos de voluntad anticipada"
        ordering = ["-fecha"]
        db_table = "documento_voluntad_anticipada"

    def __str__(self):
        return f"Voluntad {self.voluntad} - {self.paciente_uuid}"


class OposicionPresuncionDonacion(models.Model):
    paciente_uuid = models.OneToOneField(Paciente, on_delete=models.CASCADE, primary_key=True, null=False )
    manifestacion = models.CharField(max_length=2, null=True)
    fecha = models.DateTimeField(null=False)

    class Meta:
        verbose_name = "Oposición a presunción de donación"
        verbose_name_plural = "Oposiciones a presunción de donación"
        ordering = ["-fecha"]
        db_table = "oposicion_presuncion_donacion"

    def __str__(self):
        return f"Oposición {self.manifestacion} - {self.paciente_uuid}"


# CONTACTO SERVICIO DE SALUD


class ContactoServicioSalud(models.Model):
    id_atencion_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha_atencion = models.DateTimeField(null=False)
    grupo_servicios = models.CharField(max_length=2, choices=GRUPO_SERVICIOS_CHOICES)
    entorno_atencion = models.CharField(max_length=2, choices=ENTORNO_ATENCION_CHOICES)
    fecha_triage = models.DateTimeField(null=False)
    clasificacion_triage = models.CharField(max_length=2, choices=TRIAGE_CHOICES, blank=True, null=True)

    paciente_uuid = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    codigo_entidad_salud = models.ForeignKey(EntidadSalud, on_delete=models.SET_NULL, null=True, blank=True)
    codigo_causa_atencion = models.ForeignKey(CausaMotivoAtencion, on_delete=models.SET_NULL, null=True, blank=True)
    codigo_modalidad_servicio = models.ForeignKey(ModalidadServicio, on_delete=models.SET_NULL, null=True, blank=True)
    codigo_via_ingreso = models.ForeignKey(ViaIngresoUsuario, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Contacto con el servicio de salud"
        verbose_name_plural = "Contactos con el servicio de salud"
        ordering = ["-fecha_atencion"]
        db_table = "contacto_servicio_salud"

    def __str__(self):
        return f"Atención {self.id_atencion_uuid} - {self.paciente_uuid} - {self.fecha_atencion}"


class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    tipo_diagnostico = models.CharField(max_length=2, choices=TIPO_DIAGNOSTICO_CHOICES)
    id_atencion_uuid = models.ForeignKey(ContactoServicioSalud, on_delete=models.CASCADE, related_name="diagnosticos")
    codigo_cie10 = models.ForeignKey(CIE10, on_delete=models.SET_NULL, null=True, blank=True)
    codigo_enfermedad_huerfana = models.ForeignKey(EnfermedadHuerfana, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Diagnóstico"
        verbose_name_plural = "Diagnósticos"
        ordering = ["-id_diagnostico"]
        db_table = "diagnostico"

    def __str__(self):
        return f"Diag {self.id_diagnostico} - {dict(TIPO_DIAGNOSTICO_CHOICES).get(self.tipo_diagnostico, self.tipo_diagnostico)}"


