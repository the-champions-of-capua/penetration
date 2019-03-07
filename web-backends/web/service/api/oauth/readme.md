## 设置用户管理

- 用户管理项目的相关内容

- 查看 `TOKEN` 用户
 - `select username, created from authtoken_token left join auth_user on auth_user.id=user_id;`


## 2018-9-18 
- 管理员写入用户一定要计入审计日志
- 给用户页面添加一个设置, 只有管理员权限才能看到用户的编辑页面

## 2018-9-19
- 1, 新的令牌挤掉原来的登陆账户
- 2, 在单位时间内重复登陆失败次数过多, 封禁几分钟 
- 3, 测试继承和重写原来的 `ObtainJSONWebToken`

## 2018-9-20 
- 1, `django-rest-auth` 查看
- 2, 放弃 `django-black-list` 自己编译的结果失败
- 3, 准备完成相关后台的开发工作和相关的详细逻辑的准备

## 2018-9-21
- 1, 完成所有基础配置管理
- 2, 完成规则的基础分类
- 3, 完成内置规则文件的规则启停
- 4, 完成高级访问设置的相关设置
- 5, 完成日志报表的条件查询和生成
- 上述是紧急完成的内容; 完成和优化须知
- [jwt](https://tools.ietf.org/html/rfc7519)
- [node-jwt](https://github.com/auth0/node-jsonwebtoken)

## 2018-9-22
- [黑名单设计](./blacklist) 里面的相关设置
- 新的想法, jwt 高级功能的设置
  - 1, 使用中间件来对应
  - 2, 登陆失败和成功都可以用stat传递

## 2018-10-18
- [github解决方案](https://github.com/GetBlimp/django-rest-framework-jwt/issues/456)
- `JWT_GET_USER_SECRET_KEY`
- 终止账号登陆而不是`Remote_addr`

## 2018-10-29
- 完成登陆频繁的接口
- 完成单点登陆的功能实现
- [内容说明](./local_jwt/readme.md)

## 2018-10-30
- 修复和修改扫描器的相关接口[暂时没出现问题, 但是以后呢]

