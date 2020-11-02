# pytest 执行方式
## 执行方式一
1. 打开Terminal，进入pytest.ini文件目录
```shell script
    cd /conf/
```
2. 执行pytest命令，执行测试用例后在该目录下生成report目录
```shell script
    pytest
```
3. 将json转为html
```shell script
    allure generate report/ -o report/html --clean
```
4. 打开报告
```shell script
    allure serve report/
```
## 执行方式二
1. 生成jenkins可查看报告命令
```shell script
    cd /conf/
    pytest --alluredir ./allure-results
```