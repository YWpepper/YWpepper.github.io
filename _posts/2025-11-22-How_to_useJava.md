---
layout: post
title: 'How_to_useJava'
date: 2025-11-22
author: pepper
tags: [Java]
comments: true
toc: true
pinned: false
---
这篇博客介绍了JAVA下的代码生成器。
<!-- more -->

### JAVA 代码生成器


1. 修改generator.properties文件
比如代码配置文件 `renren-generator/target/classes/generator.properties`
  
```properties
#代码生成器，配置信息

mainPath=com.atpepper
#包名
package=com.atpepper.modules
moduleName=coupon
#作者
author=pepper
#Email
email=newen.yan@gmail.com
#表前缀（类名不会包含表前缀）
tablePrefix=pms_

#\u7C7B\u578B\u8F6C\u6362\uFF0C\u914D\u7F6E\u4FE1\u606F
tinyint=Integer
smallint=Integer
mediumint=Integer
int=Integer
integer=Integer
bigint=Long
float=Float
double=Double
decimal=BigDecimal
bit=Boolean

char=String
varchar=String
tinytext=String
text=String
mediumtext=String
longtext=String


date=Date
datetime=Date
timestamp=Date

NUMBER=Integer
INT=Integer
INTEGER=Integer
BINARY_INTEGER=Integer
LONG=String
FLOAT=Float
BINARY_FLOAT=Float
DOUBLE=Double
BINARY_DOUBLE=Double
DECIMAL=BigDecimal
CHAR=String
VARCHAR=String
VARCHAR2=String
NVARCHAR=String
NVARCHAR2=String
CLOB=String
BLOB=String
DATE=Date
DATETIME=Date
TIMESTAMP=Date
TIMESTAMP(6)=Date

int8=Long
int4=Integer
int2=Integer
numeric=BigDecimal

nvarchar=String

```

2. 修改yaml文件
比如代码配置文件 `renren-generator/src/main/resources/application.yaml`,修改现在需要连接的数据库`gulimail_sms`

```yaml
server:
  port: 80

# mysql
spring:
  datasource:
    type: com.alibaba.druid.pool.DruidDataSource
    #MySQL配置
    driverClassName: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3308/gulimail_sms?useUnicode=true&characterEncoding=UTF-8&useSSL=false&serverTimezone=Asia/Shanghai
    username: root
    password: xxxxxxxx
```
3. 运行生成器服务
运行 `RenrenGeneratorApplication` 类，启动代码生成器服务，该项目启动后会运行到localhost:80端口，生成代码到 `gulimail_sms` 数据库中对应的表。

  <img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763794603048-80bf3e8a-b6ba-49c1-a127-bd365116f9ff.png?x-oss-process=image%2Fformat%2Cwebp" width="100%" alt="FinRpt Framework Diagram"/>

  3. 替换生成代码
生成代码的java和resource替换掉原来的代码现在需要修补里的common包

```xml
  <!-- Add shared common utilities so controllers/services can import com.atpepper.common.* -->
  <dependency>
    <groupId>com.atpepper.gulimail</groupId>
    <artifactId>gulimail-common</artifactId>
    <version>0.0.1-SNAPSHOT</version>
  </dependency>
```

4. 配置yaml文件

修改 `gulimail-sms/src/main/resources/application.yaml` 文件，配置数据库连接

```yaml

spring:
  config:
    import: "optional:nacos:"
  datasource:
    username: root
    password: xxxxxx
    url: jdbc:mysql://localhost:3308/gulimail_sms?useUnicode=true&characterEncoding=UTF-8&useSSL=false&serverTimezone=Asia/Shanghai
    driver-class-name: com.mysql.cj.jdbc.Driver

mybatis-plus:
  mapper-locations: classpath*:/mapper/**/*.xml
  global-config:
    db-config:
      id-type: auto
```
5. 测试运行
   根据代码的路由打开网站`http://localhost:8080/coupon/coupon/list` 

```java
@RestController
@RequestMapping("/coupon/coupon")
public class CouponController {
    @Autowired
    private CouponService couponService;
}
```

网站响应如下：
  <img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763816685783-30c05649-32b0-4f48-8e06-a1d237f48988.png?x-oss-process=image%2Fformat%2Cwebp" width="100%" alt="FinRpt Framework Diagram"/>


6. 手动修改由于路径冲突问题
  
  在模板 `Controller.java.vm` 添加类级 `@RequestMapping("/${moduleName}/${classname}")`，生成的控制器将拥有唯一前缀，避免所有实体共享根路径导致的 `/update` 等冲突。

```java
package ${package}.${moduleName}.controller;

import java.util.Arrays;
import java.util.Map;

//import org.apache.shiro.authz.annotation.RequiresPermissions;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import ${package}.${moduleName}.entity.${className}Entity;
import ${package}.${moduleName}.service.${className}Service;
import ${mainPath}.common.utils.PageUtils;
import ${mainPath}.common.utils.R;

/**
 * ${comments}
 *
 * @author ${author}
 * @email ${email}
 * @date ${datetime}
 */
@RestController
@RequestMapping("/${moduleName}/${classname}")
public class ${className}Controller {
    @Autowired
    private ${className}Service ${classname}Service;

    /**
     * 列表
     */
    @RequestMapping("/list")
    //@RequiresPermissions("${moduleName}:${pathName}:list")
    public R list(@RequestParam Map<String, Object> params){
        PageUtils page = ${classname}Service.queryPage(params);

        return R.ok().put("page", page);
    }


    /**
     * 信息
     */
    @RequestMapping("/info/{${pk.attrname}}")
    //@RequiresPermissions("${moduleName}:${pathName}:info")
    public R info(@PathVariable("${pk.attrname}") ${pk.attrType} ${pk.attrname}){
		${className}Entity ${classname} = ${classname}Service.getById(${pk.attrname});

        return R.ok().put("${classname}", ${classname});
    }

    /**
     * 保存
     */
    @RequestMapping("/save")
    //@RequiresPermissions("${moduleName}:${pathName}:save")
    public R save(@RequestBody ${className}Entity ${classname}){
		${classname}Service.save(${classname});

        return R.ok();
    }

    /**
     * 修改
     */
    @RequestMapping("/update")
    //@RequiresPermissions("${moduleName}:${pathName}:update")
    public R update(@RequestBody ${className}Entity ${classname}){
		${classname}Service.updateById(${classname});

        return R.ok();
    }

    /**
     * 删除
     */
    @RequestMapping("/delete")
    //@RequiresPermissions("${moduleName}:${pathName}:delete")
    public R delete(@RequestBody ${pk.attrType}[] ${pk.attrname}s){
		${classname}Service.removeByIds(Arrays.asList(${pk.attrname}s));

        return R.ok();
    }

}

```


---