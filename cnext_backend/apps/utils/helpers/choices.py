from tools.models import CasteCategory, DisabilityCategory

CONSUMPTION_TYPE = {"paid": "Paid", "free": "Free"}
PUBLISHING_TYPE = {"published": "Published", "unpublished": "Unpublished"}
TOOL_TYPE = {
    "result_predictor": "Result Predictors",
    "college_predictor": "College Predictors",
    "mba_college_predictor": "MBA College Predictors",
}
TOOL_TYPE_INTEGER = {
    1: "college_predictor",
    2: "mba_college_predictor",
    3: "result_predictor",
}
FIELD_TYPE = {
    1: "Studying In",
    2: "Course Interest for College",
    3: "Stream Interest for Class 11th",
    4: "College Education Stream",
}
QUESTION_STATUS = {
    "Published": "Published",
    "Unpublished": "Unpublished",
    "Deleted": "Deleted",
}

STUDENT_TYPE = {1: "Overall", 2: "Category-wise"}
CASTE_CATEGORY = [
    {"id": caste.get("id"), "value": caste.get("name")}
    for caste in CasteCategory.objects.all().values("id", "name")
]
DISABILITY_CATEGORY = [
    {"id": disability.get("id"), "value": disability.get("name")}
    for disability in DisabilityCategory.objects.all().values("id", "name") #TODO do it using F in django
]
