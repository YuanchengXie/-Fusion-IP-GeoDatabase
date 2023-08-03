package cdccbdr

import (
	"bufio"
	"iplocate/lib"
	"iplocate/utils"
	"os"
	"strconv"
)

/*
this functioin read ping result from rapath and get cdc of each city
then writes cdc out into wtpath
*/
func ParseCdc(rdPath string, wtPath string) error {
	spingRes, err := utils.ReadSpingRes_RttMs(rdPath)
	if err != nil {
		return err
	}
	//rtt:count
	rcMap := map[int]int{}
	for _, r := range spingRes {
		rcMap[r.Rtt]++
	}
	trim(rcMap, mode(rcMap), len(spingRes))
	return writeCdc(rcMap, len(spingRes), wtPath)
}

func writeCdc(cdc lib.CDCType, total int, wtpath string) error {
	fi, err := os.OpenFile(wtpath, os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
	if err != nil {
		return err
	}
	defer fi.Close()
	wtr := bufio.NewWriter(fi)
	for rtt, count := range cdc {
		p := float64(count) * 100 / float64(total)
		pstr := strconv.FormatFloat(p, 'f', 2, 64)
		_, err := wtr.WriteString("rtt=" + strconv.Itoa(rtt) + ", p=" + pstr + "\n")
		if err != nil {
			return err
		}
	}
	wtr.Flush()
	return nil
}

// mode: the number who appears most frequently
func mode(rcMap map[int]int) int {
	m := 0
	cnt := 0
	for w_, cnt_ := range rcMap {
		if cnt_ > cnt {
			m = w_
			cnt = cnt_
		}
	}
	return m
}

// drop all rtt:count pair whose rtt value is greater than mode/20 or lower than mode*20
func trim(rcMap map[int]int, mode int, total int) {
	lw := mode / 20
	rw := mode * 20
	for rtt, cnt := range rcMap {
		if rtt < lw || rtt > rw || cnt*1000 < total {
			delete(rcMap, rtt)
		}
	}
}
