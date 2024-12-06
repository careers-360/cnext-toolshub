from rest_framework.views import APIView
from utils.helpers.response import SuccessResponse,ErrorResponse
from utils.helpers.custom_permission import ApiKeyPermission
from rest_framework import status

from tools.helpers.helpers import ToolsHelper
from tools.models import CPProductCampaign, Domain
from utils.helpers.choices import TOOL_TYPE, CONSUMPTION_TYPE, PUBLISHING_TYPE


class HealthCheck(APIView):

    def get(self, request):
        return SuccessResponse({"message": "Tools App runnning"}, status=status.HTTP_200_OK)
    
class CMSToolsFilterAPI(APIView):
    """
    Pending
    """

    permission_classes = (ApiKeyPermission,)

    def get(self, request, version, format=None, **kwargs):

        try:
            result = dict()
            tools_name = list(CPProductCampaign.objects.values('id', 'name'))
            domain = list(Domain.objects.filter(is_stream = 1).values('id','name'))

            # Construct the response payload
            result = {
                'tool_type': TOOL_TYPE,
                'consumption_type': CONSUMPTION_TYPE,
                'published_status_web_wap': PUBLISHING_TYPE,
                'published_status_app': PUBLISHING_TYPE,
                'domain': domain,
                'tools_name': tools_name,
            }
            return SuccessResponse(result,status=status.HTTP_200_OK)

        except Exception as e:
            return ErrorResponse("An unexpected error occurred.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ManagePredictorToolAPI(APIView):
    """
    Predictor List API
    Endpoint -> api/<int:version>/cms/manage-tool/list
    version -> v1 required
    GET API ->api/1/cms/manage-tool/list
    """
    permission_classes = (ApiKeyPermission,)

    def get(self, request, version, format=None, **kwargs):
        try:
            helper = ToolsHelper(request=request)
            filter_value = helper.get_manage_predictor_tools_filter()
            data = helper.get_predictor_tool_list(filter_value)
            return SuccessResponse(data, status=status.HTTP_200_OK)

        except Exception as e:
            return ErrorResponse(e.__str__(), status=status.HTTP_400_BAD_REQUEST)