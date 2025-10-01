from django.conf import settings
from django.contrib import admin
from django.urls import include, path

# Wagtail imports
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

# Other apps
from search import views as search_views
from user_group_management.views import (
    GroupProfileListView,
    GroupMembersView,
    RemoveMemberView,
)

urlpatterns = [
    # Django + Wagtail admin
    path('django-admin/', admin.site.urls),        # Django admin
    path('admin/', include(wagtailadmin_urls)),   # Wagtail admin

    # Home app (your custom pages)
    path('', include('home.urls')),

    # Group management
    path('group/', GroupProfileListView.as_view(), name='group_list'),
    path('group/<int:group_id>/', GroupMembersView.as_view(), name='group_members'),
    path(
        'group/<int:group_id>/remove_member/<int:user_id>/',
        RemoveMemberView.as_view(),
        name='remove_member'
    ),

    # Documents + Search
    path('documents/', include(wagtaildocs_urls)),
    path('search/', search_views.search, name='search'),

    # Auth + wagtail (keep these last so they don’t override your home app)
    path('', include('allauth.urls')),
    path('', include(wagtail_urls)),
]

# Static + media (development only)
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
