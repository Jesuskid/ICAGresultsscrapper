from selenium import webdriver
from  selenium.webdriver.support.ui import Select
import time
import pandas

driver = webdriver.Edge('msedgedriver.exe')

results_list = []
with open('RESULTS.csv') as file:
    lines = file.readlines()

for i in lines:
    items = i.split(',')
    results_list.append(items)

print(results_list)
driver.get('https://resultchecker.icagh.org/')
for result in results_list:
    try:
        results_list[results_list.index(result)][2] = result[2].replace('\n', '')
        if (results_list.index(result) > 0):
            tab = driver.find_element_by_css_selector('#contact-tab')
            tab.click()
            time.sleep(1)
            student_number = driver.find_element_by_xpath(
                '/html/body/div/main/div[1]/div/div/div/div/div[3]/form/div[1]/input')
            time.sleep(1)
            student_number.send_keys(result[1])

            month_select = Select(
                driver.find_element_by_xpath(
                    '/html/body/div/main/div[1]/div/div/div/div/div[3]/form/div[2]/div[1]/select'))
            month_select.select_by_visible_text('November')

            year_select = Select(
                driver.find_element_by_xpath(
                    '/html/body/div/main/div[1]/div/div/div/div/div[3]/form/div[2]/div[2]/select'))
            year_select.select_by_visible_text('2021')
            button = driver.find_element_by_xpath(
                '/html/body/div/main/div[1]/div/div/div/div/div[3]/form/div[3]/div/button')
            button.click()
            time.sleep(4)

            table = driver.find_element_by_xpath(
                '/html/body/div/main/div/div/div/div/div/div[3]/div/div[2]/table/tbody/tr').find_elements_by_css_selector(
                'td')
            res = result
            for i in table:
                res.append(i.text)
            results_list[results_list.index(result)] = res
            print(results_list)
    except:
        results_list.pop(results_list.index(result))

driver.close()
results_list[0].append('Student number')
results_list[0].append('Exam number')
results_list[0].append('L3.1 (CR)')
results_list[0].append('L3.2 (AAA))')
results_list[0].append('L3.3 (AT)')
results_list[0].append("L3.4 (SCS)")
csv = pandas.DataFrame(results_list)
csv.columns = csv.iloc[0]
csv = csv[1:]
csv.reset_index(drop=True, inplace=True)
print(csv.head())
csv.to_csv('resultfile.csv')