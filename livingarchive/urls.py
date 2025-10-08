from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.urls import path
from . import views

from search import views as search_views
from user_group_management.views import GroupProfileListView, GroupMembersView, RemoveMemberView

urlpatterns = [
    path("3d/", views.cesium_view, name="cesium_view"),
    path("api/annotations.geojson", views.annotations_geojson),
    path("api/annotations/", views.annotations_post),
    
    path("", include("home.urls")),   # homepage

    path("django-admin/", admin.site.urls),

    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),

    path("group/", GroupProfileListView.as_view(), name="group_list"),
    path("group/<int:group_id>/", GroupMembersView.as_view(), name="group_members"),
    path("group/<int:group_id>/remove_member/<int:user_id>/", RemoveMemberView.as_view(), name="remove_member"),

    path("search/", search_views.search, name="search"),

    path("accounts/", include("allauth.urls")),

    path("cms/", include(wagtail_urls)),  # wagtail site under /cms/
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
