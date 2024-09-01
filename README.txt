# Serverless-Web-Hosting
Hosting a website using Amazon S3, CloudFront, API Gateway, Lambda (Python 3.9), and DynamoDB.

Step 1: Create an S3 Bucket for Static Website Hosting
        => Create S3 Bucket:
           -> Go to the S3 console and create a new bucket.
           -> Enable static website hosting in the bucket properties.
           -> Upload your HTML, CSS, and JS files to the bucket.
        => Set Bucket Policy:
           -> Make the bucket content publicly accessible by setting the appropriate bucket policy.

Step 2: Create CloudFront Distribution
        => Create CloudFront Distribution:
           -> Go to the CloudFront console and create a new distribution.
           -> Set the S3 bucket as the origin.
           -> Configure the distribution settings (e.g., caching, SSL).

Step 3: Create API Gateway
        => Create API Gateway:
           -> Go to the API Gateway console and create a new REST API.
           -> Create a new resource and method (e.g., POST) for handling form submissions.

Step 4: Create Lambda Function
        => Create Lambda Function:
           -> Go to the Lambda console and create a new function with Python 3.9 runtime.(Copy-paste function given in Lambda.py)
           -> Write the Lambda function code to process the form data and store it in DynamoDB.
        => Set Permissions:
           -> Attach the necessary IAM role to the Lambda function to allow it to write to DynamoDB.

Step 5: Integrate API Gateway with Lambda
        => Set Integration:
           -> In the API Gateway console, set the integration type of your method to Lambda Function.
           -> Select the Lambda function you created.
        => Deploy API:
           -> Deploy the API to a stage (e.g., prod).

Step 6: Update CloudFront Distribution
        => Add API Gateway as Origin:
           -> Add the API Gateway endpoint as a new origin in your CloudFront distribution.
           -> Set up path patterns to route API requests to the API Gateway and static content requests to the S3 bucket.

Step 7: Test Your Setup
        => Test the Website:
           -> Access your CloudFront distribution URL.
           -> Ensure that static content is served correctly and form submissions are processed by the Lambda function and stored in DynamoDB.

## This setup will allow you to host a static website on S3, use CloudFront for CDN, API Gateway to handle API requests, Lambda for serverless backend processing, and DynamoDB for data storage. ##




