from django.urls import path
from rank_predictor.api import controllers as rp_controller



urlpatterns = [
    path("rank-predictor", rp_controller.HealthCheck.as_view(), name='rank_predictor_health_check'),
    path("api/<int:version>/rank-predictor/content-section", rp_controller.ContentSectionAPI.as_view(), name='content_section'),
    path("api/<int:version>/rank-predictor/faq-section", rp_controller.FAQSectionAPI.as_view(), name='faq_section'),
    path("api/<int:version>/rank-predictor/feedback-section", rp_controller.ReviewSectionAPI.as_view(), name='feedback_section'),
    path("api/<int:version>/rank-predictor/top-college", rp_controller.TopCollegesSectionAPI.as_view(), name='top_college'),
    path("api/<int:version>/rank-predictor/header-section", rp_controller.HeaderSectionAPI.as_view(), name='header_section'),
    path("api/<int:version>/rank-predictor/form-section", rp_controller.FormSectionAPI.as_view(), name='form_section'),
    path("api/<int:version>/rank-predictor/top-colleges", rp_controller.TopCollegesAPI.as_view(), name='top_colleges_api'),
    # path(
    #     "api/<int:version>/rank-predictor/rank-calculation",
    #     rp_controller.RankCalculatorAPI.as_view(),
    #     name="rank_calculation",
    # ),
]