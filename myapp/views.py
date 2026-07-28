from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Item
from .forms import ItemForm


class OwnerQuerysetMixin(LoginRequiredMixin):
    def get_queryset(self):
        return Item.objects.filter(owner=self.request.user)


class ItemListView(OwnerQuerysetMixin, ListView):
    model = Item
    template_name = 'read.html'
    context_object_name = 'items'


class ItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'create_update.html'
    success_url = reverse_lazy('item_list')
    success_message = 'Item created successfully!'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ItemUpdateView(OwnerQuerysetMixin, SuccessMessageMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'create_update.html'
    success_url = reverse_lazy('item_list')
    success_message = 'Item updated successfully!'


def item_delete(request, pk):
    item = Item.objects.filter(pk=pk, owner=request.user).first()
    if item:
        item.delete()
    return redirect('item_list')