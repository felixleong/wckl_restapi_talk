from django.conf.urls.defaults import url
from extendedmodelresource import ExtendedModelResource
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.utils import trailing_slash
from restapi_talk.fundtracking.models import FundHouse, Fund, Price, Annotation
from restapi_talk.api import v1_api


class FundHouseResource(ExtendedModelResource):
    class Meta:
        queryset = FundHouse.objects.all()
        resource_name = 'fundhouse'
        allowed_methods = ['get']

    class Nested:
        fund = fields.ToManyField(
            'restapi_talk.fundtracking.api.FundResource', 'fund_set')


class FundResource(ExtendedModelResource):
    fund_house = fields.ForeignKey(FundHouseResource, 'fund_house')

    class Meta:
        queryset = Fund.objects.all()
        resource_name = 'fund'
        allowed_methods = ['get']
        detail_uri_name = 'code'
        filtering = {
            'fund_house': ['exact', 'in', ],
        }

    class Nested:
        price = fields.ToManyField(
            'restapi_talk.fundtracking.api.PriceResource', 'price_set')

    def prepend_urls(self):
        return [
            url(
                r"^(?P<resource_name>%s)/(?P<pk>\d+)%s$" % (
                    self._meta.resource_name, trailing_slash()),
                self.wrap_view('dispatch_detail'),
                name="api_dispatch_detail_pk"),
        ]

    def override_urls(self):
        #NOTE: DEPRECATED - implemented as extendedmodelresource 0.22 is still
        #      not updated to use prepend_urls
        return self.prepend_urls()


class PriceResource(ExtendedModelResource):
    fund = fields.ForeignKey(FundResource, 'fund', full=True)
    annotation = fields.ToManyField(
        'restapi_talk.fundtracking.api.AnnotationResource', 'annotation_set')

    class Meta:
        queryset = Price.objects.all()
        resource_name = 'price'
        allowed_methods = ['get']
        filtering = {
            'fund': ['exact', 'in'],
            'date': ['exact', 'lte', 'lt', 'gte', 'gt'],
            'nav': ['exact', 'lte', 'lt', 'gte', 'gt'],
        }

    class Nested:
        annotation = fields.ToManyField(
            'restapi_talk.fundtracking.api.AnnotationResource',
            'annotation_set')


class AnnotationResource(ExtendedModelResource):
    price = fields.ForeignKey(PriceResource, 'price')

    class Meta:
        queryset = Annotation.objects.all()
        resource_name = 'annotation'
        #NOTE: BEWARE! Authorization() is a no-op, no permission checked option
        #      and is only used because it's demo code. Should NEVER be used
        #      in any sort of production code.
        authorization = Authorization()


#NOTE: This is bad practice -- i.e. to have dupe resources in the same API
#      namespace. Am only doing it to illustrate the authentication example.
class NeedAuthFundHouseResource(FundHouseResource):
    class Meta(FundHouseResource.Meta):
        resource_name = 'fundhouse_needauth'
        authentication = BasicAuthentication()


# Register the endpoint
v1_api.register(FundHouseResource())
v1_api.register(FundResource())
v1_api.register(PriceResource())
v1_api.register(AnnotationResource())
v1_api.register(NeedAuthFundHouseResource())
