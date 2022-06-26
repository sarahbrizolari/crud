from django.urls import path
from django.contrib import admin

from .views import list_Locacao, create_Locacao, update_Locacao, delete_Locacao

urlpatterns = [

 path('list_Locacao', list_Locacao, name='list_Locacao'),
 path('new_Locacao', create_Locacao, name='create_Locacao'),
 path('update_Locacao/<int:id>/', update_Locacao, name='update_Locacao'),
 path('delete_Locacao/<int:id>/', delete_Locacao, name='delete_Locacao'),
 path('admin/', admin.site.urls),

]
