from django.contrib import admin
from myapp1.models import Worker, Adopters

# Added databases to admin panel
admin.site.register(Worker)
admin.site.register(Adopters)


# Register your models here.
