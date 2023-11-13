package main

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
)

type MonkeySpeak interface {
	getValue(cache map[string]int, monkeys map[string]MonkeySpeak, targetNo int) (int, error)
}

type Numeric struct {
	value int
	name  string
}

func (n Numeric) getValue(cache map[string]int, monkeys map[string]MonkeySpeak, targetNo int) (int, error) {
	if n.name == "humn" {
		return 3378273370680, nil
		fmt.Println("Asked for humn", targetNo)
		return targetNo, errors.New("Hey")
		// panic("Asked for humn")
	}
	return n.value, nil
}

type Expr struct {
	left  string
	right string
	op    string
	name  string
}

func (e Expr) getValue(cache map[string]int, monkeys map[string]MonkeySpeak, targetNo int) (int, error) {
	cacheValue, exists := cache[e.name]
	if exists {
		return cacheValue, nil
	}

	l, lContainsHuman := monkeys[e.left].getValue(cache, monkeys, 999999999999)
	r, rContainsHuman := monkeys[e.right].getValue(cache, monkeys, 999999999999)
	var nextTargetNo int
	var result int
	if targetNo == 999999999999 && (lContainsHuman != nil || rContainsHuman != nil) {
		return 0, errors.New("Hey")
	}
	if lContainsHuman != nil {
		switch e.op {
		case "+":
			nextTargetNo = targetNo - r
		case "*":
			nextTargetNo = targetNo / r
		case "-":
			nextTargetNo = targetNo + r
		case "/":
			nextTargetNo = targetNo * r
		}
	} else if rContainsHuman != nil {
		switch e.op {
		case "+":
			nextTargetNo = targetNo - l
		case "*":
			nextTargetNo = targetNo / l
		case "-":
			nextTargetNo = l - targetNo
		case "/":
			nextTargetNo = l / targetNo
		}
	}

	if rContainsHuman != nil {
		monkeys[e.right].getValue(cache, monkeys, nextTargetNo)
		return 0, errors.New("Hey")
	} else if lContainsHuman != nil {
		monkeys[e.left].getValue(cache, monkeys, nextTargetNo)
		return 0, errors.New("Hey")
	} else {
		switch e.op {
		case "+":
			result = l + r
		case "*":
			result = l * r
		case "-":
			result = l - r
		case "/":
			result = l / r
		}
		cache[e.name] = result
		return result, nil
	}
}

func parseMonkey(line string) MonkeySpeak {
	name := line[0:4]
	rest := line[6:]
	if strings.Count(rest, " ") == 0 {
	}

	splits := strings.Split(strings.Trim(rest, " \n"), " ")
	if len(splits) == 1 {
		value, error := strconv.Atoi(strings.Trim(rest, " \n"))
		if error != nil {
			panic(error)
		}

		return Numeric{value: value, name: name}
	}

	left := splits[0]
	ops := splits[1]
	right := splits[2]
	return Expr{left: left, right: right, op: ops, name: name}

}

func d21() {
	lines := readAllInput()
	monkeys := make(map[string]MonkeySpeak)
	for _, line := range lines {
		monkeys[line[0:4]] = parseMonkey(line)
	}
	cache := make(map[string]int)
	leftMonkey := monkeys[monkeys["root"].(Expr).left]
	rightMonkey := monkeys[monkeys["root"].(Expr).right]
	fmt.Println(rightMonkey.getValue(cache, monkeys, 109255486022220))
	// 109255486022220
	fmt.Println(leftMonkey.getValue(cache, monkeys, 109255486022220))
}
