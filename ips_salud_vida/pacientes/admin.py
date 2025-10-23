from django.contrib import admin
from . import models

admin.site.site_header = "Administración Salud y Vida"
admin.site.site_title = "Panel Salud y Vida"
admin.site.index_title = "Panel Administrativo - Salud y Vida"

class PacienteDiscapacidadInline(admin.TabularInline):
    model = models.PacienteDiscapacidad
    extra = 0
    raw_id_fields = ("paciente_uuid",)

class PacienteNacionalidadInline(admin.TabularInline):
    model = models.PacienteNacionalidad
    extra = 0
    raw_id_fields = ("paciente_uuid",)

class DiagnosticoInline(admin.TabularInline):
    model = models.Diagnostico
    extra = 0
    raw_id_fields = ("codigo_cie10", "codigo_enfermedad_huerfana")

@admin.register(models.Ocupacion)
class OcupacionAdmin(admin.ModelAdmin):
    list_display = ("codigo_ocupacion", "nombre")
    search_fields = ("codigo_ocupacion", "nombre")

@admin.register(models.Etnia)
class EtniaAdmin(admin.ModelAdmin):
    list_display = ("id_etnia", "descripcion")
    search_fields = ("descripcion",)

@admin.register(models.Comunidad)
class ComunidadAdmin(admin.ModelAdmin):
    list_display = ("id_comunidad", "descripcion")
    search_fields = ("descripcion",)

@admin.register(models.MunicipioResidenciaHabitual)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ("codigo_municipio_RH", "nombre")
    search_fields = ("nombre",)

@admin.register(models.EntidadSalud)
class EntidadSaludAdmin(admin.ModelAdmin):
    list_display = ("codigo_entidad_salud", "nombre", "eps", "ips")
    search_fields = ("codigo_entidad_salud", "nombre")
    list_filter = ("eps", "ips")

@admin.register(models.TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ("tipo_documento", "descripcion")
    search_fields = ("descripcion",)

@admin.register(models.Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ("id_pais", "nombre","codigo_alfa_3")
    search_fields = ("id_pais","nombre", "codigo_alfa_3")
    list_per_page = 10

@admin.register(models.CIE10)
class CIE10Admin(admin.ModelAdmin):
    list_display = ("codigo_CIE10", "descripcion")
    search_fields = ("codigo_CIE10", "descripcion")
    list_per_page = 10

@admin.register(models.EnfermedadHuerfana)
class EnfermedadHuerfanaAdmin(admin.ModelAdmin):
    list_display = ("codigo_enfermedades_huerfanas", "descripcion")
    search_fields = ("descripcion",)
    list_per_page = 10

@admin.register(models.CausaMotivoAtencion)
class CausaMotivoAdmin(admin.ModelAdmin):
    list_display = ("codigo_causa_atencion", "descripcion")
    search_fields = ("descripcion",)


@admin.register(models.ModalidadServicio)
class ModalidadServicioAdmin(admin.ModelAdmin):
    list_display = ("codigo_modalidad_servicio", "descripcion")
    search_fields = ("descripcion",)


@admin.register(models.ViaIngresoUsuario)
class ViaIngresoAdmin(admin.ModelAdmin):
    list_display = ("codigo_via_ingreso", "descripcion")
    search_fields = ("descripcion",)

@admin.register(models.CategoriaDiscapacidad)
class CategoriaDiscapacidadAdmin(admin.ModelAdmin):
    list_display = ("codigo_discapacidad", "descripcion")
    search_fields = ("descripcion",)
    inlines = [PacienteDiscapacidadInline]

@admin.register(models.PacienteDiscapacidad)
class PacienteDiscapacidadAdmin(admin.ModelAdmin):
    list_display = ("paciente_uuid", "codigo_discapacidad")
    search_fields = ("paciente_uuid__documento", "codigo_discapacidad__descripcion")
    raw_id_fields = ("paciente_uuid", "codigo_discapacidad")

@admin.register(models.PacienteNacionalidad)
class PacienteNacionalidadAdmin(admin.ModelAdmin):
    list_display = ("paciente_uuid", "id_pais")
    search_fields = ("paciente_uuid__documento", "id_pais__nombre")
    raw_id_fields = ("paciente_uuid", "id_pais")

@admin.register(models.DocumentoVoluntadAnticipada)
class DocumentoVoluntadAnticipadaAdmin(admin.ModelAdmin):
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
    list_display = ("paciente_uuid", "manifestacion", "fecha")
    search_fields = ("paciente_uuid__documento",)
    raw_id_fields = ("paciente_uuid",)

@admin.register(models.Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ("id_diagnostico", "id_atencion_uuid", "get_tipo_diagnostico_display", "codigo_cie10", "codigo_enfermedad_huerfana")
    search_fields = ("id_atencion_uuid__id_atencion_uuid", "codigo_cie10__codigo_CIE10", "codigo_cie10__descripcion")
    list_filter = ("tipo_diagnostico",)
    raw_id_fields = ("id_atencion_uuid", "codigo_cie10", "codigo_enfermedad_huerfana")