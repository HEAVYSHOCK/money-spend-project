"""Views for spends app"""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.spends.api.serializers import (
    SpendsSerializer,
    CategorySerializer,
    CurrencySerializer
)
from apps.spends.models import (
    Spends,
    Category,
    Currency
)


class SpendsListCreateAPIView(ListCreateAPIView):
    """List all spends, or create a new spend."""
    serializer_class = SpendsSerializer
    queryset = Spends.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class CurrencyListCreateAPIView(ListCreateAPIView):
    """List all currencies, or create a new currency."""
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class CategoryListCreateAPIView(ListCreateAPIView):
    """List all categories, or create a new category."""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SpendsDetailAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating or deleting a specific spend."""
    serializer_class = SpendsSerializer
    queryset = Spends.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class CurrencyDetailAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating or deleting a specific currency."""
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating or deleting a specific category."""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
