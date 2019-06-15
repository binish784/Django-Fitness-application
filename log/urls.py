from django.urls import path
from log.api import views as api_views
from . import views

app_name='log'

urlpatterns = [
	path('',views.IndexView,name='index'),	
	path('<int:log_id>/logDetails',views.LogDetailView,name='logDetails'),
	path('<int:record_id>/confirm_delete',views.DeleteRecordView,name='deleteRecord'),
	#api urls
	path('api/<int:log_id>/log-details-read/',api_views.logDetailReadAPIView.as_view(),name='log-details-read'),
	path('api/<int:log_id>/log-details-write/',api_views.logDetailWriteAPIView.as_view(),name='log-details-write'),

]
