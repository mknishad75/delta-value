import time
import deltacalculate.getOption as delta
from datetime import datetime
import logging
#import pywhatkit as kit

count = 0

logging.basicConfig(
    level=logging.INFO,  # Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def recall(count, pe, ce,expirydate):
    try:
        while True:
            logging.info("Entred in method -----")
            deltaValue =delta.callEveryMinute(pe,ce,expirydate)  # Run the task
            print("Running -----")
            logging.info("Running -----")
            count = count+1
            # Get the current date and time
            current_datetime = datetime.now()
            current_hour = current_datetime.hour
            current_minute = current_datetime.minute
            current_minuteis = current_minute+2
            print(current_hour, current_minute+2)
            
            # Print the current date and time

            if count == 10 :
              deltaVal = 'Service is Running fine :'
              string_num = str(deltaValue)
              value = deltaVal + string_num
              count =0
              #kit.sendwhatmsg('+919899096249',value, current_hour, current_minuteis)
              print("hey i am ready", count)
            print("Current Date and Time:", current_datetime)
            time.sleep(60)  # Wait for 60 seconds before running again

    except Exception as e:
         logging.info("exception 1-----",e)
         print("exception 1===================================================================================================", e)
         count = count+1
         if count == 10 :
            count =0
            
            #kit.sendwhatmsg('+919899096249','Service has error::', current_hour, current_minuteis)
            print("hey i am ready", count)
         time.sleep(120)
         recall(count,pe,ce,expirydate)


items = [
    {"id": 1, "name": "Item 1", "price": 15.00},
    {"id": 2, "name": "Item 2", "price": 25.00},
    {"id": 3, "name": "Item 3", "price": 35.00}
]


class DeltaValue:

 def __init__(self):
        # Simulating a simple in-memory "database"
        self.items = [
            {"id": 1, "name": "Item 1", "price": 10.0},
            {"id": 2, "name": "Item 2", "price": 20.0},
        ]
 def calling(self,pe,ce,expirydate):
  count = 0
  try:
    print("Task is running...")
    while True:
       
        deltaValue =delta.callEveryMinute(pe,ce,expirydate)
        count = count+1 # Run the task
        print("Running -----")
        logging.info("Running -----")
        # Get the current date and time
        current_datetime = datetime.now()
        current_hour = current_datetime.hour
        current_minute = current_datetime.minute
        current_minuteis = current_minute+2
        print(current_hour, current_minute+2)
        
        # Print the current date and time

        print("Current Date and Time:", current_datetime)
        if count == 10 :
            deltaVal = 'Service is Running fine :'
            string_num = str(deltaValue)
            value = deltaVal + string_num
            count =0
            #kit.sendwhatmsg('+919899096249',value, current_hour, current_minuteis)
            print("hey i am ready", count)
        time.sleep(80)  # Wait for 60 seconds before running again
  except Exception as e:
    
    count = count+1
    if count == 2 :
      count =0
      #kit.sendwhatmsg('+919899096249','Service has error:', current_hour, current_minuteis)
      print("hey i am ready", count)
    logging.info("exception 2 -----", e)
    print("exception 2===================================================================================================", e)
    time.sleep(120)
    recall(count,pe,ce,expirydate)
  return self.e


class CreateToken:
  def token(self,name, userId, token):
        # Open the file in 'write' mode (overwrites any existing content)
      with open('deltacalculate/enctoken.txt', 'w') as file:
       file.write(token)
      with open('deltacalculate/userdetail.txt', 'w') as user: 
       user.write(name)
      with open('deltacalculate/usercode.txt', 'w') as code:  
       code.write(userId)
       
      return 'Sucessfully added' 