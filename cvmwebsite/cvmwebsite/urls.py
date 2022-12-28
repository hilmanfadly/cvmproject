
from django.contrib import admin
from django.urls import path,include
#from JobApply.views import index
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('JobApply/', include('JobApply.urls'), name='index')
]

