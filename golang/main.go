package main

import (
	"bufio"
	"errors"
	"fmt"
	"github.com/hashicorp/golang-lru/v2"
	"io"
	"math"
	"os"
	"strconv"
	"strings"
)

type Valve struct {
	name      string
	flow_rate int
	ends      []string
}

// TODO: simplify
func parseValve(input string) (Valve, error) {
	var valve Valve
	splits := strings.Split(input, ";")
	if len(splits) != 2 {
		return valve, errors.New("Invalid input" + input)
	}

	name := strings.Split(splits[0], " ")[1]
	valve.name = name

	rate, err := strconv.Atoi(strings.Split(strings.Split(splits[0], " ")[4], "=")[1])
	if err != nil {
		return valve, err
	}
	valve.flow_rate = rate

	endsString := strings.Join(strings.Split(strings.Trim(splits[1], " \n"), " ")[4:], "")

	ends := strings.Split(endsString, ",")
	valve.ends = ends

	return valve, nil
}

type DpKey struct {
	timeLeft     int
	currentValve string
	openList     int64
}

// Only returns how many additional pressure is released except for the currently open ones
func getMostPressureReleaseable(timeLeft int, currentValve string, openValves int64, valves map[string]ValveWithIdx, dpDict *lru.Cache[DpKey, int]) int {
	// println("==================", timeLeft, currentValve)
	if timeLeft <= 0 {
		// fmt.Println("Returning using time")
		return 0
	}
	if openValves == int64(math.Pow(2, float64(len(valves))))-1 {
		// fmt.Println("Returning using openValves")
		return 0
	}

	dpKey := DpKey{timeLeft, currentValve, openValves}
	value, exists := dpDict.Get(dpKey)
	if exists {
		return value
	}

	maxResult := 0
	cr := valves[currentValve]
	// fmt.Println("Getting valve", currentValve, cr, valves)

	if (1<<cr.idx)&openValves == 0 && cr.valve.flow_rate != 0 { // not open yet
		for _, v := range cr.valve.ends {
			maxResult = getMostPressureReleaseable(timeLeft-2, v, openValves+(1<<cr.idx), valves, dpDict) + (timeLeft-1)*cr.valve.flow_rate
		}

	}

	for _, v := range cr.valve.ends {
		maxResult = max(maxResult,
			getMostPressureReleaseable(timeLeft-1, v, openValves, valves, dpDict))
	}

	dpDict.Add(dpKey, maxResult)
	return maxResult

}

type ValveWithIdx struct {
	valve Valve
	idx   int
}

func main() {
	valves := map[string]ValveWithIdx{}
	reader := bufio.NewReader(os.Stdin)
	valveNo := 0
	for {
		var input string
		input, error := reader.ReadString('\n')
		if error != nil {
			if errors.Is(error, io.EOF) {
				break
			}
			panic(error)
		}
		valve, error := parseValve(input)
		valves[valve.name] = ValveWithIdx{valve, valveNo}
		valveNo += 1
	}

	dp, err := lru.New[DpKey, int](10000000)
	if err != nil {
		panic(err)
	}

	ans := getMostPressureReleaseable(30, "AA", 0, valves, dp)

	fmt.Println(ans)
}
