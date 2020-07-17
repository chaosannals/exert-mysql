package replicator

import (
	"fmt"
	log "github.com/cihub/seelog"
	"github.com/siddontang/go-mysql/canal"
)

//MyEventHandler 自定义
type MyEventHandler struct {
	canal.DummyEventHandler
}

//OnRow 行
func (h *MyEventHandler) OnRow(e *canal.RowsEvent) error {
	log.Infof("%s %v\n", e.Action, e.Rows)
	return nil
}

//String 字符串
func (h *MyEventHandler) String() string {
	return "MyEventHandler"
}

//ReplicateByCanal 示例，需要命令下有 mysqldump
func ReplicateByCanal() {
	cfg := canal.NewDefaultConfig()
	cfg.Addr = "127.0.0.1:3306"
	cfg.User = "replicator"
	cfg.Password = "123456"
	cfg.Dump.TableDB = "exert"
	cfg.Dump.Tables = []string{"e_mobilephone"}
	
	c, err := canal.NewCanal(cfg)
	if err!=nil {
		fmt.Println("error",err)
	}

	c.SetEventHandler(&MyEventHandler{})
	c.Run()
}
