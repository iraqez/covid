from django.contrib import admin
from .models import Hospitals, Nomenclature, Rayon, NomenclatureCount


@admin.register(Rayon)
class RayonAdmin(admin.ModelAdmin):
    pass


@admin.register(Nomenclature)
class NomenclatureAdmin(admin.ModelAdmin):
    list_display = ('groupNomenlature', 'name',)
    list_filter = ('groupNomenlature',)
    list_display_links = ('name',)


# @admin.register(NomenclatureCount)
# class NomenclatureCountAdmin(admin.ModelAdmin):
#     list_display = ('nomenclature', 'potreba',)


class NomenclatureCountInline(admin.TabularInline):
    model = NomenclatureCount
    fields = ('nomenclature', 'potreba', 'nayavnist', 'neobhidno',)
    readonly_fields = ('neobhidno', 'nomenclature')
    sortable_by = ('nomenclature',)



@admin.register(Hospitals)
class HospitalsAdmin(admin.ModelAdmin):
    list_display = ('name', 'rayon',)
    list_filter = ('rayon',)
    list_display_links = ('name',)
    search_field = ('rayon',)
    fields = ('name', 'rayon',)
    inlines = [NomenclatureCountInline]




