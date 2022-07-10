from django.urls import path,include
from . import views
#from .views import TopView,SnsCreateView,SnsDeleteView,MySnsShowView,SnsCommentView,SnsCommentIndex
from django.conf import settings
from django.conf.urls.static import static
from .views import TopView

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('ajax-number/', views.ajax_number, name='ajax_number'),
    #path('res/', views.Res, name='res'),
]