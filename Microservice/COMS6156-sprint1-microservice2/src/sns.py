import requests
import json
import boto3


"""
# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
webhook_url = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'
slack_data = {'text': "Sup! We're hacking shit together @HackSussex :spaghetti:"}
response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
"""

AWSAccessKeyId="AKIAY2SPKZA2LGLAP2WK"
AWSSecretKey="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"

class NotificationMiddlewareHandler:
    sns_client = None

    def __init__(self):
        pass

    @classmethod
    def get_sns_client(cls):

        if NotificationMiddlewareHandler.sns_client is None:
            NotificationMiddlewareHandler.sns_client = sns = boto3.client("sns",
                                                                          aws_access_key_id=AWSAccessKeyId,
                                                                          aws_secret_access_key=AWSSecretKey,
                                                                          region_name = "us-east-1"
                                                                          )
        return NotificationMiddlewareHandler.sns_client

    @classmethod
    def get_sns_topics(cls):
        s_client = NotificationMiddlewareHandler.get_sns_client()
        result = response = s_client.list_topics()
        topics = result["Topics"]
        return topics

    @classmethod
    def send_sns_message(cls, sns_topic, message):
        import json
        import boto3

        s_client = NotificationMiddlewareHandler.get_sns_client()
        response = s_client.publish(
            TargetArn=sns_topic,
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'
        )
        print("Publish response = ", json.dumps(response, indent=2))
