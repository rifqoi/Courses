import reports
import os
import datetime
import emails

def parse_text(files):
    fruit_dict = {}
    list_dict = []
    for file in files:
        filename, ext = os.path.splitext(os.path.basename(file))
        with open(file) as f:
            f_list = [line.strip() for line in f.readlines()]
            fruit_dict['name'] = f_list[0]
            fruit_dict['weight'] = f_list[1]
            print(fruit_dict)
            list_dict.append(dict(fruit_dict))
    # print(list_dict)
    return list_dict

def list_directory(path):
    return [os.path.join(path, file) for file in os.listdir(path)]

def fruit_summary(fruit_dict):
    fruit_list = []
    for data in fruit_dict:
        string = f"name: {data['name']}<br/>weight: {data['weight']}"
        fruit_list.append(string)
    return fruit_list


def main():
    files = list_directory('supplier-data/descriptions')
    print(files)
    fruit_dict = parse_text(files)
    fruit_list = fruit_summary(fruit_dict)

    # PDF
    today = datetime.datetime.today()
    today = today.strftime("%B %d, %Y")
    title = "Processed Update on " + today
    paragraph = '<br/><br/>'.join(fruit_list)
    reports.generate("/tmp/processed.pdf", title, paragraph)

    # Email
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    
    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)
    print('Sent')



if __name__ == "__main__":
    main()
