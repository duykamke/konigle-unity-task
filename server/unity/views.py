from rest_framework import pagination, views
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

class PostLimitOffsetPagination(
    pagination.PageNumberPagination, 
    pagination.LimitOffsetPagination
):

    def get_paginated_response(self, data):
        return Response({
            'metadata': {
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'total_count': self.page.paginator.count,
            },
            'results': data
        })

class UserListAPIView(ListAPIView):
    serializer_class=UserSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()

        pagination.PageNumberPagination.page_size = self.request.GET.get('page_size', 10)
        pagination.PageNumberPagination.page = self.request.GET.get('page', 1)

        return queryset_list.order_by('created_at')


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserCountAPIView(views.APIView):

    def get(self, *args, **kwargs):
        queryset_count = User.objects.filter()
        from_date = self.request.GET.get('from_date', None)
        to_date = self.request.GET.get('to_date', None)

        if from_date is not None and to_date is not None:
            queryset_count = queryset_count.filter(created_at__range=(from_date, to_date))
        if from_date is not None and to_date is None:
            queryset_count = queryset_count.filter(created_at__gte=(from_date))
        if to_date is not None and from_date is None:
            queryset_count = queryset_count.filter(created_at__lte=(to_date))

        subscription_status = self.request.GET.get('subscription_status', 1)
        queryset_count = queryset_count.filter(subscription_status=subscription_status)

        count = queryset_count.count()

        return Response({"count": count})