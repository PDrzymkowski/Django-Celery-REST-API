from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class SmallPagesPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "limit"

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "total": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "data": data,
            }
        )


class MediumPagesPagination(SmallPagesPagination):
    page_size = 50


class BigPagesPagination(SmallPagesPagination):
    page_size = 200
