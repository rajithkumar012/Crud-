from my_applications import views
from django.urls import path


urlpatterns = [
    # path("",views.home),
    # path('register',views.register)
    path("",views.home,name="home"),
    path('addData/',views.addData,name='addData'),
    path('updateData/<int:id>',views.updateData,name="updateData"),
    path('deleteData/<int:id>',views.deleteData,name="deleteData")
    
   
]
