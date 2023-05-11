
from django.contrib import admin
from django.urls import path
from course.views import home, course, blog, teachers, pricings, contact, blog_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home-page"),
    path('course/', course, name="course-page"),
    path('blog/', blog, name="blog-page"),
    path('teachers/', teachers, name="teachers-page"),
    path('pricing/', pricings, name="pricing-page"),
    path('contact/', contact, name="contact-page"),
    path('blog/single/<int:id>/', blog_detail, name="blog-detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
