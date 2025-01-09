# log-processor

This project demonstrates the creation and configuration of an AWS Lambda function and an API Gateway using the AWS Serverless Application Model (SAM) CLI and AWS CLI. The application processes log data to count the number of errors and extract unique error messages.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [API Usage](#api-usage)
- [Code Details](#code-details)
- [SAM Template](#sam-template)
- [File Structure](#file-structure)
- [License](#license)

---

## Overview

The `log-processor` application:
- Receives log data through an API Gateway.
- Processes the log data in the AWS Lambda function.
- Returns the total number of errors and unique error messages in the logs.

---

## Architecture

- **AWS Lambda Function**: Processes the log data and extracts error information.
- **API Gateway**: Exposes an HTTP endpoint to trigger the Lambda function.

---

## Setup Instructions

### Prerequisites

- [AWS CLI](https://aws.amazon.com/cli/) installed and configured.
- [AWS SAM CLI](https://aws.amazon.com/serverless/sam/) installed.
- Python 3.12 installed locally.

### Deployment Steps

1. **Clone the Repository**  
   Clone the repository or copy the files to your local system.

   ```bash
   git clone https://github.com/your-repo/log-processor.git
   cd log-processor
   ```

2. **Install Dependencies**  
   Navigate to the `src/` directory and install required Python packages (if any).

   ```bash
   cd src/
   pip install -r requirements.txt
   ```

3. **Validate the SAM Template**  
   Validate the SAM template file.

   ```bash
   sam validate
   ```

4. **Build the Application**  
   Build the application using the SAM CLI.

   ```bash
   sam build
   ```

5. **Deploy the Application**  
   Deploy the application to AWS.

   ```bash
   sam deploy --guided
   ```

   During deployment, you will be prompted to provide configuration values such as stack name and AWS region.

6. **Test the API**  
   Once deployed, the API Gateway URL will be provided. Use this URL to send a POST request to `/log-data-processor`.

---

## API Usage

### Endpoint

```
POST /log-data-processor
```

### Request Body

```json
{
  "candidate_id": "12345",
  "log_content": "INFO: Process started\nERROR: Missing configuration file\nERROR: Network timeout"
}
```

### Response

#### Success

```json
{
  "data": {
    "candidate_id": "12345",
    "result": {
      "total_errors": 2,
      "unique_error_messages": [
        "Missing configuration file",
        "Network timeout"
      ]
    }
  },
  "message": "Data Fetched Successfully",
  "status_code": 200
}
```

#### Failure

```json
{
  "data": {
    "candidate_id": "12345",
    "result": {
      "total_errors": 0,
      "unique_error_messages": []
    }
  },
  "message": "Logs not found!",
  "status_code": 400
}
```

---

## File Structure

```
log-processor/
│
├── src/
│   ├── app.py           # Lambda function code
│   └── requirements.txt # (Optional) Python dependencies
│
├── template.yaml        # SAM template defining AWS resources
└── README.md            # Project documentation
```

---

## License

This project is licensed under the [MIT License](LICENSE).

