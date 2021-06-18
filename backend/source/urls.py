from django.urls import path

from source.views import SourceKindViewSet, SourceViewSet, PriceViewSet, ProvinceViewSet 

url_view_set = {
    'source_kind': SourceKindViewSet,
    'source': SourceViewSet,
    'price': PriceViewSet,
    'province': ProvinceViewSet,
}

url_view = [
    # path('deploy_action/', DeployAction.as_view(), {'method': 'action'}),
    # path('cost/', ProjectCost.as_view())
]