from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('companies', views.CompanyViewSet)

urlpatterns = router.urls
