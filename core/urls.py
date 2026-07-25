from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),

    path("select-role/<str:role>/", views.select_role, name="select_role"),

    path("client/dashboard/", views.client_dashboard, name="client_dashboard"),

    path("cpa/dashboard/", views.cpa_dashboard, name="cpa_dashboard"),

    path("returns/", views.returns_list, name="returns"),

    path("returns/<int:return_id>/", views.return_detail, name="return_detail"),

    path("documents/", views.documents, name="documents"),

    path("documents/<int:document_id>/",
         views.document_detail, name="document_detail"),

    path("documents/detail/", views.document_detail, name="document_detail"),

    path("ai-review/<int:id>/", views.ai_review_detail, name="ai_review_detail"),

    path("ai-chat/", views.client_ai_chat, name="client_ai_chat"),

    path("messages/", views.messages, name="messages"),

    path("ai-review/", views.ai_review, name="ai_review"),

    path("status/", views.status, name="status"),

    path("return-workspace/<int:id>/",
         views.return_workplace, name="return_workspace"),
]
