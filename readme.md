# [exert-mysql](https://github.com/chaosannals/exert-mysql)

```sql
/* 赋权 */
GRANT ALL PRIVILEGES ON schemaname.* TO 'useraccount'@'%';

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
