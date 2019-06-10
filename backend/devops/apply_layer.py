# -*- coding: utf-8 -*-

"""
Layer can't automatically attached by serverless command line

- https://forum.serverless.com/t/lambda-layer-not-attaching-to-function/6884/3
- https://forum.serverless.com/t/layers-upload-on-each-deploy/6634/3

- boto3 lambda reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html
"""

import boto3
from picage import Package

session = boto3.session.Session(profile_name="eqtest")
lbd = session.client("lambda")
api = session.client("apigateway")

service_name_slug = "sls-forum"
package_name = "sls_forum"
stage = "dev"
layer = "arn:aws:lambda:us-east-1:224233068863:layer:sls_forum:2"

# update VPC, Security Group, and Layer
for submodule in Package("sls_forum.handlers").sub_modules:
    if "__init__" not in submodule:
        func_name = f"{service_name_slug}-{stage}-{submodule}"
        print("update %s ..." % func_name)
        try:
            response = lbd.get_function(FunctionName=func_name)
            lbd.update_function_configuration(
                FunctionName=func_name,
                Layers=[layer, ]
            )
            print("  success!")
        except Exception as e:
            print("  failed! %s" % e)
