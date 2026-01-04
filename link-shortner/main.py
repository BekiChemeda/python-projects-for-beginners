import time
from Link import Link
link = Link()

text = """
Welcome to link My Link Shortener 
********************************
Follow this Commands to navigate:
    1. Shorten Link
    2. Check Redirect Link
    3. List all Links 
"""

while True:
    print(text)
    command = input("Your command: ").strip()
    if command.isdigit():
        if int(command) == 1:
            input_link = input("Enter Link to shorten: ").strip()
            if link.is_link(input_link):
                print(link.shorten)
                (input_linklink, shortened_link) = link.shorten(input_link)
                print(f"Your Input: {input_link} \n"
                      f"Shortened Link: {shortened_link}")
            else: 
                print("Link should start with http:// or https://")
                continue
        elif int(command) == 2:
            shortened_link = input("Enter Shortened link to check: ").strip()
            normal_link = link.generated_before(shortened_link)
            print(f"Your Input: {shortened_link} \n"
                    f"Normal Link: {normal_link}")
        elif int(command) == 3:
            urls = link.list_all()
            print(f"Number of total shortened links: {len(urls)}")
            time.sleep(2)
            for url in urls:
                print(f"Original Link: {url["real_link"]}")
                print(f"Shortened Link: {url["shortened_link"]}")
                print("*********************************")
                time.sleep(2)