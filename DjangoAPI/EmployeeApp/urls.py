
from django.urls import path, include

from EmployeeApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('departement/', views.departementApi),
    path('departement/<int:id>', views.departementApi),
    path('employee/', views.employeeApi),
    path('employee/<int:id>', views.employeeApi),

    path('Employee/SaveFile', views.SaveFile),

] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)