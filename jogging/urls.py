from rest_framework import routers
from jogging import views
from django.conf.urls import url, include
from jogging import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'records', views.RecordViewSet, basename="record")

urlpatterns = [
    url('', include(router.urls)),
    url('auth', jwt_views.TokenObtainPairView.as_view()),
    url('token_verify', views.TokenVerify.as_view()),
    url('signup', views.SignupView.as_view()),
]
