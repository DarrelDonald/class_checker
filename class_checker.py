from lxml import html
import requests
from notify_run import Notify
import sys
import time

notify = Notify()

test = open("test.txt", "w")
test.write("im working")

print(sys.argv[1])

while True:
    page = requests.get('https://coursebook.utdallas.edu/'
                        '' + sys.argv[1].split()[0].lower() + '/'
                        '' + sys.argv[1].split()[1] + '/term_19f?')
    tree = html.fromstring(page.content)

    status = tree.xpath('//*[@id="r-1"]/td[1]/span')
    course = tree.xpath('//*[@id="r-1"]/td[2]/a')

    for i in range(len(status)):
        status[i] = status[i].text_content()
    for i in range(len(course)):
        course[i] = course[i].text_content()

    print('status: ', status)
    print('course: ', course)

    for i in range(len(status)):
        if status[i] == 'Closed':
            if course[i][:course[i].find('.')] == sys.argv[1]:
                notify.send('available')
    time.sleep(300)
