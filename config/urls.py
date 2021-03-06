from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views

from modain.users.views import(
     Indice, ListadoProducto, DetalleProducto, ComentarioProducto, 
     Ingresar, Salir, CambiarPerfil, AddCart
)

urlpatterns = [

    path("", Indice.as_view(), name="index"),
    #path("test/", test.as_view()),
    #path("listado_productos/", ListadoProducto.as_view(), name="test_listado"),
    path("listado_productos/", ListadoProducto.as_view(), name="listado_productos"),
    path("detalle_producto/<int:pk>", DetalleProducto.as_view(), name="detalle_productos"),
    path("crear_comentario/", ComentarioProducto.as_view(), name="crear_comentario"),
    path('ingresar/', Ingresar.as_view(), name="ingresar"),
    path('salir/', Salir.as_view(), name="salir"),
    path('cambiar_perfil/', CambiarPerfil.as_view(), name="cambiar_perfil"),
    path('add_cart/', AddCart.as_view(), name="add_cart"),

    # Django Admin, use {% raw %}{% url 'admin:index' %}{% endraw %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("modain.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
