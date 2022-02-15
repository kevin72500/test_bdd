# 1.安装requirments.txt的依赖包
# 2.按照格式编写
*.feature文件
```
Feature: 百度搜索
  Scenario: 搜索关键词
    Given 关键词 behave
    When 打开百度页面
    And  输入关键词
    And  点击百度一下按钮
    Then 页面标题中应包含关键词
```
steps中*.py文件
```
from behave import given, when, then

@given('关键词 {keyword}')    # 对应步骤  Given 关键词 behave， 参数放在{}中
def step_impl(context, keyword):   # context是上下文对象，有参数的话，加上对应参数
    context.keyword = keyword  # 将参数绑定上下文对象，以便其他步骤使用

@when('打开百度页面')
def step_impl(context):
    context.driver = driver = webdriver.Chrome()  # 同样绑定上下文对象
    driver.implicitly_wait(10)
    driver.get('https://www.baidu.com')

@then('页面标题中应包含关键词')
def step_impl(context):
    assert context.keyword in context.driver.title
```
