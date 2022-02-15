from core.httpUtil import HttpOper
from core.kafkaUtil import kafkaOper
from behave import *
import json

@Given("输入{request_type},{url},{param},{header}")
def step_impl(context,request_type,url,param,header):
    context.session=HttpOper().call(request_type, url,headers=json.loads(header))

@Then("检查返回值是否包含{text_check}")
def step_impl(context,text_check):
    assert True==context.session.resCheck(flag="contain",key=text_check)

@Then("检查json返回值特定{json_pattern}包含{text_check}")
def step_impl(context,pattern,text_check):
    assert True==context.session.resCheck(flag='json',pattern=json_pattern,key=text_check)

@Then("检查返回值regx特定{regx_pattern}包含{text_check}")
def step_impl(context,pattern,text_check):
    assert True==context.session.resCheck(flag='regx',pattern=regx_pattern,key=text_check)
