#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import  boto3

'''
注释:
    boto3封装了,调用AWS平台上云服务器的API接口可以通过使用boto3来完成.AWS平台上云服务器的一些管理工作
'''


'''
#创建EC2实例连接
ec2 = boto3.resource('ec2_name')
'''

'''
#创建新实例
ec2 = boto3.resource('ec2')
ec2.create_instances(ImageId='<ami-image-id>',MinCount=1,MaxCount=5)
'''


'''

#停止实例
ids = ['instance-id-1','instance-id-2']

#停止服务器
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds=ids).stop()

#终止服务器
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds=ids).terminate()

'''

'''
#检索运行EC2云主机
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    print(instance.id, instance.instance_type)
'''


'''
#checkEC2机器的运行状态
ec2 = boto3.resource('ec2')
for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    print (status)
'''


'''
ec2 = boto3.resource('ec2')

for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
        value_list = list(status.values())
        InstancId = value_list[0]
        if InstancId == 'i-018b002d560b81b94':
                break;
print (value_list)
'''

'''
ec2 = boto3.resource('ec2')

for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
        value_list = list(status.values())
        InstancId = value_list[0]
        if InstancId == 'i-018b002d560b81b94':
                break;
print (value_list)
'''

'''
ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
        if instance.id == 'i-01d871d649b0101ad':
                break;
print instance.id,instance.state
'''

'''
ec2 = boto3.client('ec2')
InstanceId = 'i-01d871d649b0101ad'

def ec2_start():
    response = ec2.start_instances(
        InstanceIds=[InstanceId]
    )
'''

'''
ec2 = boto3.client('ec2')
InstanceId = 'i-01d871d649b0101ad'

def ec2_start():
    response = ec2.stop_instances(
        InstanceIds=[InstanceId]
    )
'''
