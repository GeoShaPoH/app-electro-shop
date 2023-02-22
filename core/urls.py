from django.urls import path
from .views import SearchResultsView
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    HomeViewM,
    HomeViewCA,
    HomeViewCN,
    HomeViewFBPCBS,
    HomeViewSE,
    OrderSummaryView,
    send_message,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('modulos/', HomeViewM.as_view(), name='modulos'),
    path('cables/', HomeViewCA.as_view(), name='cables'),
    path('conectores/', HomeViewCN.as_view(), name='conectores'),
    path('PCBs/', HomeViewFBPCBS.as_view(), name='pcbs'),
    path('sensores/', HomeViewSE.as_view(), name='sensores'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('send_message/', send_message, name='send-message'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
