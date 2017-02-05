from django.conf.urls import url
from views import Model3dCreateView, Model3dDetailView

urlpatterns = [
    url(r'^create/$', Model3dCreateView.as_view(), name='model-create'),
    url(r'^(?P<pk>\d+)/$', Model3dDetailView.as_view(), name='model-detail'),
]
