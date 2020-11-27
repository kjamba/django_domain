from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from .models import Domens
from .forms import DomensForm
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
# from .script import CreateDomen
from .nginx import main_nginx
from .apache import main_apache
from .delete import delete_host
import os, sys
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect



# res = CreateDomen().save_base('site.ru','nginx')
class HomeListView(ListView):
    model = Domens
    template_name = 'index.html'
    context_object_name = 'domens_list'

class MainView(CreateView):
    model = Domens
    template_name = 'domens.html'
    context_object_name = 'domens_list'
    success_url = reverse_lazy('domens')
    form_class = DomensForm
    
    def get_context_data(self, **kwargs):
        kwargs['concert_list'] = Domens.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
                    
    def post(self, request):
        host = Domens.objects.all()
        form = DomensForm(request.POST or None)
        context = {
            'form': form,
            'host': host
            }
        if request.method == "POST":
            if form.is_valid():
                form_save=form.save(commit=False)
                domen = form_save.name
                print(domen) 
                print(form_save.webserver)
                if form_save.webserver == 'nginx':
                    main_nginx(domen)
                    form_save.save()
                if form_save.webserver == 'apache2':
                    main_apache(domen)
                    form_save.save()
                return redirect('/domens')
        return render(request, 'domens.html', context)

class DomenDeleteView(DeleteView):
    model = Domens
    template_name = 'domens.html'
    success_url = reverse_lazy('domens_page')
    # success_msg = 'Запись удалена'
    
    # def post(self, request, *args, **kwargs):
        # messages.success(self.request, self.success_msg)
        # return super().post(request)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        
        print(self.object.name)
        delete_host(self.object.name, self.object.webserver)
        print('deleted')
        
        self.object.delete()
        return HttpResponseRedirect(success_url)
