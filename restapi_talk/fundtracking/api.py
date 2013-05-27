from tastypie.resources import ModelResource
from restapi_talk.fundtracking.models import FundHouse, Fund, Price, Annotation
from restapi_talk.api import v1_api


class FundHouseResource(ModelResource):
    class Meta:
        queryset = FundHouse.objects.all()
        resource_name = 'fundhouse'
        allowed_methods = ['get']


class FundResource(ModelResource):
    class Meta:
        queryset = Fund.objects.all()
        resource_name = 'fund'
        allowed_methods = ['get']


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
