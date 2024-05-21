# [exert-mysql](https://github.com/chaosannals/exert-mysql)

```sql
/* 列举数据库 */
SHOW DATABASES;

/* 列举表 */
SHOW TABLES;

```

```sql
/* 赋权 */
GRANT ALL PRIVILEGES ON schemaname.* TO 'useraccount'@'%';

/* 赋权，指定权限 */
GRANT DROP, SELECT ON schemaname.* TO useraccount@'%'; 

/* 赋权，指定权限和密码(已有账号，如果再赋权，在一些特定条件下，密码会被清掉，所以赋权要带上原密码。) */
GRANT ALL PRIVILEGES ON schemaname.* TO useraccount@'%' IDENTIFIED BY '123456' WITH GRANT OPTION; 

/* 删除权限 */
REVOKE ALL ON schemaname.* FROM useraccount@'%';

/* 删除权限，指定权限 */
REVOKE DROP, SELECT ON schemaname.* FROM useraccount@'%';

/* 刷新账号修改 */
FLUSH PRIVILEGES;

/* 查看账号权限 不填 @ 默认是 @'%' */
SHOW GRANTS FOR useraccount;

/* 出现过空字符串 Host 情况 */
SHOW GRANTS FOR useraccount@'';

/* 查看账号信息 需要权限 */
SELECT * FROM mysql.user;

/* 查看账号信息 需要权限 查询 条件 Host  User 等字段 */
SELECT * FROM mysql.user WHERE Host='' OR User IN ('tester');

/* 创建账号 */
CREATE USER useraccount IDENTIFIED BY 'password';

/* 删除账号 不填 @ 默认是 @'%' */
DROP USER useraccount;
DROP USER useraccount@'%';

/* 出现了创建账号空 host 的情况 */
DROP USER useraccount@'';

/* 修改密码 （5.6 见下文） */
ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';

/* 修改密码指定加密类型，用 mysql 命令行客户端本地首次修改 root 密码必须是 localhost 的 */
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

/* 直接通过更新mysql.user 数据库修改密码，但是账号要有权限，有时候公司给你的账号权限不够 */
UPDATE mysql.user SET password=PASSWORD('123456') WHERE user='username';
```

## binlog

```sql
/* 显示二进制文件列表 */
SHOW BINARY LOGS

/* 查询列举事件 */
SHOW BINLOG EVENTS IN 'mysql-bin.000563' FROM 4 LIMIT 100, 100;

/* 查询主机状态 */
SHOW MASTER STATUS

/* 删除指定日志文件 */
PURGE MASTER LOGS TO 'mysql-bin.010';

/* 删除指定日期之前 */
PURGE MASTER LOGS BEFORE '2008-12-19 21:00:00';

/* 删除 7 天前日志 */
PURGE MASTER LOGS BEFORE DATE_SUB(CURRENT_DATE, INTERVAL 7 DAY);
```


## Docker

```sh
# 在 docker 宿主机修改 ./docker/config 的权限。
# windows 下为 wsl -d docker-desktop 下
chmod 644 -R ./docker/config
```

```sh
docker-compose up -d
```


## Mysql 5.6

```sql
/* 设置密码 */
SET PASSWORD for 'root'@'localhost' = PASSWORD('password');
```

## MySQL 5.5

需要找到 /etc/my.cnf 删掉 skip_name_resolve 才命令行能用 mysql -p root 登录。

```bash
# 首次只能通过该命令执行，去掉 skip_name_resolve，不然首次也不行。
mysql 

# 这个命令首次无法运行。
mysql -e "SET PASSWORD for 'root'@'localhost' = PASSWORD('password');"
```
