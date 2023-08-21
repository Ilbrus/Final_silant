from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
from import_export import resources
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'

class UserAdmin(UserAdmin):
    inlines = (UserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class TechnicResource(resources.ModelResource):
    class Meta:
        model = Technic
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(Technic)
class TechnicAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = TechnicResource
    list_display = ('id','name','description',)
    filter = ('name',)

class EngineResource(resources.ModelResource):
    class Meta:
        model = Engine
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(Engine)
class EngineAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = EngineResource
    list_display = ('id','name','description',)
    filter = ('name',)

class TransmissionResource(resources.ModelResource):
    class Meta:
        model = Transmission
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(Transmission)
class TransmissionAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = TransmissionResource
    list_display = ('id','name','description',)
    filter = ('name',)

class DrivingBridgeResource(resources.ModelResource):
    class Meta:
        model = DrivingBridge
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(DrivingBridge)
class DrivingBridgeAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = DrivingBridgeResource
    list_display = ('id','name','description',)
    filter = ('name',)

class ControlledBridgeResource(resources.ModelResource):
    class Meta:
        model = ControlledBridge
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(ControlledBridge)
class ControlledBridgeAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = ControlledBridgeResource
    list_display = ('id','name','description',)
    filter = ('name',)

class CarResource(resources.ModelResource):
    class Meta:
        model = Car
        report_skipped = True
        fields = (
        'id',
        'car_number',
        'technic',
        'engine',
        'engine_number',
        'transmission',
        'transmission_number',
        'driving_bridge',
        'driving_bridge_number',
        'controlled_bridge',
        'controlled_bridge_number',
        'delivery_contract',
        'date_shipment',
        'сonsignee',
        'delivery_address',
        'equipment',
        'client',
        'service_company',
        )

@admin.register(Car)
class CarAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = CarResource
    list_display = (
        'id',
        'car_number',
        'technic',
        'engine',
        'transmission',
        'driving_bridge',
        'controlled_bridge',
        'date_shipment',
        'equipment',
        'client',
        'service_company',
    )
    filter = ('car_number',)
