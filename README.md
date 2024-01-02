# VCard-CSV Converter Lambda Function

## **Overview**

This Python-based AWS Lambda function facilitates the conversion between VCard and CSV formats. Users can upload either a VCard file to convert it into CSV format, or a CSV file to convert it into VCard format. The conversion logic respects the standard structure of both file types to ensure compatibility and correctness.

## **Example**

## **Features**

- **Bidirectional Conversion:** Supports conversion from VCard to CSV and vice versa.
- **File Upload Interface:** Uses AWS API Gateway to provide a file upload interface.
- **Data Integrity:** Maintains the integrity and structure of the data during conversion.

## **Requirements**

- Python >= 3.9
- AWS Lambda for hosting and executing the function.
- AWS API Gateway for creating an HTTP interface.
- The 'serverless' framework for deployment and offline debugging.

## **Local Development and Debugging**

- **Serverless Offline:** Configured for local development and debugging using **`serverless-offline`**. This simulates the AWS Lambda and API Gateway environment on your local machine.

## **Deployment**

- **Deploy to Production:** Deploy the application to a production environment with **`serverless deploy --stage prod`**.

## **Functionality**

### **`convert_vcard_to_csv(vcard_file)`**

Converts a VCard file into CSV format.

### **Parameters**

- **`vcard_file`** (file): The VCard file to be converted.

### **`convert_csv_to_vcard(csv_file)`**

Converts a CSV file into VCard format.

### **Parameters**

- **`csv_file`** (file): The CSV file to be converted.

### **`lambda_handler(event, context)`**

Lambda function handler. Processes file uploads and triggers the appropriate conversion function.

### **Parameters**

- **`event`** (dict): Contains the request details and parameters, including the uploaded file.
- **`context`**: AWS Lambda context object (not used in this function).

## **Example Usage**

- Deploy the Lambda function and API Gateway.
- Upload a VCard or CSV file to the provided endpoint, e.g., **`https://your-lambda-api.com/upload`**.
- The function will process the file and return the converted file in the corresponding format.