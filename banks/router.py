from branches.viewsets import BrachViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('branch', BrachViewset)
