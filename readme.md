# [exert-mysql](https://github.com/chaosannals/exert-mysql)

## Docker

```sh
docker run --restart=always --name mysql -v /host/mysql:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql
```

```sh
echo "\nenforce_gtid_consistency=ON\ngtid_mode=ON\n" >> /etc/mysql/my.cnf
```