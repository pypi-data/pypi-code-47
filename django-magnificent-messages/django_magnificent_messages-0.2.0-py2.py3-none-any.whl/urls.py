# """
# URLs for django_magnificent_messages
# """
# from django.urls import path
#
# from . import views
#
# app_name = 'django_magnificent_messages'
# urlpatterns = [
#     path(
#         "message/create",
#         views.MessageCreateView.as_view(),
#         name='Message_create',
#     ),
#     path(
#         "message/<int:pk>/delete",
#         views.MessageDeleteView.as_view(),
#         name='Message_delete',
#     ),
#     path(
#         "message/<int:pk>",
#         views.MessageDetailView.as_view(),
#         name='Message_detail',
#     ),
#     path(
#         "message/<int:pk>/update",
#         views.MessageUpdateView.as_view(),
#         name='Message_update',
#     ),
#     path(
#         "message",
#         views.MessageListView.as_view(),
#         name='Message_list',
#     ),
# ]
