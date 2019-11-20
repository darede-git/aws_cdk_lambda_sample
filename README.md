
# Welcome to your CDK Python project!

This is a project for Python development with CDK.

You can use the following step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth --profile <your-local-profile>
```

Bootstrap your environment on AWS. This creates a staging bucket that the AWS 
CDK needs in order to deploy stacks containing assets.

```
$ cdk bootstrap --profile <your-local-profile>
```

Deploy your app:

```
$ cdk deploy --profile <your-local-profile>
```

Testing:

    curl -X POST 'https://GUID.execute-api-REGION.amazonaws.com/prod/example'
    curl -X GET 'https://GUID.execute-api-REGION.amazonaws.com/prod/example'
    curl -X GET 'https://GUID.execute-api-REGION.amazonaws.com/prod/example'
    curl -X DELETE 'https://GUID.execute-api-REGION.amazonaws.com/prod/example'
    curl -X GET 'https://GUID.execute-api-REGION.amazonaws.com/prod'

Destroy everything:

```
$ cdk destroy --profile <your-local-profile>
```

References:

    <https://github.com/aws-samples/aws-cdk-examples>

    <https://docs.aws.amazon.com/cdk/latest/guide/serverless_example.html>

