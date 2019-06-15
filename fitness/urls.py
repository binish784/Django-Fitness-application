from django.urls import path

from . import views
from .api import views as api_views

app_name='fitness'

urlpatterns = [
	path('',views.IndexView,name='index'),
	path('set-workout/',views.SetWorkoutView,name='set-workout'),
	path('detail-workout/<int:workout_id>',views.DetailWorkoutView,name='detail-workout'),
	path('<int:set_id>/set-details',views.SetDetailView,name='set-detail'),
	path('profile/',views.ProfileView,name='profile'),
	path('update-profile/',views.UpdateProfileView,name='updateProfile'),
	path('weight-statistics/',views.StatsView,name='weight-statistics'),

	#api
	path('api/list-weight',api_views.WeightWeekStat.as_view(),name='weight-week-stat'),
	path('api/monthly-weight',api_views.WeightMonthStat.as_view(),name='weight-month_stat'),
	path('api/<int:pk>/workout-list/',api_views.WorkoutListAPIView.as_view(),name='workout-list'),
	path('api/workout-set/',api_views.WorkoutSetAPIView.as_view(),name='workout-set')
]
