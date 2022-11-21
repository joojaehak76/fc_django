from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email', 'level')
    
    def changelist_view(self, request, extra_context=None):
        extra_context = { 'title': '사용자 목록' }
        
        return super().changelist_view(request, extra_context)
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        fcuer = Fcuser.objects.get(pk=object_id)
        extra_context = { 'title': f'{fcuer.email} 수정' }
        
        return super().changeform_view(request, object_id, form_url, extra_context)    
    
admin.site.register(Fcuser, FcuserAdmin)
