from tools.models import CPProductCampaign
from rank_predictor.models import RpFormField, RpContentSection, CnextRpCreateInputForm
from wsgiref import validate
from tools.models import CPProductCampaign, CPTopCollege, UrlAlias
from  utils.helpers.choices import HEADER_DISPLAY_PREFERANCE
import os

class RPHelper:

    def __init__(self):
        self.base_image_url = os.getenv("CAREERS_BASE_IMAGES_URL","https://cnextassets.careers360.de/media_tools/")
        pass

    def _get_header_section(self, product_id=None, alias=None):

        if alias != None:
            alias_data = self._get_product_from_alias(alias=alias)
            split_string = alias_data.source.split("/")

            print(split_string[1])

            product_id = int(split_string[1])


        header_data = CPProductCampaign.objects.filter(id=product_id).values("id", "header_section", "custom_exam_name", "custom_flow_type", "custom_year", "video", "usage_count_matrix", "positive_feedback_percentage", "display_preference", "gif", "secondary_image", 'image', 'exam_other_content')
        # print(header_data['result'])

        header_data_list = list(header_data)

        for data in header_data_list:

            removable_fields = {key: value for key, value in HEADER_DISPLAY_PREFERANCE.items() if key != data.get('display_preference')}
            # print(removable_fields)

            for k in removable_fields:
                data.pop(HEADER_DISPLAY_PREFERANCE.get(k), None)

        return header_data
    
    def _get_form_section(self, product_id=None):

        # flow_type_count = RpFormField.objects.filter(product_id=product_id, status=1, mapped_process_type__isnull=False).values('mapped_process_type').distinct().count()

        input_form_mapping = CnextRpCreateInputForm.objects.filter(product_id=product_id).values('input_process_type', 'process_type_toggle_label', 'submit_cta_name')

        input_process_type_mapping = {}
        input_process_type_list = []

        # fetch cta submit button once
        for process_type in input_form_mapping:
            input_process_type_mapping[process_type['input_process_type']] = {
                'process_type_toggle_label': process_type['process_type_toggle_label'],
                'submit_cta_name': process_type['submit_cta_name']
        }
            input_process_type_list.append(input_process_type_mapping)
        
        # print(f"process type mapping {input_process_type_mapping}")
        form_data = RpFormField.objects.filter(product_id=product_id, status=1).values("field_type", "input_flow_type", "display_name", "place_holder_text", "error_message", "weight", "mapped_process_type", "mandatory", "status", 'min_val', 'max_val').order_by('weight')

        with_appended_cta = {'form_data': form_data, 'input_process_type_mapping': input_process_type_mapping }

        return with_appended_cta
    
    def _get_top_colleges(self, exam_id=None):
        """
        Fetch top colleges related to a specific exam ID.
        """
        return CPTopCollege.objects.filter(exam_id=exam_id, status=1).values(
            "id",
            "exam_id",
            "college_id",
            "college_name",
            "college_short_name",
            "college_url",
            "review_count",
            "aggregate_rating",
            "course_id",
            "course_name",
            "course_url",
            "final_cutoff",
            "rank_type",
            "process_type",
            "submenu_data"
        )
    
    def _get_content_section(self, product_id=None):

        """
        Fetch content for the product
        """

        content_response = []

        content_list = RpContentSection.objects.filter(product_id=product_id).values("heading", "content", "image_web", "image_wap")
        
        # print(content_list)

        for content in content_list:
            content['image_web'] = self.base_image_url+content.get('image_web', None)
            content['image_wap'] = self.base_image_url+content.get('image_wap', None)
            content_response.append(content)

        return content_response
    
    def _get_product_from_alias(self , alias):
        source = UrlAlias.objects.filter(alias=alias).first()
        # source_list = list(source)
        
        return source
        
        
        
    # def calculate_percentile(self, score, max_score):
    #     """
    #     Calculate percentile from score
    #     Formula: (score / max_score) * 100
    #     """
    #     try:
    #         percentile = (score / max_score) * 100
    #         return round(percentile, 2)
    #     except ZeroDivisionError:
    #         raise ValueError("max_score cannot be zero.")
    #     except Exception as e:
    #         raise ValueError(f"Error calculating percentile: {str(e)}")

    # def calculate_category_rank(self, percentile, total_candidates, caste=None, disability=None, slot=None, difficulty_level=None, year=None):
    #     """
    #     Calculate the rank based on percentile
    #     Formula: rank = ((100 - percentile) / 100) * total_candidates
    #     """
    #     try:
    #         # Calculate overall rank from percentile
    #         rank = ((100 - percentile) / 100) * total_candidates
    #         rank = int(rank)

    #         # Adjust rank for category-wise considerations if provided (caste, disability, etc.)
    #         category_rank_data = {
    #             "general": rank,  # Default to overall rank for general category
    #             "obc": rank + 200,  # Example adjustment, can be based on actual data
    #             "sc": rank + 400,   # Example adjustment
    #             "st": rank + 600,   # Example adjustment
    #         }

    #         # Can adjust the rank further based on caste, disability, etc.
    #         if caste:
    #             category_rank_data["caste_rank"] = category_rank_data.get(caste.lower(), rank)
    #         if disability:
    #             category_rank_data["disability_rank"] = category_rank_data.get(disability.lower(), rank)
    #         if slot:
    #             category_rank_data["slot_rank"] = category_rank_data.get(slot.lower(), rank)
    #         if difficulty_level:
    #             category_rank_data["difficulty_level_rank"] = category_rank_data.get(difficulty_level.lower(), rank)
    #         if year:
    #             category_rank_data["year_rank"] = category_rank_data.get(year, rank)

    #         # Return rank and category-specific ranks
    #         return {
    #             "rank": rank,
    #             "category_rank": category_rank_data
    #         }

    #     except Exception as e:
    #         raise ValueError(f"Error calculating rank: {str(e)}")
