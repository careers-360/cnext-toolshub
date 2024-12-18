from rest_framework.views import APIView
from rest_framework.response import Response
from utils.helpers.response import SuccessResponse, CustomErrorResponse
from utils.helpers.custom_permission import ApiKeyPermission
from rest_framework import status
from .helpers import RPCmsHelper, CommonDropDownHelper


class FlowTypeAPI(APIView):

    """
    API for Flow Type CMS Pannel
    Endpoint : api/<int:version>/cms/rp/flow-type
    Params : product_id
    """

    permission_classes = [ApiKeyPermission]

    def get(self, request, version, **kwargs):
        # Fetch flow master data from database and return it to client.
        cms_helper = RPCmsHelper()
        data = cms_helper._get_flow_types(**request.GET)
        return SuccessResponse(data, status=status.HTTP_200_OK)
    
    def post(self, request, version):
        # Add new flow master data to database.
        # This method will be implemented in future.

        flow_type = request.data.get('flow_type')
        if not flow_type:
            return CustomErrorResponse("Missing required parameters", status=status.HTTP_400_BAD_REQUEST)
        
        cms_helper = RPCmsHelper()
        resp, msg = cms_helper._add_flow_type(**request.data)
        if not resp:
            return CustomErrorResponse(msg, status=status.HTTP_400_BAD_REQUEST)
        else:
            return SuccessResponse({"message": msg}, status=status.HTTP_201_CREATED)
        
    def delete(self, request, version):
        # Add new flow master data to database.
        # This method will be implemented in future.

        flow_type = request.data.get('flow_type')
        if not flow_type:
            return CustomErrorResponse("Missing required parameters", status=status.HTTP_400_BAD_REQUEST)
        
        cms_helper = RPCmsHelper()
        resp, msg = cms_helper._delete_flow_type(**request.data)
        if not resp:
            return CustomErrorResponse(msg, status=status.HTTP_400_BAD_REQUEST)
        else:
            return SuccessResponse({"message": msg}, status=status.HTTP_204_NO_CONTENT)


class ExamSessiondAPI(APIView):
    """
    API for exam session CMS Pannel
    Endpoint : api/<int:version>/cms/rp/exam-session
    Params : product_id, year
    """

    permission_classes = [ApiKeyPermission]

    def get(self, request, version, **kwargs):
        uid = request.GET.get('uid')
        product_id = request.GET.get('product_id')
        year = request.GET.get('year')
        if not product_id or not uid or not product_id.isdigit() or not uid.isdigit():
            return CustomErrorResponse({"message": "product_id, uid are required and should be a integer value"}, status=status.HTTP_400_BAD_REQUEST)
        
        if year and not str(year).isdigit():
            return CustomErrorResponse({"message": "year should be a integer value"}, status=status.HTTP_400_BAD_REQUEST)
        
        product_id = int(product_id)
        # Fetch exam session data from database and return it to client.
        cms_helper = RPCmsHelper()
        resp, data = cms_helper._get_exam_session_data(product_id=product_id, year=year)
        if resp:
            return SuccessResponse(data, status=status.HTTP_200_OK)
        else:
            return CustomErrorResponse(data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, version):
        uid = request.data.get('uid')
        product_id = request.data.get('product_id')
        year = request.data.get('year')
        session_data = request.data.get('session_data')

        if not product_id or not uid or not str(product_id).isdigit() or not str(uid).isdigit():
            return CustomErrorResponse({"message": "product_id, uid are required and should be a integer value"}, status=status.HTTP_400_BAD_REQUEST)
        
        if year and not str(year).isdigit():
            return CustomErrorResponse({"message": "year should be a integer value"}, status=status.HTTP_400_BAD_REQUEST)

        product_id = int(product_id)
        # add exam session data in database.
        cms_helper = RPCmsHelper()
        resp, data = cms_helper._add_exam_session_data(uid=uid, session_data=session_data, product_id=product_id, year=year)
        if resp:
            return SuccessResponse(data, status=status.HTTP_201_CREATED)
        else:
            return CustomErrorResponse(data, status=status.HTTP_400_BAD_REQUEST)


class CommonDropDownAPI(APIView):

    """
    API for Common Dropdown CMS Pannel
    Endpoint : api/<int:version>/cms/rp/common-dropdown
    Params : product_id, type
    """

    def get(self, request, version, **kwargs):
        field_name = request.GET.get('field_name')
        selected_id = request.GET.get('selected_id')

        if not field_name:
            return CustomErrorResponse({"message": "field_name is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if selected_id:
            if not str(selected_id).isdigit():
                return CustomErrorResponse({"message": "selected_id should be a integer value"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                selected_id = int(selected_id)
    
        # Fetch common dropdown data from database and return it to client.
        cms_helper = CommonDropDownHelper()
        resp = cms_helper._get_dropdown_list(field_name=field_name, selected_id=selected_id)
        return SuccessResponse(resp, status=status.HTTP_200_OK)
    

class VariationFactorAPI(APIView):
    """
    API for variation factor CMS Pannel
    Endpoint : api/<int:version>/cms/rp/exam-session
    Params : product_id
    """

    permission_classes = [ApiKeyPermission]

    def get(self, request, version, **kwargs):
        uid = request.GET.get('uid')
        product_id = request.GET.get('product_id')

        if not uid or not product_id or not uid.isdigit() or not product_id.isdigit():
            return CustomErrorResponse({"message": "uid, product_id are required and should be a integer value"}, status=status.HTTP_400_BAD_REQUEST)

        product_id = int(product_id)
        # Fetch variation factor data from database and return it to client.
        cms_helper = RPCmsHelper()
        resp, data = cms_helper._get_variation_factor_data(product_id=product_id)
        if resp:
            return SuccessResponse(data, status=status.HTTP_200_OK)
        else:
            return CustomErrorResponse(data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, version):
        uid = request.data.get('uid')
        product_id = request.data.get('product_id')
        variation_factor_data = request.data.get('variation_factor_data')

        if not uid or not product_id or not str(uid).isdigit() or not str(product_id).isdigit():
            return CustomErrorResponse({"message": "product_id, uid are required and should be a integer value"}, status=status.HTTP_400_BAD_REQUEST)

        product_id = int(product_id)
        # add variation factor data in database.
        cms_helper = RPCmsHelper()
        resp, data = cms_helper._add_variation_factor_data(uid=uid, var_factor_data=variation_factor_data, product_id=product_id)
        if resp:
            return SuccessResponse(data, status=status.HTTP_201_CREATED)
        else:
            return CustomErrorResponse(data, status=status.HTTP_400_BAD_REQUEST)
        

class CustomMeanSD(APIView):
    """
    API for Custom Mean/SD CMS Pannel
    Endpoint : api/<int:version>/cms/rp/custom-mean-sd
    Params : product_id, year
    """

    permission_classes = [ApiKeyPermission]

    def get(self, request, version, **kwargs):
        uid = request.GET.get('uid')
        product_id = request.GET.get('product_id')
        year = request.GET.get('year')

        if not product_id or not uid or not product_id.isdigit() or not uid.isdigit():
            return CustomErrorResponse({"message": "product_id, uid are required and should be a integer value"}, status=status.HTTP_400_BAD_REQUEST)
        
        if year and not str(year).isdigit():
            return CustomErrorResponse({"message": "year should be a integer value"}, status=status.HTTP_400_BAD_REQUEST)
        
        product_id = int(product_id)
        # Fetch custom mean, SD from database and return it to client.
        cms_helper = RPCmsHelper()
        resp, data = cms_helper._get_custom_mean_sd_data(product_id=product_id, year=year)
        if resp:
            return SuccessResponse(data, status=status.HTTP_200_OK)
        else:
            return CustomErrorResponse(data, status=status.HTTP_400_BAD_REQUEST)