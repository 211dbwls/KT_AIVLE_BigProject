from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.boards, name='boards'),
    path('posting/', views.posting, name='posting'),
    path('faq_detail/<bpk>', views.faq_detail, name='faq_detail'),
    path('inquiry_detail/<bpk>', views.inquiry_detail, name='inquiry_detail'),
    path('update/<bpk>', views.update, name='update'),
    path('delete/<bpk>', views.delete, name='delete'),
    path('creply/<bpk>', views.creply, name='creply'),
    path('dreply/<bpk>/<rpk>', views.dreply, name='dreply'),
    
    path('faq/', views.faq, name='faq'),
    path('inquiry/', views.inquiry, name='inquiry'),
    
    path('test/', views.test, name='test'),
]
