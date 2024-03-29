from django.contrib import admin
from .models import BurnHistory, GoldBar, Mint, Burn, BarHolder, EditBarStatus
from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from solo.admin import SingletonModelAdmin

# Register your models here.

class GoldBarResource(ModelResource):
    class Meta:
        model = GoldBar

class MintResource(ModelResource):
    class Meta:
        model = Mint

class BurnResource(ModelResource):
    class Meta:
        model = Burn

class BarHolderResource(ModelResource):
    class Meta:
        model = BarHolder

class BurnHistoryResource(ModelResource):
    class Meta:
        model = BurnHistory

class GoldBarAdmin(ImportExportModelAdmin):
    resource_class = GoldBarResource
    list_display = ('bar_number', 'warrant_number', 'escrow_date', 'is_deleted')
    list_filter = ('is_deleted', 'escrow_date')
    search_fields = ('bar_number', 'warrant_number')
    readonly_fields = ('escrow_date',)

class MintAdmin(ImportExportModelAdmin):
    resource_class = MintResource
    list_display = ('bar_details', 'mint_date', 'status', 'burnt')
    list_filter = ('burnt', 'mint_date')
    search_fields = ('bar_details__bar_number', 'mint_date')
    readonly_fields = ('mint_date',)

class BurnAdmin(ImportExportModelAdmin):
    resource_class = BurnResource
    list_display = ('bar_details', 'status', 'burnt_date')
    list_filter = ('burnt_date',)
    search_fields = ('bar_details__bar_number', 'burnt_date')
    readonly_fields = ('burnt_date',)

class BarHolderAdmin(ImportExportModelAdmin):
    resource_class = BarHolderResource
    list_display = ('bar_details', 'holder_xinfin_address', 'token_balance', 'holder_date')
    list_filter = ('holder_date',)
    search_fields = ('bar_details__bar_number', 'holder_xinfin_address')
    readonly_fields = ('holder_date',)

class BurnHistoryAdmin(ImportExportModelAdmin):
    resource_class = BurnHistoryResource
    list_display = ('burnt_bar', 'adjusted_bar', 'adjusted_user', 'adjusted_amount', 'tx_hash')
    list_filter = ('burnt_bar', 'adjusted_bar', 'adjusted_user', 'tx_hash')
    search_fields = ('burnt_bar__bar_number', 'adjusted_bar', 'adjusted_user', 'tx_hash')
    readonly_fields = ('burnt_bar', 'adjusted_bar', 'adjusted_user', 'adjusted_amount', 'tx_hash')

admin.site.register(GoldBar, GoldBarAdmin)
admin.site.register(Mint, MintAdmin)
admin.site.register(Burn, BurnAdmin)
admin.site.register(BarHolder, BarHolderAdmin)
admin.site.register(BurnHistory, BurnHistoryAdmin)
admin.site.register(EditBarStatus, SingletonModelAdmin)