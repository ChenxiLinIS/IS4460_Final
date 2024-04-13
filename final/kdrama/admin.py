from django.contrib import admin
from .models import kdrama,actor,prod_company,award,director

class KdramaAdmin(admin.ModelAdmin):
    pass

admin.site.register(kdrama)


class actorAdmin(admin.ModelAdmin):
    pass

admin.site.register(actor)

class prod_companyAdmin(admin.ModelAdmin):
    pass

admin.site.register(prod_company)

class awardAdmin(admin.ModelAdmin):
    pass

admin.site.register(award)

class directorAdmin(admin.ModelAdmin):
    pass

admin.site.register(director)




# Register your models here.
