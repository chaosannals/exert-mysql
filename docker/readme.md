# Docker

## 容器

```sh
docker run -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -v /host/mysql/data:/var/lib/mysql -v /host/mysql/file:/var/lib/mysql-files -v /host/mysql/config:/etc/mysql -d --restart=always --name mysql mysql
```

/host/mysql/config 目录需要预先在宿主机上生成。
实例 config 目录里，确保有 my.cnf 文件。
