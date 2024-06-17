from rest_framework.response import Response
from rest_framework.views import APIView

from common.tasks.dump_data_to_csv import dump_data_to_csv
from fml_api.authentication import APIKeyAuthentication


class DataDumpAPI(APIView):
    authentication_classes = [APIKeyAuthentication]

    def post(self, request):
        """Dumps models data to a file in a background task."""
        dump_data_to_csv.delay()
        return Response({"status": "success", "message": "Data dumped in progress."})
