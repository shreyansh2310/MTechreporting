from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='reporting-home'),
    path('student_login/',views.login,name='student_login'),
    path('admin-signup/',views.signup,name='admin-signup'),
    path('admin-logout/',views.logout,name='admin-logout'),
    path('reg_validate/',views.validate_candidate,name='reg_validate'),
    path('reporting-form/',views.reporting,name='reporting-form'),
    path('dynamic/',views.dynamic,name='dynamic'),
    path('dashboard/',views.dashboard,name='dashboard')
]
