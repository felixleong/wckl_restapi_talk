from django.conf.urls.defaults import url
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash
from restapi_talk.fundtracking.models import FundHouse, Fund, Price, Annotation
from restapi_talk.api import v1_api


class FundHouseResource(ModelResource):
    class Meta:
        queryset = FundHouse.objects.all()
        resource_name = 'fundhouse'
        allowed_methods = ['get']


class FundResource(ModelResource):
    fund_house = fields.ForeignKey(FundHouseResource, 'fund_house')

    class Meta:
        queryset = Fund.objects.all()
        resource_name = 'fund'
        allowed_methods = ['get']
        detail_uri_name = 'code'
        filtering = {
            'fund_house': ['exact', 'in', ],
        }

    def prepend_urls(self):
        return [
            url(
                r"^(?P<resource_name>%s)/(?P<pk>\d+)%s$" % (
                    self._meta.resource_name, trailing_slash()),
                self.wrap_view('dispatch_detail'),
                name="api_dispatch_detail_pk"),
        ]


class PriceResource(ModelResource):
    class Meta:
        queryset = Price.objects.all()
        resource_name = 'price'
        allowed_methods = ['get']


class AnnotationResource(ModelResource):
    class Meta:
        queryset = Annotation.objects.all()
        resource_name = 'annotation'


# Register the endpoint
v1_api.register(FundHouseResource())
v1_api.register(FundResource())
v1_api.register(PriceResource())
