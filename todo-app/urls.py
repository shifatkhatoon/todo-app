from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
# from . import views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('todo-app/', include('todo-app.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/todo-app/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)