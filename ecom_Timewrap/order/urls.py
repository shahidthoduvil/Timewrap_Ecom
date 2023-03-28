from django.urls import path
from .import views,views2




urlpatterns = [

    path('success-page/',views.success_page,name="success_page"),
    path('order-list/', views.order_list, name="order_list"),
    path('order-details/<str:order_id>/', views.order_details, name="order_details"),
    path('order-tracking/<int:item_id>/', views.order_tracking, name="order_tracking"),
    path('invoice/<str:order_id>/', views.invoice, name="invoice"),
    path('refund/',views.refund,name="refund"),
    path('cancel_order/<int:item_id>/<str:order_id>',views.cancel_order,name="cancel_order"),
#................................................. admin_side-------------
    path('adm/order-list',views2.orderlist,name="orderlist"),
    path('adm/coupon',views2.coupon_list,name="coupon"),
    path('adm/add_coupon',views2.add_coupon,name="add_coupon"),
    path('adm/delete_coupon',views2.delete_coupon,name="delete_coupon"),
    path('ordered-items/<int:id>/', views2.order_items,name="order_items"),
    path('status-update/<int:id>/', views2.status_update,name="status_update"),

    

]


    
