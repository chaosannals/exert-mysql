package replicator

import (
	"log"
	// "github.com/satori/go.uuid"
	"github.com/siddontang/go-mysql/mysql"
	"github.com/siddontang/go-mysql/canal"
	"github.com/siddontang/go-mysql/replication"
)

//CustomEventHandler 自定义事件处理器
type CustomEventHandler struct {
	Start bool
}

//OnRotate 日志切割
func (h *CustomEventHandler) OnRotate(roateEvent *replication.RotateEvent) error {
	log.Println("OnRotate")
	log.Printf("%d", roateEvent.Position)
	h.Start = true
	return nil
}

//OnTableChanged 表变动
func (h *CustomEventHandler) OnTableChanged(schema string, table string) error {
	log.Println("OnTableChanged")
	return nil
}

//OnDDL 表定义
func (h *CustomEventHandler) OnDDL(nextPos mysql.Position, queryEvent *replication.QueryEvent) error {
	log.Println("OnDDL")
	return nil
}

//OnXID XA分布式事务
func (h *CustomEventHandler) OnXID(nextPos mysql.Position) error {
	log.Println("OnXID")
	return nil
}

//OnGTID 全局事务ID
func (h *CustomEventHandler) OnGTID(gtid mysql.GTIDSet) error {
	log.Println("OnGTID")
	log.Println(gtid.String())
	return nil
}

//OnPosSynced 同步
func (h *CustomEventHandler) OnPosSynced(pos mysql.Position, set mysql.GTIDSet, force bool) error {
	log.Println("OnPosSynced")
	log.Printf("%s %d", pos.Name, pos.Pos)
	return nil
}

//OnRow 行
func (h *CustomEventHandler) OnRow(e *canal.RowsEvent) error {
	log.Printf("%s %v\n", e.Action, e.Rows)
	for _, v := range e.Table.Columns {
		log.Printf("%s\n", v.Name)
	}
	return nil
}

//String 字符串
func (h *CustomEventHandler) String() string {
	return "CustomEventHandler"
}

//ReplicateByCanalGTID 示例，需要命令下有 mysqldump
func ReplicateByCanalGTID() {
	cfg := canal.NewDefaultConfig()
	cfg.Addr = "127.0.0.1:13306"
	cfg.User = "replicator"
	cfg.Password = "123456"
	// cfg.Dump.TableDB = "exert"
	// cfg.Dump.Tables = []string{"e_mobilephone", "e_telephone"}
	c, _ := canal.NewCanal(cfg)
	//uuid := uuid.Must(uuid.FromString("2d94cff5-c575-11ea-a36d-0242ac110003"))
	//it := mysql.Interval{}
	//it.Start = 1
	//it.Stop = 9
	//set := mysql.NewUUIDSet(uuid, it)
	//mset := &mysql.MysqlGTIDSet{}

	//m := map[string]*mysql.UUIDSet{"28": set}
	//mset.Sets = m
	//c.StartFromGTID(mset)

	c.SetEventHandler(&CustomEventHandler{})

	c.Run()
}
