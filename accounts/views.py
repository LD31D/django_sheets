from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import logout


class LogoutView(View):
	LOGOUT_URL = '/'

	def get(self, request):
		logout(request)
		return redirect(self.LOGOUT_URL)

