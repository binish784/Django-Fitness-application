from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .forms import LogForm,LogDetailForm
from .models import log, logDetail


# Create your views here.

@login_required
def IndexView(request):
	form=LogForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(form.instance.get_absolute_url())
	recent_logs=log.objects.order_by('-pk')[:5]
	return render(request,'log/index.html',{'form':form,'recent_logs':recent_logs})


@login_required
def LogDetailView(request,log_id):
	selected_log=get_object_or_404(log,pk=log_id)
	#setform=LogSetForm(request.POST or None)
	form=LogDetailForm(request.POST or None)
	#if setform.is_valid():
	if form.is_valid():
			#setform.save()
		form.save()
		form.instance.parent_log=selected_log
		return HttpResponseRedirect(reverse('log:logDetails',kwargs={'log_id':selected_log.id}))
	return render(request,'log/logDetails.html',{'form':form,'log':selected_log})

@login_required
def DeleteRecordView(request,record_id):
	selected_log=get_object_or_404(logDetail,pk=record_id)
	if request.method=='POST':
		selected_log.delete()
		return HttpResponseRedirect(selected_log.parent_log.get_absolute_url());
	else:
		return render(request,'log/deleteLogDetail.html',{'record':selected_log});
	
