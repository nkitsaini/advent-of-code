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
	timeLeft      int
	currentValve  string
	elephantValve string

	openList int64
}

// Only returns how many additional pressure is released except for the currently open ones
func getMostPressureReleaseable(timeLeft int, currentValve string, elephantValve string, openValves int64, valves map[string]ValveWithIdx, dpDict *lru.Cache[DpKey, int], nonHelpful map[string]bool) int {
	// println("==================", timeLeft, currentValve)
	if timeLeft <= 0 {
		// fmt.Println("Returning using time")
		return 0
	}
	if openValves == int64(math.Pow(2, float64(len(valves))))-1 {
		// fmt.Println("Returning using openValves")
		return 0
	}

	dpKey := DpKey{timeLeft, currentValve, elephantValve, openValves}
	value, exists := dpDict.Get(dpKey)
	if exists {
		return value
	}

	maxResult := 0
	cr := valves[currentValve]
	er := valves[elephantValve]

	myOptions := append(cr.valve.ends, "<NA>")
	elOptions := append(er.valve.ends, "<NA>")
	for _, myOpt := range myOptions {
		if nonHelpful[myOpt] {
			continue
		}
		opens := openValves
		nextPosition := myOpt
		additionalPressure := 0
		if myOpt == "<NA>" {
			nextPosition = currentValve
			if (1<<cr.idx)&opens == 0 && cr.valve.flow_rate != 0 { // not open yet
				additionalPressure += (timeLeft - 1) * cr.valve.flow_rate
				opens += 1 << cr.idx
			} else {
				continue
			}
		}
		for _, elOpt := range elOptions {
			nextPositionElphant := elOpt
			if elOpt == "<NA>" {
				nextPositionElphant = elephantValve
				if (1<<er.idx)&opens == 0 && er.valve.flow_rate != 0 { // not open yet
					additionalPressure += (timeLeft - 1) * er.valve.flow_rate
					opens += 1 << er.idx
				} else {
					continue
				}
			}
			if nonHelpful[elOpt] && myOpt != "<NA>" {
				continue
			}
			maxResult = max(maxResult,
				getMostPressureReleaseable(timeLeft-1, nextPosition, nextPositionElphant, opens, valves, dpDict, nonHelpful)+additionalPressure)

		}
	}

	dpDict.Add(dpKey, maxResult)
	return maxResult

}

type ValveWithIdx struct {
	valve Valve
	idx   int
}

func findNonHelpfulValves(valves map[string]ValveWithIdx) map[string]bool {
	nonHelpful := map[string]bool{}
	var totalBenefit func(valve string, visited map[string]bool) int
	totalBenefit = func(valve string, visited map[string]bool) int {
		isVisited := visited[valve]
		if isVisited {
			return 0
		}
		if valve == "AA" {
			return -1000000000
		}
		// fmt.Println("Novisited", valve)
		visited[valve] = true
		rv := valves[valve].valve.flow_rate
		for _, end := range valves[valve].valve.ends {
			if !visited[end] {
				rv += totalBenefit(end, visited)
			}
		}
		visited[valve] = false
		return rv
	}
	visited := map[string]bool{}
	for valveName, valve := range valves {
		fmt.Println("Checking", valveName)
		isNonHelpful := true
		if valve.valve.flow_rate > 0 {
			continue
		}
		visited[valveName] = true
		totalNeg := 0
		for _, end := range valve.valve.ends {
			benefit := totalBenefit(end, visited)
			fmt.Println("Trying Branch", end, benefit)
			if benefit < 0 {
				totalNeg += 1
			}
			if benefit > 0 {
				isNonHelpful = false
			}
			if benefit == 0 {
				println("ZeroBenefit", end, valveName)
			}
		}
		visited[valveName] = false
		if isNonHelpful && totalNeg <= 1 {
			println("NonHelpful", valveName)
			nonHelpful[valveName] = true
		}
	}

	return nonHelpful
}

func readAllInput() []string {
	// reader := bufio.NewReader(os.Stdin)
	f, err := os.Open("d22_data_small")
	if err != nil {
		panic(err)
	}
	reader := bufio.NewReader(f)
	rv := []string{}
	for {
		var input string
		input, error := reader.ReadString('\n')
		if error != nil {
			if errors.Is(error, io.EOF) {
				break
			}
			panic(error)
		}
		rv = append(rv, input)
	}
	return rv
}

func d16() {
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
	fmt.Println("Started")
	if err != nil {
		panic(err)
	}

	nonHelpful := findNonHelpfulValves(valves)
	fmt.Println(nonHelpful)
	ans := getMostPressureReleaseable(26, "AA", "AA", 0, valves, dp, nonHelpful)

	fmt.Println(ans)
}

func main() {
	// d21()
	d22()
}
