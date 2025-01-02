from django.urls import path
from rank_predictor.api import cms_controllers as cms_controller


urlpatterns = [
    path("api/<int:version>/cms/rp/flow-type", cms_controller.FlowTypeAPI.as_view(),  name='flow_type'),
    path("api/<int:version>/cms/rp/exam-session", cms_controller.ExamSessiondAPI.as_view(),  name='student_appeared'),
    path("api/<int:version>/cms/rp/appeared-student", cms_controller.RPAppearedStudentsAPI.as_view(), name='student_appeared'),
    path("api/<int:version>/cms/rp/create-form", cms_controller.CreateForm.as_view(),  name='create_form'),

    path("api/<int:version>/cms/rp/common-dropdown", cms_controller.CommonDropDownAPI.as_view(),  name='common_dropdown'),
    path("api/<int:version>/cms/rp/variation-factor", cms_controller.VariationFactorAPI.as_view(),  name='variation_factor'),
    path("api/<int:version>/cms/rp/custom-mean-sd", cms_controller.CustomMeanSD.as_view(),  name='custom_mean_sd'),
    path("api/<int:version>/cms/rp/create-input-form", cms_controller.CreateInputForm.as_view(),  name='create_input_form'),
    path("api/<int:version>/cms/rp/input-form-list", cms_controller.InputFormList.as_view(),  name='input_form_list'),
    path("api/<int:version>/cms/rp/merit-list-validation-check", cms_controller.MeritListValidationCheck.as_view(),  name='merit_list_validation'),
    path("api/<int:version>/cms/rp/upload-merit-list", cms_controller.UploadMeritList.as_view(),  name='upload_merit_list'),
    path("api/<int:version>/cms/rp/merit-list", cms_controller.MeritListView.as_view(),  name='merit_list_view'),
]