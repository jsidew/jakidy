from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'food.views.index', name='home'),
    url(r'^food/list$', 'food.views.foodlist', name='foodlist'),
    url(r'^food/meals$', 'food.views.meals', name='meals'),
    url(r'^food/save$', 'food.views.save', name='savefood'),
    url(r'^food/savemeal$', 'food.views.savemeal', name='savemeal'),
    url(r'^jakidy[.]manifest', 'food.views.manifest', name='manifest'),
    # url(r'^jakidy/', include('jakidy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
