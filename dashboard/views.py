from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SheetForm


class ArticleCreateView(LoginRequiredMixin, FormView):
	template_name = 'dashboard/main/index.html'
	form_class = SheetForm
	login_url = '/accounts/login/'

	def form_valid(self, form):
		sheet = form.save(commit=False)
		sheet.owner = self.request.user
		sheet.save()

		return redirect('/')
