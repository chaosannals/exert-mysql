package main

import (
	"github.com/chaosannals/exert-mysql/replicator"
)

func main() {
	replicator.ReplicateByPosition()
	// replicator.ReplicateByGUID()
	// replicator.ReplicateByCanal()
}