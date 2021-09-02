import requests
import wget
from bs4 import BeautifulSoup


def download_images(direct_img_url):
    file_content = requests.get(direct_img_url)
    # detects file name using file url and will be used to name file
    file_name = wget.detect_filename(url=direct_img_url)
    print("Downloading ", file_name)
    open(file_name, "wb").write(file_content.content)


class Assets:
    def __init__(self, url: str):
        self.url = url

    def pull_images(self, download: bool = False):
        htmlcontent = requests.get(f"{self.url}").text  # get html content of pages
        noodle_soup = BeautifulSoup(
            htmlcontent, "html.parser"
        )  # finding all img tags  and storing
        anchors = noodle_soup.find_all("img")
        filtered_list = list(set(anchors))  # filtering duplicate images

        for images in filtered_list:
            print(self.url + images["src"])
        if download == True:
            for images in filtered_list:
                complete_url_of_file = self.url + images["src"]
                download_images(
                    direct_img_url=complete_url_of_file
                )  # downloading all images

    def get_all_links(self):  # prints all links found in pages
        htmlcontent = requests.get(f"{self.url}").text
        noodle_soup = BeautifulSoup(htmlcontent, "html.parser")
        anchors = noodle_soup.find_all("a")
        for href in anchors:
            print(href["href"])


"""     |      page link       |     method     |  """
Assets("https://www.itsnp.org/").get_all_links()
