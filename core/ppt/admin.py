from django.contrib import admin

from core.ppt.models import Pais
from core.ppt.models import Barrio, Cargo, Ciudad, Comuna, Etnia, Hobby, Lider, Profesion, Puesto

admin.site.register(Pais)
admin.site.register(Barrio)
admin.site.register(Ciudad)
admin.site.register(Cargo)
admin.site.register(Comuna)
admin.site.register(Hobby)
admin.site.register(Etnia)
admin.site.register(Lider)
admin.site.register(Profesion)
admin.site.register(Puesto)
