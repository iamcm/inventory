from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from core.forms import CollectionForm, ItemForm, FileForm 
from core.models import Collection, Item, File

class IndexView(ListView):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        self.queryset = Collection.objects.filter(user=request.user)
        return super(self.__class__, self).get(request, *args, **kwargs)


class CollectionCreateView(CreateView):
    template_name = 'form.html'
    form_class = CollectionForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.user = self.request.user
        form.save()

        return super(CollectionCreateView, self).form_valid(form)


class CollectionUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = CollectionForm
    success_url = '/'

    def get(self, request, pk, *args, **kwargs):
        self.queryset = Collection.objects.filter(pk=pk)
        return super(self.__class__, self).get(request, pk, *args, **kwargs)

    def post(self, request, pk, *args, **kwargs):
        self.queryset = Collection.objects.filter(pk=pk)
        return super(self.__class__, self).post(request, pk, *args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()

        return super(self.__class__, self).form_valid(form)


class ItemCreateView(CreateView):
    template_name = 'form.html'
    form_class = ItemForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.user = self.request.user
        form.save()

        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = ItemForm
    success_url = '/'

    def get(self, request, pk, *args, **kwargs):
        self.queryset = Item.objects.filter(pk=pk)
        return super(self.__class__, self).get(request, pk, *args, **kwargs)

    def post(self, request, pk, *args, **kwargs):
        self.queryset = Item.objects.filter(pk=pk)
        return super(self.__class__, self).post(request, pk, *args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()

        return super(self.__class__, self).form_valid(form)