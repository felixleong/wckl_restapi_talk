from django.contrib import admin
from restapi_talk.fundtracking.models import FundHouse, Fund, Price, Annotation


class FundHouseAdmin(admin.ModelAdmin):
    list_display = ('name', )


class FundAdmin(admin.ModelAdmin):
    list_display = ('fund_house', 'code', 'name', )


class PriceAdmin(admin.ModelAdmin):
    list_display = ('fund', 'date', 'nav',)
    list_filter = ('date',)
    search_fields = ('fund__code', 'fund__name',)


class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('price', 'time_added', )


# Add the admin modules
admin.site.register(FundHouse, FundHouseAdmin)
admin.site.register(Fund, FundAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Annotation, AnnotationAdmin)
