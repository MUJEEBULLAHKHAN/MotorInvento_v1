from django.contrib import admin

from .models import admins,make,model,years,addcar,addpart,sellpart,Project, Task

@admin.register(admins)
class admins_admin(admin.ModelAdmin):
    list_display = ("full_name","email","mobile_no","username","password","national_id","role")



class makeAdmin(admin.ModelAdmin):
    list_display = ["make_id",
"make_name"]

admin.site.register(make, makeAdmin)

class modelAdmin(admin.ModelAdmin):
    list_display = ["model_id",
"model_name",
"make"]

admin.site.register(model, modelAdmin)

class yearAdmin(admin.ModelAdmin):
    list_display = ["year_id",
"year"]

admin.site.register(years, yearAdmin)

class addcarAdmin(admin.ModelAdmin):
    list_display = ["car_id",
"purchase_price",
"purchase_date",
"year",
"model",
"make",
"admin"]

admin.site.register(addcar, addcarAdmin)

class addpartAdmin(admin.ModelAdmin):
    list_display = ["part_id",
"part_name",
"part_no",
"is_scrap",
"sell_price",
"part_location",
"year",
"model",
"make",
"admin"]

admin.site.register(addpart, addpartAdmin)

class sellpartAdmin(admin.ModelAdmin):
    list_display = ["sell_id",
"part_name",
"date",
"discount",
"discounted_amount",
"sell_price",
"sell_price_after_discount",
"quantity",
"sub_total",
"year",
"model",
"make",
"admin"]

admin.site.register(sellpart, sellpartAdmin)


admin.site.register(Project)