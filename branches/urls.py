from django.conf.urls import url
from branches import views
# from branches.views import BranchListView

urlpatterns = [
    url('^branches/$', views.BranchesApi),
    # url('^branches/$', BranchListView.as_view(), name='list-view'),
    url('^branches/([0-9]+)$', views.BranchesApi),
]
