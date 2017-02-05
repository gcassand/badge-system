from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from models import Model3d
from forms import Model3dForm


class Model3dCreateView(CreateView):
    model = Model3d
    form_class = Model3dForm
    template_name = "model-create.html"

    def form_valid(self, form):
        model3d = form.save(commit=False)
        model3d.user = User.objects.get(user=self.request.user)
        model3d.save()
        return super(CreateView, self).form_valid(form)


class Model3dDetailView(DetailView):
    model = Model3d
    template_name = "model-detail.html"

    def dispatch(self, *args, **kwargs):
        # check visited in session to count views
        if "visited" not in self.request.session:
            model3d = get_object_or_404(Model3d, pk=kwargs["pk"])
            model3d.update_count()
            self.request.session['visited'] = True
        return super(DetailView, self).dispatch(*args, **kwargs)
