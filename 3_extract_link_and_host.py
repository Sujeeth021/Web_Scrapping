from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
import pandas as pd
import re
from selenium.common.exceptions import NoSuchElementException

input_file = "input_1.csv"
output_file = "output_1.csv"

n1,n2 = 457,1487
link_output_file = "output\\{},{}_link.txt".format(n1,n2)
host_output_file = "output\\{},{}_host.txt".format(n1,n2)
# output3 = "output\\{},{}_excel.xlsx".format(n1,n2)
# no_of_times = range(n1,n2)

chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
global final_aws_list_file
global final_aws_list
final_aws_list_file = "output\\final_aws_list_file_1.csv"

try:
    final_aws_list = list(pd.read_csv(final_aws_list_file,header=None)[0])
except:
    f = open(final_aws_list_file, "w")
    f.write("0")
    f.close()

def link_extractor(button_no):
    browser = webdriver.Chrome(options=chromeOptions)
    browser.get(button_no)
    # time.sleep(5)

    # for i in range(0,(button_no//20)):
    #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight-100);")
    #     time.sleep(5)
        
    # doc = browser.find_element(By.CSS_SELECTOR, "app-company-card.mb-3:nth-child({}) > div:nth-child(1) > div:nth-child(4) > button:nth-child(1)".format(button_no))
    
    # browser.execute_script("arguments[0].click()",doc)
    # time.sleep(5)


    doc1 = browser.find_element(By.CSS_SELECTOR,'a.ng-star-inserted:nth-child(3)')

    a = doc1.get_attribute("href")
    print(a)
    browser.quit()
    
    f = open(link_output_file, "a")
    f.write(a+'\n')
    f.close()

    return a

def get_host(ls):
    # if ls in final_aws_list:
    #     return "aws"

    pattern = r"https?://(?:www\.)?([a-zA-Z0-9.-]+)"
    match = re.search(pattern, ls)
    a =match.group(1)    

    browser = webdriver.Chrome(options=chromeOptions)
    browser.get("https://hostadvice.com/tools/whois/#{}".format(ls))
    time.sleep(5)

    doc = browser.find_element("xpath",'/html/body/div[3]/div[2]/section[2]/div[1]/div[2]/ul/li[1]/div/a')
    b = doc.text
    browser.quit()
    f = open(host_output_file, "a")
    f.write(b+'\n')
    
    f.close()
    # check_and_write_to_final_aws_file(ls,b,final_aws_list)
    return b


def check_and_write_to_final_aws_file(host_name,website,final_aws_list):
    if (host_name == "Amazon Web Services (AWS)"):
        f = open(final_aws_list_file, "a")
        f.write(website+'\n')
        f.close()
        final_aws_list = list(pd.read_csv(final_aws_list_file,header=None)[0])


list1 = []
list2 = []
student = dict()


list_input_1 = list(pd.read_csv(input_file,header=None)[0])
# print(list_1)
len1 = len(list_input_1)
uuuu = 0
for i in list_input_1:
    try:
        website_link = link_extractor(i)
    except:
        website_link = 0
    # print(i)
    if website_link:
        list1.append(website_link)
        ls = website_link
        try:
            host_name = get_host(ls)
        except:
            host_name = 0
            continue
        
        f = open(output_file, "a")
        f.write(i+','+website_link+','+host_name+'\n')
        print(uuuu)
        uuuu += 1
        f.close()
        # check_and_write_to_final_aws_file(host_name,ls,final_aws_list)

# list1 = list(pd.read_csv("output\\{},{}_link.txt".format(51,150),header=None)[0])

# for ls in list1:
    
#     if ls != "nil":
#         try:
#             host_name = get_host(ls)
#         except:
#             host_name = 0
        
#         list2.append(host_name)
#         check_and_write_to_final_aws_file(host_name,ls,final_aws_list)

# dict1 = {"Company name": list1, "Host":list2}

# df = pd.DataFrame(data=dict1)

# df.to_excel(output3)
