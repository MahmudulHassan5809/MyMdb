from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

import core.urls
import user.urls

from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include(user.urls,namespace='user')),
    path('',include(core.urls,namespace='core')),
    path('',core_views.MovieList.as_view()),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
