from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication

from fitness.models import WorkoutSet
from log.models import logDetail
from .serializer import LogDetailReadSerializer,LogDetailWriteSerializer


class logDetailReadAPIView(generics.ListAPIView):

	model=logDetail
	serializer_class=LogDetailReadSerializer

	def get_queryset(self,*args,**kwargs):
		parent_log=self.kwargs['log_id']
		return logDetail.objects.filter(parent_log=parent_log)

class logDetailWriteAPIView(generics.CreateAPIView):
	model=logDetail
	serializer_class=LogDetailWriteSerializer

	def get_queryset(self,*args,**kwargs):
		parent_log=self.kwargs['log_id']
		return logDetail.objects.filter(parent_log=parent_log)
