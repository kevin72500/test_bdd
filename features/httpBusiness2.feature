Feature: http请求并检查
    Scenario: 
        Given 获取主机地址
        Given 获取主机端口
        Given 设置get请求  
        Given 设置请求路径{path}
        |path|
        | device/v1/api/devices/926499854176743469 |
        Given 设置请求头{header}
            | header                                            |       
            | {"Content-Type":"application/json;charset=UTF-8"} | 
        When 发送请求
        Then 检查返回值是否包含<text_check>
            |text_check|
            | 926499854176743469 |

# Feature: kafka消息检查
#     检查kafka X 分钟内有没有包含 X 的消息
#     Scenario Outline: kafka检查消息
#         Given 输入kafka<address>,<topic>
#         Given 分钟数<mins>
#         Given 检查方式<flag>,检查匹配<pattern>,目标字符<key>
#         When 初始化kafka连接
#         Then 检查是否存在
#     Examples:
#         |address|topic|mins|flag|pattern|key|
