# [exert-mysql](https://github.com/chaosannals/exert-mysql)

```sql
/* 赋权 */
GRANT ALL PRIVILEGES ON schemaname.* TO 'useraccount'@'%';
FLUSH PRIVILEGES;
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
