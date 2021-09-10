import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

def test_see_button_add_to_basket(browser):
	
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(link)
	#time.sleep(30)
	assert browser.find_element_by_css_selector(".btn-add-to-basket"), "No button 'Add to basket' on page!"
#