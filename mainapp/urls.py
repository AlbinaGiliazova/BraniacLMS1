from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("news/", views.NewsPageView.as_view(), name="news"),
    path("news/<int:pk>/", views.NewsPageDetailView.as_view(), name="news_detail"),
    path("courses/", views.CoursesListView.as_view(), name="courses"),
    path(
        "courses/<int:pk>/",
        views.CoursesDetailView.as_view(),
        name="courses_detail",
    ),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
