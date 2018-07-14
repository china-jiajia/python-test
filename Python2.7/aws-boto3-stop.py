#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import boto3
import time

def stop():
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(Filters=[{'Name':'instance-state-name','Value':['running']}])

    for ins in instances:
        ins.stop()

def start():
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(Filters=[{'Name':'instace-state-name','Value':['stopped']}])

    for ins in instances:
        ins.start()

def check():
        ec2 = boto3.resource('ec2')

        for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
                print  status
