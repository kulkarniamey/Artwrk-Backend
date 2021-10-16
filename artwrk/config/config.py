import logging
import json

LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="Logger.log",level=logging.WARNING,format=LOG_FORMAT)
#filemode='w' in the brackets above      for deleting previous logs 

with open('artwrk/config/config.json') as f:
  data = json.load(f)

logger=logging.getLogger()
AWS_ACCESS_KEY_ID = data["aws_access_key_id"]
AWS_SECRET_ACCESS_KEY = data["aws_secret_access_key"]
TABLE_NAME = data["table_name"]
AWS_REGION = data["region"]
DYNAMODB_HOST = data["host"]