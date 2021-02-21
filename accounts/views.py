from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class LogoutView(View):
	LOGOUT_REDIRECT_URL = '/'

	def get(self, request):
		logout(request)
		return redirect(self.LOGOUT_REDIRECT_URL)


class CustomLoginView(LoginView):
	form_class = AuthenticationForm
	template_name = 'accounts/login/index.html'

	LOGIN_REDIRECT_URL = '/'

	def get_redirect_url(self):
		next_page = self.request.GET.get('next', '')

		if not next_page:
			return self.LOGIN_REDIRECT_URL
			
		else:
			return next_page

	def form_valid(self, form):
		user = form.get_user()
		login(self.request, user)
		return super(CustomLoginView, self).form_valid(form)
