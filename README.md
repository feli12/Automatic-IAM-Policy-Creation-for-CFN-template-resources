# Automatic-IAM-Policy-Creation-for-CFN-template-resources

# Overview

1.The proposed work is built to assist PS engineers and users who find it difficult to attach IAM Policies to a CFN Template. 
2.It reduces the effort of the users who manually write the policies. 
3.The non-root users who don’t have the required permission to create those resources will be automatically given those permissions.


# Design of the Solution:

1. Uploading the can template to S3 (Manual process to be completed by the user.)
2. Extracting the JSON dumps of the can template using Lambda function.
3. Extracting the individual resources from the template.
4. Using boto3 to create IAM policies for each and every resource.
5. Attaching them to the user who is executing the template. 
6. Finally, putting a S3 put-object trigger for the lambda function.

# Scope of Growth:

Right now, we are planting ‘FullAccess’ to all the custom policies. Moving forward we can customize the policies even more to actually have granular permissions and follow the concept of ‘least privilege’.
