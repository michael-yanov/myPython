import boto3

regions = [
    'us-east-2',  # US East (Ohio)
    'us-east-1',  # US East (N. Virginia)
    'us-west-1',  # US West (N. California)
    'us-west-2',  # US West (Oregon)
    #'ap-east-1',  # Asia Pacific (Hong Kong)
    'ap-south-1',  # Asia Pacific (Mumbai)
    'ap-northeast-2',  # Asia Pacific (Seoul)
    'ap-southeast-1',  # Asia Pacific (Singapore)
    'ap-southeast-2',  # Asia Pacific (Sydney)
    'ap-northeast-1',  # Asia Pacific (Tokyo)
    'ca-central-1',  # Canada (Central)
    'eu-central-1',  # Europe (Frankfurt)
    'eu-west-1',  # Europe (Ireland)
    'eu-west-2',  # Europe (London)
    'eu-west-3',  # Europe (Paris)
    'eu-north-1',  # Europe (Stockholm)
    #'me-south-1',  # Middle East (Bahrain)
    'sa-east-1'  # South America (São Paulo)
]

for region in regions:
    ec2_console = boto3.resource(service_name='ec2', region_name=region)
    filter_1 = {'Name': 'tag:Group', 'Values': ['production']}
    for ec2 in ec2_console.instances.filter():
        print(ec2.public_ip_address)


