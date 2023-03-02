from django.urls import path

from . import views

app_name = 'customer'
urlpatterns = [
	# path('customer_search/', views.customer_search, name='customer_search'),
	path('list/<user_id>', views.friends_list_view, name='list'),
	path('friend_remove/', views.remove_friend, name='remove-friend'),
    path('friend_request/', views.send_friend_request, name='friend-request'),
    path('friend_request_cancel/', views.cancel_friend_request, name='friend-request-cancel'),
    path('friend_requests/<user_id>/', views.friend_requests, name='friend-requests'),
    path('friend_request_accept/<friend_request_id>/', views.accept_friend_request, name='friend-request-accept'),
    path('friend_request_decline/<friend_request_id>/', views.decline_friend_request, name='friend-request-decline'),
	# path('list/<user_id>', views.customer_search, name='search'),
]
