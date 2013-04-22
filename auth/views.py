from django.shortcuts import redirect, render_to_response, HttpResponseRedirect, HttpResponse
from auth.models import FailedLogin, BannedIP, User
from auth.forms import LoginForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.mail import mail_admins

from urlparse import urlparse
from datetime import datetime, timedelta

from inventory import settings


def get_safe_url(url, safehost):
	parsed = urlparse(url)
	if parsed.netloc and parsed.netloc != safehost:
		#this is bad redirect to home
		return '/'
	else:
		return url

def login(request):
	if request.method == 'POST':
		ip = request.META['REMOTE_ADDR']
		# check for banned ip
		banned = BannedIP.objects.values_list('ip')
		if len(banned)>0 and ip in banned[0]:
			return HttpResponseRedirect(settings.LOGIN_URL)

		# check for more than 3 failed attempts in the last 5 minutes
		dt = datetime.now() - timedelta(minutes=5)
		if FailedLogin.objects.filter(added__gt=dt).count() > 2:
			b = BannedIP()
			b.ip = ip
			b.save()
			return HttpResponseRedirect(settings.LOGIN_URL)

		success_redirect = get_safe_url(request.GET['next'], request.get_host()) if request.GET.get('next') else '/'
		
		return process_login(request, success_redirect, settings.LOGIN_URL)

	else:
		f = LoginForm()

	return render_to_response('login.html', {'form':f.as_p()}, context_instance=RequestContext(request))


def process_login(request, success_redirect=None, error_redirect=None, success_response=None):
	f = LoginForm(request.POST)
	
	if f.is_valid():
		u = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if u:
			if u.is_active:
				auth.login(request, u)

				if success_redirect:
					return HttpResponseRedirect(success_redirect)
				elif success_response:
					return success_response
				else:
					return HttpResponse(200)

			else:
				mail_admins('Inactive user attempted to login', '')

				if error_redirect:
					return HttpResponseRedirect(error_redirect)
				else:
					return HttpResponse(status=403)

		else:
			f = FailedLogin()
			f.ip = request.META['REMOTE_ADDR']
			f.save()

			mail_admins('Failed login attempt', '')
			if error_redirect:
				return HttpResponseRedirect(error_redirect)
			else:
				return HttpResponse(status=403)

	else:
		return False





@login_required()
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

