import json, os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": "https://europa.eu/eurobarometer/api/deliverable/download/file?deliverableId=46056"
    },
    include_image_base64=False
)

response_dict = json.loads(ocr_response.model_dump_json())
json_string = json.dumps(response_dict, indent=4)
print(json_string)
