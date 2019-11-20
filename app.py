#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_api_sample.aws_cdk_api_sample_stack import AwsCdkApiSampleStack


env = core.Environment(region="us-east-1")

app = core.App()
AwsCdkApiSampleStack(app, "aws-cdk-api-sample", env=env)

app.synth()
