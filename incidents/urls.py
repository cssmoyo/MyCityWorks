from django.urls import path
from . import views

app_name = 'incidents'


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('report/', views.report_incident, name='report'),
    path('incidents/', views.incidents_list, name='incidents_list'),
    path('incident/<int:incident_id>/', views.incident, name='incident'),
    path("my-incidents/", views.my_incidents, name="my_incidents"),
    path("councillor/", views.councillor_dashboard, name="councillor_dashboard"),
    path("incident/<int:incident_id>/update/", views.update_status,name="update_status"),
    path("comment/<int:comment_id>/edit/",views.edit_comment, name="edit_comment"),
    path("mayor/", views.mayor_dashboard, name="mayor_dashboard")


    ]