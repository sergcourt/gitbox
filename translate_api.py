pip install --upgrade google-api-python-client

# running Translate API
from googleapiclient.discovery import build
service = build('translate', 'v2', developerKey=APIKEY)

# use the service
inputs = ['is it really this easy?', 'amazing technology', 'wow']
outputs = service.translations().list(source='en', target='it', q=inputs).execute()
# print outputs
for input, output in zip(inputs, outputs['translations']):
  print u"{0} -> {1}".format(input, output['translatedText'])