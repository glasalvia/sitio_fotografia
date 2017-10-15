from django.contrib import admin
from apps.equipo.models import Camara, Lente, Apertura, ISO, Velocidad


# Register your models here.


admin.site.register(Camara)
admin.site.register(Lente)
admin.site.register(Apertura)
admin.site.register(ISO)
admin.site.register(Velocidad)

