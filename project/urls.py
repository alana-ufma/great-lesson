from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include(('core.urls', 'pages'), namespace='core')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('recursos/', include(('recurso.urls', 'recurso'), namespace='recurso')),
    path('aulas/', include(('aula.urls', 'aula'), namespace='aula')),
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
