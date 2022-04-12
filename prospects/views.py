from django.shortcuts import render
from django.utils import timezone
from .models import Prospecters
from .forms import ProspectsForm

# Create your views here.

def prospects_index(request):
	prospects = Prospecters.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'prospects/prospects_index.html', {'prospects': prospects})

def prospects_sign_in(request):
	prospects = Prospecters.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'prospects/prospects_sign_in.html', {'prospects': prospects})

def prospects_list(request):
	prospects = Prospecters.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'prospects/prospects_list.html', {'prospects': prospects})

def prospects_register(request):

	if request.method == "POST":
		form = ProspectsForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.sponsor = request.user
			post.published_date = timezone.now()
			post.save()
			return render('prospects/prospects_list', pk=post.pk)
	else:
		form = ProspectsForm()
		return render(request, 'prospects/prospects_register.html', {'form': form})