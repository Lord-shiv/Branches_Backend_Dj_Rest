from django.contrib import admin
from django.urls import path
# from rest_framework import routers

from django.conf.urls import url, include
# router = routers.DefaultRouter()
# router.register('branches', BranchListView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    url(r'', include('branches.urls'))
]
