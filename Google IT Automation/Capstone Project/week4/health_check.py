import os
import sys 
import psutil
import emails
import shutil
import socket

def generate_error(subject, body):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    
    message = emails.generate_report_error(sender, receiver, subject, body)
    emails.send(message)


def check_cpu():
    if psutil.cpu_percent() > 8:
        subject = "Error - CPU usage is over 80%"
        body = "Please check your system and resolve the issue as soon as possible."
        generate_error(subject, body)

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == "127.0.0.1":
        return True
    else:
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        body = "Please check your system and resolve the issue as soon as possible."
        generate_error(subject, body)

def check_disk_usage():
    min_disk_percentage = 20
    disk_usage_perc = psutil.disk_usage("/").percent

    if disk_usage_perc< min_disk_percentage:
        subject = "Error - Available disk space is less than 20%"
        body = "Please check your system and resolve the issue as soon as possible."
        generate_error(subject,body)

def check_memory_usage():
    max_memory = 500
    one_mb = 2 ** 20
    max_mem_avail = one_mb * max_memory
    mem_avail = psutil.virtual_memory().available
    if mem_avail < max_mem_avail:
        subject = "Error - Available memory is less than 500MB"
        body = "Please check your system and resolve the issue as soon as possible."
        generate_error(subject, body)

def main():
    check_cpu()
    check_disk_usage()
    check_localhost()
    check_memory_usage()

main()
