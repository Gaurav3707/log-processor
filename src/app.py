import json, re
import logging 

logger = logging.getLogger()
logger.setLevel(logging.INFO) 


def lambda_handler(event, context):
    """
    Lambda function to process log data and count the total number of errors
    and extract unique error messages.

    Args:
    event (dict): The event data passed by the API Gateway or invoking service.
    context (object): Runtime information of the Lambda function.

    Returns:
    dict: A response with error details and metadata.
    """

    total_errors = 0
    unique_error_messages = []
    if 'body' in event:
        request_data = json.loads(event.get('body', '{}'))
        logger.info("Request data parsed from body.")

    else:
        request_data = event
        logger.info("Request data parsed from body.")

    log_data = request_data.get('log_content', '')
    candidate_id = request_data.get('candidate_id', None)

    if not log_data:
        logger.error("No log content found in the request.")
        return {
        "statusCode": 400,
        "body": json.dumps({
        "data":{
            "candidate_id":candidate_id,
            "result":{
                "total_errors": total_errors,
                "unique_error_messages": unique_error_messages
            }
            
        },
        "message":"Logs not found!",
        "status_code":400
    })
    }
    
    for line in log_data.splitlines():
        if re.search(r'ERROR', line, re.IGNORECASE):
            total_errors += 1
            error_string = line.split('ERROR:')[-1].strip()
            if error_string not in unique_error_messages:
                unique_error_messages.append(error_string)

    logger.info(f"Processing completed: {total_errors} errors found.")
    

    return {
        "statusCode": 200,
        "body": json.dumps({
        "data":{
            "candidate_id":candidate_id,
            "result":{
                "total_errors": total_errors,
                "unique_error_messages": unique_error_messages
            }
            
        },
        "message":"Data Fetched Successfully",
        "status_code":200
    })
    }
