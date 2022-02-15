Feature: http请求并检查
    Scenario Outline: 
        Given 输入<request_type>,<url>,<param>,<header>
        # Given 输入<username>,<password>,<client_id>
        # When <url>,<param>,<header>
        # Then 检查返回码是否为<status_code>
        Then 检查返回值是否包含<text_check>
        # Then 检查json返回值特定<json_pattern>包含<text_check>
    Examples:
        | request_type | header |url | text_check|
        | get | {"Content-Type":"application/json;charset=UTF-8"} | http://192.168.xxx.xxx:9499/device/v1/api/devices/926499854176743469 | 926499854176743469|


    Scenario Outline: 查询设备状态,检查json结果定位包含
        Given 输入<request_type>,<url>,<param>,<header>
        # Given 输入<username>,<password>,<client_id>
        # When <url>,<param>,<header>
        # Then 检查返回码是否为<status_code>
        # Then 检查返回值是否包含<text_check>
        Then 检查json返回值特定<json_pattern>包含<text_check>
        Examples:
            | request_type | header                                            | url                                                                  | text_check         | json_pattern |
            | get          | {"Content-Type":"application/json;charset=UTF-8"} | http://192.168.xxx.xxx:9499/device/v1/api/devices/926499854176743469 | 926499854176743469 | data.id      |


    Scenario Outline: 查询设备状态,检查结果regx定位包含
        Given 输入<request_type>,<url>,<param>,<header>
        # Given 输入<username>,<password>,<client_id>
        # When <url>,<param>,<header>
        # Then 检查返回码是否为<status_code>
        # Then 检查返回值是否包含<text_check>
        Then 检查返回值regx特定<regx_pattern>包含<text_check>
        Examples:
            | request_type | header                                            | url                                                                  | text_check         | regx_pattern |
            | get | {"Content-Type":"application/json;charset=UTF-8"} | http://192.168.xxx.xxx:9499/device/v1/api/devices/926499854176743469 | 926499854176743469 | \"data\":{\"id\":\"(.*)\" |


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
