package replicator

import (
	"context"
	"os"
	"github.com/satori/go.uuid"
	"github.com/siddontang/go-mysql/mysql"
	"github.com/siddontang/go-mysql/replication"
)

//ReplicateByPosition 通过文件名及其位移获取日志
func ReplicateByPosition() {
	cfg := replication.BinlogSyncerConfig{
		ServerID: 100,
		Flavor:   "mysql",
		Host:     "127.0.0.1",
		Port:     3306,
		User:     "replicator",
		Password: "123456",
	}
	syncer := replication.NewBinlogSyncer(cfg)
	streamer, _ := syncer.StartSync(mysql.Position{"binlog.000002", 0})
	for {
		ev, _ := streamer.GetEvent(context.Background())
		ev.Dump(os.Stdout)
	}
}

//ReplicateByGUID 移获取日志
func ReplicateByGUID() {
	cfg := replication.BinlogSyncerConfig{
		ServerID: 100,
		Flavor:   "mysql",
		Host:     "127.0.0.1",
		Port:     3306,
		User:     "replicator",
		Password: "123456",
	}
	
	syncer := replication.NewBinlogSyncer(cfg)
	uuid := uuid.Must(uuid.FromString("2d94cff5-c575-11ea-a36d-0242ac110003"))
	it := mysql.Interval{}
	it.Start = 1
	it.Stop = 9
	set := mysql.NewUUIDSet(uuid, it)
	mset := &mysql.MysqlGTIDSet{}
	mset.Sets = map[string]*mysql.UUIDSet{"21-30": set}
	streamer, _ := syncer.StartSyncGTID(mset)
	for {
		ev, _ := streamer.GetEvent(context.Background())
		ev.Dump(os.Stdout)
	}
}
