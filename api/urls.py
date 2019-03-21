from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from api import views
from api.views import RankViewSet


router = DefaultRouter()
router.register(r'rank', RankViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('rank/', views.RankList.as_view()),
    # path('rank/<int:pk>/', views.RankDetail.as_view()),
]
