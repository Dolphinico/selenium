import selenium                 # импортируем библиотеки селениума
import time                     # импортируем библиотеки времени

from selenium import webdriver  # импортируем селениум в вебдрайвер
from selenium.webdriver.common.keys import Keys # импортируем вебдайвер который обеспечивает взаимодействие с командами клавиатуры


driver = webdriver.Chrome("C:\python_projects\selenium\drivers\chromedriver.exe")  # указание драйверов необходимых для работы
# driver = webdriver.Firefox()

driver.set_page_load_timeout(10)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("github.com")
# driver.find_element_by_name("btnK").click()               # click для нажатия по элементу
driver.find_element_by_name("btnK").send_keys(Keys.RETURN)  # отправка команды нажатия конкретной клавиши - ENTER(RETURN)
time.sleep(4) # таймер для остановки, перед выполнением следующей строки
driver.quit()