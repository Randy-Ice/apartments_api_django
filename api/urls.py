from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apartments.views import ApartmentView, ApartmentDetailView, CommentViewSet, NoteViewSet, AddressViewSet, \
    PointsOfInterestsViewSet, ActivitiesViewSet

router = DefaultRouter()
router.register('comments', CommentViewSet)
router.register('notes', NoteViewSet)
router.register('address', AddressViewSet)
router.register('point-of-interests', PointsOfInterestsViewSet)
router.register('activities', ActivitiesViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('apartments/', ApartmentView.as_view()),
    path('apartments/<uuid:pk>/', ApartmentDetailView.as_view()),

]