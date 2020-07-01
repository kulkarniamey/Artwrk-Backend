import logging

LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="Logger.log",level=logging.WARNING,format=LOG_FORMAT)
#filemode='w' in the brackets above      for deleting previous logs 

logger=logging.getLogger()
email="alumnijnec@gmail.com"
password="Jnec12345"
smtp_host="smtp.gmail.com"