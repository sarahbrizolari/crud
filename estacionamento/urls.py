from django.urls import path
from django.contrib import admin

from .views import list_Locacao, create_Locacao, update_Locacao, delete_Locacao

urlpatterns = [

 path('list_locacao', list_Locacao, name='list-Locacao'),
 path('new-Locacao', create_Locacao, name='create-Locacao'),
 path('update-Locacao/<int:id>/', update_Locacao, name='update-Locacao'),
 path('delete-Locacao/<int:id>/', delete_Locacao, name='delete-Locacao'),
 path('admin/', admin.site.urls),
]
