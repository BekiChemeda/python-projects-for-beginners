import json
import os
import random
import logging

file_path = os.path.join(os.path.dirname(__file__), "urls.json")
logger_path = os.path.join(os.path.dirname(__file__), "link.log")
logger = logging.getLogger(__name__)
logging.basicConfig(filename=logger_path,encoding="utf-8", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
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
                logger.info("json File created and initiated with []")
        else:
            return True
    
    def is_link(self,link):
        return link.startswith("http://") or link.startswith("https://")
    
    def check_available(self, link):
        try:
                
            with open(file_path, "r") as f:
                urls = json.load(f)
            for url in urls:
                if url["real_link"] == link:
                    logger.info(f"Found mapped shortened link for {link}")
                    return link, url["shortened_link"]
            return False
        except Exception as e:
            logger.error("Error happened while checking whether the link is mapped before")
            return False
    def generated_before(self,shortened_link):
        try:
            with open(file_path, "r") as f:
                urls = json.load(f)
            for url in urls:
                if url["shortened_link"] == shortened_link:
                    logger.warning(f"This link is not valid(generated before try regenerating): {shortened_link}")
                    return url["real_link"]
            logger.info(f"This link is valid: {shortened_link}")
            return False
        except Exception as e:
            logger.error(f"err hapened while checking if the new generated link is valid: {e}")
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
            logger.info("New Link map added to json file")
            return True
        except Exception as e:
            print(f"Error while saving as json : {e}")
            logger.error(f"Error while saving as json : {e}")
            return False
    def generate(self, link):
        try:
            short_link = []
            for a in range(self.link_length):
                i = random.randint(0,len(self.chars)-1)
                short_link.append(self.chars[i])
            logger.info(f"New link generated {"".join(short_link)}")
            return link, self.base_link + "".join(short_link)
        except Exception as e:
            logger.error(f"error happened while generating short link: {e}")
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
            logger.error("Link shortening Successfull")
            return (link, generated_link)
        except Exception as e:
            logger.error(f"err happened while shortening {e}")
            print(e)
            

    def list_all(self):
        try:
            with open(file_path, "r") as f:
                urls = json.load(f)
            return urls
        except Exception as e:
            print("Error happened while listing them down")