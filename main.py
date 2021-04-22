from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
#打开Coreplus首页
coreplus = 'http://170.18.10.231:11000/_web/mspplus/main/index.jsp'
driver.get(coreplus)
#窗口最大化
driver.maximize_window()

#登录Coreplus
#定位用户名，输入用户
userName = driver.find_element_by_id("userName")
userName.send_keys("admin")

#定位密码框，输入密码
userPassword = driver.find_element_by_id("password")
userPassword.send_keys("admin123")

#定位并点击登录
driver.find_element_by_xpath("//button[@class='login-btn']").click()

#定位点击工程管理
gcgl = driver.find_element_by_xpath("//*[@id='core-top_nav']/div[1]/ul/li[3]/a/div/span")
gcgl.click()

#工程构建无法交互，需要使用单击后鼠标悬浮到工程构建，点击
gcgj = driver.find_element_by_xpath("//*[@id='core-top_nav']/div[1]/ul/li[3]/div/ul/li[2]/a/span")
ActionChains(driver).move_to_element(gcgj).perform()
gcgj.click()
ActionChains(driver).move_to_element(gcgl).perform()

#需要切换frame否则无法定位到元素
core_main = driver.find_element_by_css_selector("iframe[src='corePlus/engineeringManagement/ztree.html']")
driver.switch_to_frame(core_main)

mrgzkj = driver.find_element_by_xpath("//span[@id='treeDemo_1_span']")
ActionChains(driver).move_to_element(mrgzkj).perform()
mrgzkj.click()

driver.find_element_by_xpath("//*[@title='宁波理工教职工费用报销']").click()
driver.find_element_by_xpath("//*[@title='表单']").click()




