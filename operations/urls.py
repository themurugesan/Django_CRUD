from django.urls import path
from .import views

urlpatterns=[
    path("",views.index,name="read"),
    path("create/",views.create,name="create"),
    path("update/<int:id>",views.update,name="update"),
    path("delete/<int:id>",views.delete,name="delete")
    
]