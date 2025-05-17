from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apartments.views import ApartmentView, ApartmentDetailView, CommentViewSet

router = DefaultRouter()
router.register('comments', CommentViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('apartments/', ApartmentView.as_view()),
    path('apartments/<uuid:pk>/', ApartmentDetailView.as_view()),

]