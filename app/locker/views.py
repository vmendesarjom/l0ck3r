from datetime import datetime, timedelta

from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy, reverse

from . import models

# Projectors list view
#-------------------
class ProjectorView(ListView):

    model = models.Projector
    template_name = 'locker/projector/list.html'

# Projector create view
#-------------------
class ProjectorCreateView(CreateView):

    model = models.Projector
    template_name = 'locker/projector/form.html'
    success_url = reverse_lazy('locker:projector-list')
    fields = ['tipping', 'type', 'note', 'cable','status']

# Projector edit
#-------------------
class ProjectorEditView(UpdateView):

    model = models.Projector
    template_name = 'locker/projector/update.html'
    success_url = reverse_lazy('locker:projector-list')
    fields = ['tipping', 'type', 'note', 'cable', 'status']


#Reserve list view
#-------------------
class ReserveView(ListView):

    model = models.Reserve
    template_name = 'locker/reserve/list.html'

    def get_context_data(self, **kwargs):
        if self.request.user.is_staff:
            kwargs['object_list'] = models.Reserve.objects.all()
        else:
            kwargs['object_list'] = models.Reserve.objects.filter(user = self.request.user)
        return super(ReserveView, self).get_context_data(**kwargs) 

# Reserve create view
#-------------------
class ReserveCreateView(TemplateView):
    
    #model = models.Reserve
    template_name = 'locker/reserve/reserve.html'
    #success_url = reverse_lazy('locker:projector-list')
    #fields = ['user', 'date', 'projector', 'slots']

    def get_context_data(self, **kwargs):
        # TODO: Se a data nao vier na URL
        date = datetime.today()
        # Days
        kwargs['days'] = []
        i = 1
        for day in range(0, date.weekday()):
            kwargs['days'].append( (date - timedelta(days=i)).day )
            i += 1
        
        i = 0
        for day in range(date.weekday(), 5):
            kwargs['days'].append( (date + timedelta(days=i)).day )
            i += 1

        # Slots
        kwargs['slots'] = models.Slot.objects.all().order_by('turn', 'name')
        return super(ReserveCreateView, self).get_context_data(**kwargs)
    
    def post(self, request, *args, **kwargs):
        r = models.Reserve()
        tipo = request.POST.get("erro")
        reserves = models.Reserve.objects.all()
        projectors = models.Projector.objects.all()
        r.user = self.request.user
        r.date = datetime.now()
        # TODO: Search projector
        for p in projectors:
            if tipo == p.type:
                for res in reserves:
                    if res.projector == p:
                        pass
                    else:    
                        r.projector = models.Projector.objects.get(p.tipping)
        #r.projector = models.Projector.objects.first()
        # TODO: Ver uma forma melhor de pegar os dias
        r.save()
        #r.slots.add(self.request.POST['4'])
        #r.save()

        return HttpResponseRedirect(reverse('locker:reserve-list'))

# Reserve remove view 
#-------------------
class ReserveDeleteView(DeleteView):
    
    model = models.Reserve
    success_url = reverse_lazy('locker:reserve-list')
    
# Reserver detail view
#-------------------
class ReserveDetailView(DetailView):

    model = models.Reserve
    template_name = 'locker/reserve_confirm_delate.html'