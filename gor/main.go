package main

import (
	"context"
	"fmt"
	"os"

	"time"

	"github.com/go-mysql-org/go-mysql/mysql"
	"github.com/go-mysql-org/go-mysql/replication"
)

func main() {
	cfg := replication.BinlogSyncerConfig{
		ServerID: 100,
		Flavor:   "mysql",
		Host:     "127.0.0.1",
		Port:     3306,
		User:     "root",
		Password: "password",
	}
	syncer := replication.NewBinlogSyncer(cfg)

	// 设置起始点。
	streamer, _ := syncer.StartSync(mysql.Position{
		Name: "binlog.000221",
		Pos:  0,
	})

	// 读取循环
	for {
		ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
		ev, err := streamer.GetEvent(ctx)
		cancel()

		if err == context.DeadlineExceeded {
			continue
		}

		et := ev.Header.EventType // 类型
		ep := ev.Header.LogPos // 位置，可以保存后通过这个位置，断点续读。
		fmt.Println(ep)

		// 判定类型，并用强制类型转换获得指定类型的指针
		if et == replication.ROTATE_EVENT {
			// 切换文件的时候必定有的日志，每个日志文件的头行日志。
			re := ev.Event.(*replication.RotateEvent)
			fmt.Println(string(re.NextLogName), re.Position)
		} else if (et == replication.WRITE_ROWS_EVENTv2) {
			// 插入类型，MYSQL 不同版本的增删改查日志略有不同，所以这里有版本。
			wr := ev.Event.(*replication.RowsEvent)
			fmt.Println(wr.Rows)
		} else {
			ev.Dump(os.Stdout)
		}
	}
}
