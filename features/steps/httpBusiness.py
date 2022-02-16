from core.httpUtil import HttpOper
from core.kafkaUtil import kafkaOper
from behave import *
import json

from dotenv import load_dotenv
load_dotenv(verbose=True)
import os


@Given("获取主机地址")
def setp_impl(context):
    context.host=os.getenv("key")

@Given("获取主机端口")
def setp_impl(context):
    context.port=os.getenv("port")

@Given("设置get请求")
def setp_impl(context):
    context.method="get"

@Given("设置post请求")
def setp_impl(context):
    context.method="post"

@Given("设置请求路径{path}")
def setp_impl(context,path):
    context.path=path

@Given("设置请求参数{param}")
def setp_impl(context,param):
    context.param=param

@Given("设置请求头{header}")
def setp_impl(context,header):
    context.header=json.loads(header)

@When("发送请求")
def setp_impl(context,header):
    context.header=json.loads(header)
    url=f"http://{context.host}:{context.port}/{context.path}"
    context.session=HttpOper().call(context.method, url,params=context.param,headers=context.header)

@When("以{jmespath_pattern}方式获取接口返回存入变量{param_name}")
def step_impl(context,jmespath_pattern,param_name):
    context.session.setExportParam(param_name,"json",jmespath_pattern)

@When("以{regx_pattern}方式获取接口返回存入变量{param_name}")
def step_impl(context,regx_pattern,param_name):
    context.session.setExportParam(param_name,"regx",regx_pattern)

@When("获取前一次的返回值{param_name}")
def step_impl(context,param_name):
    context.session.getExportParam(param_name)


# @When("处理特定值{param_name}")
# def step_impl(context,param_name):
#     context.session.getExportParam(param_name)


@Given("输入{request_type},{path},{param},{header}")
def step_impl(context,request_type,path,param,header):
    context.host=os.getenv("host")
    context.port=os.getenv("port")
    url=f"http://{context.host}:{context.port}/{path}"
    context.session=HttpOper().call(request_type,url,headers=json.loads(header))

@Then("检查返回值是否包含{text_check}")
def step_impl(context,text_check):
    assert True==context.session.resCheck(flag="contain",key=text_check)

@Then("检查json返回值特定{json_pattern}包含{text_check}")
def step_impl(context,pattern,text_check):
    assert True==context.session.resCheck(flag='json',pattern=json_pattern,key=text_check)

@Then("检查返回值regx特定{regx_pattern}包含{text_check}")
def step_impl(context,pattern,text_check):
    assert True==context.session.resCheck(flag='regx',pattern=regx_pattern,key=text_check)

