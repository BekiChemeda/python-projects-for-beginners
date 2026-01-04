import json
import os
import random
file_path = os.path.join(os.path.dirname(__file__), "urls.json")
class Link:
    def __init__(self, base_link="http://short.ly/"):
        self.base_link = base_link
        self.chars = ["A","B","C","D","E","F","J","K","L","M"]
        self.link_length = 5
        self.file_checker()
        
    def file_checker(self):
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([],f,indent=4)
        else:
            return True
    
    def is_link(self,link):
        return link.startswith("http://") or link.startswith("https://")
    def check_available(self, link):
        with open(file_path, "r") as f:
            urls = json.load(f)
        for url in urls:
            if url["real_link"] == link:
                return link, url["shortened_link"]
        return False
    def generated_before(self,shortened_link):
        try:
            with open(file_path, "r") as f:
                urls = json.load(f)
            for url in urls:
                if url["shortened_link"] == shortened_link:
                    return url["real_link"]
            return False
        except Exception as e:
            print(e)
    def save(self,link,shortened_link):
        try:
            with open(file_path, "r") as f:
                urls = json.load(f)
            new_url = {
                "real_link": link,
                "shortened_link": shortened_link
            }
            urls.append(new_url)
            with open(file_path,"w") as f:
                json.dump(urls,f,indent=4)
            return True
        except Exception as e:
            print(f"Error while saving as json : {e}")
            return False
    def generate(self, link):
        try:
            short_link = []
            for a in range(self.link_length):
                i = random.randint(0,len(self.chars)-1)
                short_link.append(self.chars[i])
            return link, self.base_link + "".join(short_link)
        except Exception as e:
            print(e)
    def shorten(self, link):
        try:
            if not self.is_link(link):
                raise ValueError("Link should start either with http:// or https://")
            available_link = self.check_available(link)
            if available_link:
                return available_link
            link, generated_link = self.generate(link)
            while self.generated_before(link):
                link, generated_link = self.generate(link)
            self.save(link,generated_link)
            return (link, generated_link)
        except Exception as e:
            print(e)
            

    def list_all(self):
        try:
            with open(file_path, "r") as f:
                urls = json.load(f)
            return urls
        except Exception as e:
            print("Error happened while listing them down")