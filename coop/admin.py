from django.contrib import admin
from .models import Batch, Member, Vehicle, Document


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ["number"]
    search_fields = ["number"]


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["name", "gmail", "batch", "file_number", "renewal_date"]
    search_fields = ["name", "gmail", "file_number"]
    list_filter = ["batch", "renewal_date"]


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [
        "plate_number",
        "engine_number",
        "chassis_number",
        "make_brand",
        "body_type",
        "year_model",
        "series",
        "color",
        "member",
    ]
    search_fields = [
        "plate_number",
        "engine_number",
        "chassis_number",
        "make_brand",
        "body_type",
        "series",
        "color",
    ]
    list_filter = ["make_brand", "body_type", "year_model"]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["vehicle", "official_receipt", "certificate_of_registration"]
    search_fields = ["vehicle__plate_number"]
    list_filter = ["vehicle__member__renewal_date"]
