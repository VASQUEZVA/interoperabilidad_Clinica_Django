"""
Este módulo define la configuración del panel administrativo para la aplicación de Salud y Vida.
Define las clases de administración y personalización del sitio de administración
para las entidades básicas y relaciones del sistema.
"""

from django.contrib import admin
from . import models

# Personalización general del panel administrativo de Django
admin.site.site_header = "Administración Salud y Vida"
admin.site.site_title = "Panel Salud y Vida"
admin.site.index_title = "Panel Administrativo - Salud y Vida"

# -----------------------------
# Inlines
# -----------------------------
class PacienteDiscapacidadInline(admin.TabularInline):
    """
    Permite visualizar y editar las discapacidades asociadas a un paciente
    directamente desde el panel de administración.
    """
    model = models.PacienteDiscapacidad
    extra = 0
    raw_id_fields = ("paciente_uuid",)

class PacienteNacionalidadInline(admin.TabularInline):
    """
    Muestra las nacionalidades relacionadas con cada paciente en el panel administrativo.
    """
    model = models.PacienteNacionalidad
    extra = 0
    raw_id_fields = ("paciente_uuid",)

class DiagnosticoInline(admin.TabularInline):
    """
    Permite gestionar los diagnósticos asociados a una atención médica.
    """
    model = models.Diagnostico
    extra = 0
    raw_id_fields = ("codigo_cie10", "codigo_enfermedad_huerfana")


# -----------------------------
# Modelos básicos
# -----------------------------
@admin.register(models.Ocupacion)
class OcupacionAdmin(admin.ModelAdmin):
    """Administra las ocupaciones registradas en el sistema."""
    list_display = ("codigo_ocupacion", "nombre")
    search_fields = ("codigo_ocupacion", "nombre")

@admin.register(models.Etnia)
class EtniaAdmin(admin.ModelAdmin):
    """Administra las etnias registradas en el sistema."""
    list_display = ("id_etnia", "descripcion")
    search_fields = ("descripcion",)

@admin.register(models.Comunidad)
class ComunidadAdmin(admin.ModelAdmin):
    """Administra las comunidades registradas en el sistema."""
    list_display = ("id_comunidad", "descripcion")
    search_fields = ("descripcion",)

@admin.register(models.MunicipioResidenciaHabitual)
class MunicipioAdmin(admin.ModelAdmin):
    """Administra los municipios de residencia habitual."""
    list_display = ("codigo_municipio_RH", "nombre")
    search_fields = ("nombre",)

@admin.register(models.EntidadSalud)
class EntidadSaludAdmin(admin.ModelAdmin):
    """Administra las entidades de salud (EPS e IPS) del sistema."""
    list_display = ("codigo_entidad_salud", "nombre", "eps", "ips")
    search_fields = ("codigo_entidad_salud", "nombre")
    list_filter = ("eps", "ips")

@admin.register(models.TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    """Administra los tipos de documento disponibles en el sistema."""
    list_display = ("tipo_documento", "descripcion")
    search_fields = ("descripcion",)

@admin.register(models.Pais)
class PaisAdmin(admin.ModelAdmin):
    """Administra los países registrados en el sistema."""
    list_display = ("id_pais", "nombre","codigo_alfa_3")
    search_fields = ("id_pais","nombre", "codigo_alfa_3")
    list_per_page = 10

@admin.register(models.CIE10)
class CIE10Admin(admin.ModelAdmin):
    """Administra los códigos CIE10 de enfermedades."""
    list_display = ("codigo_CIE10", "descripcion")
    search_fields = ("codigo_CIE10", "descripcion")
    list_per_page = 10

@admin.register(models.EnfermedadHuerfana)
class EnfermedadHuerfanaAdmin(admin.ModelAdmin):
    """Administra las enfermedades huérfanas registradas."""
    list_display = ("codigo_enfermedades_huerfanas", "descripcion")
    search_fields = ("descripcion",)
    list_per_page = 10

@admin.register(models.CausaMotivoAtencion)
class CausaMotivoAdmin(admin.ModelAdmin):
    """Administra las causas o motivos de atención médica."""
    list_display = ("codigo_causa_atencion", "descripcion")
    search_fields = ("descripcion",)


@admin.register(models.ModalidadServicio)
class ModalidadServicioAdmin(admin.ModelAdmin):
    """Administra las modalidades de servicio médico."""
    list_display = ("codigo_modalidad_servicio", "descripcion")
    search_fields = ("descripcion",)


@admin.register(models.ViaIngresoUsuario)
class ViaIngresoAdmin(admin.ModelAdmin):
    """Administra las vías de ingreso del usuario al sistema de salud."""
    list_display = ("codigo_via_ingreso", "descripcion")
    search_fields = ("descripcion",)

@admin.register(models.CategoriaDiscapacidad)
class CategoriaDiscapacidadAdmin(admin.ModelAdmin):
    """Administra las categorías de discapacidad disponibles en el sistema."""
    list_display = ("codigo_discapacidad", "descripcion")
    search_fields = ("descripcion",)
    inlines = [PacienteDiscapacidadInline]


# -----------------------------
# Modelos relacionados con pacientes
# -----------------------------
@admin.register(models.PacienteDiscapacidad)
class PacienteDiscapacidadAdmin(admin.ModelAdmin):
    """Administra la relación entre pacientes y discapacidades."""
    list_display = ("paciente_uuid", "codigo_discapacidad")
    search_fields = ("paciente_uuid__documento", "codigo_discapacidad__descripcion")
    raw_id_fields = ("paciente_uuid", "codigo_discapacidad")

@admin.register(models.PacienteNacionalidad)
class PacienteNacionalidadAdmin(admin.ModelAdmin):
    """Administra la relación entre pacientes y nacionalidades."""
    list_display = ("paciente_uuid", "id_pais")
    search_fields = ("paciente_uuid__documento", "id_pais__nombre")
    raw_id_fields = ("paciente_uuid", "id_pais")

@admin.register(models.DocumentoVoluntadAnticipada)
class DocumentoVoluntadAnticipadaAdmin(admin.ModelAdmin):
    """Administra los documentos de voluntad anticipada de los pacientes."""
    list_display = ("paciente_uuid", "voluntad", "fecha", "codigo_entidad")
    search_fields = ("paciente_uuid__documento",)
    list_filter = ("voluntad",)
    raw_id_fields = ("paciente_uuid",)
    fieldsets = (
        ("Datos del paciente", {"fields": ("paciente_uuid",)}),
        ("Decisión", {"fields": ("voluntad", "fecha", "codigo_entidad")}),
    )

@admin.register(models.OposicionPresuncionDonacion)
class OposicionPresuncionDonacionAdmin(admin.ModelAdmin):
    """Administra los registros de oposición o presunción de donación de órganos."""
    list_display = ("paciente_uuid", "manifestacion", "fecha")
    search_fields = ("paciente_uuid__documento",)
    raw_id_fields = ("paciente_uuid",)

@admin.register(models.Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    """Administra los diagnósticos médicos asociados a las atenciones."""
    list_display = ("id_diagnostico", "id_atencion_uuid", "get_tipo_diagnostico_display", "codigo_cie10", "codigo_enfermedad_huerfana")
    search_fields = ("id_atencion_uuid__id_atencion_uuid", "codigo_cie10__codigo_CIE10", "codigo_cie10__descripcion")
    list_filter = ("tipo_diagnostico",)
    raw_id_fields = ("id_atencion_uuid", "codigo_cie10", "codigo_enfermedad_huerfana")