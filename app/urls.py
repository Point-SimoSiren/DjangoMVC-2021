from django.urls import path
from .views import landingview, supplierlistview, addsupplier, deletesupplier

urlpatterns = [
    path('landing/', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
]
