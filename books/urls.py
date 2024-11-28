from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookAPIView,BookDetailAPIView,BookUpdateAPIView,BookDeleteAPIView,BookCreateAPIView,BookViewSet

router=SimpleRouter()
router.register('books',BookViewSet,basename='books')
urlpatterns=[
        # path('books/',BookAPIView.as_view()),
        # path('books/<int:pk>/', BookDetailAPIView.as_view()),
        # path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
        # path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
        # path('books/create/', BookCreateAPIView.as_view()),
]

urlpatterns=urlpatterns+router.urls