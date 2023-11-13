package main

import (
	"fmt"
	"strconv"
	"strings"
	// "strings"
)

type Turn string
type Steps int
type Direction int

const (
	Right Direction = iota
	Down
	Left
	Up
)

func (d Direction) reverse() Direction {
	switch d {
	case Up:
		return Down
	case Down:
		return Up
	case Left:
		return Right
	case Right:
		return Left
	}
	panic("Invalid direction")
}

func (d Direction) right() Direction {
	switch d {
	case Up:
		return Right
	case Down:
		return Left
	case Left:
		return Up
	case Right:
		return Down
	}
	panic("Invalid direction")
}
func (d Direction) left() Direction {
	switch d {
	case Up:
		return Left
	case Down:
		return Right
	case Left:
		return Down
	case Right:
		return Up
	}
	panic("Invalid direction")
}

type Position struct {
	x int
	y int
}

func (p Position) neighbour(direction Direction) Position {
	var rv Position = p
	switch direction {
	case Up:
		rv.x -= 1
	case Down:
		rv.x += 1
	case Left:
		rv.y -= 1
	case Right:
		rv.y += 1
	}

	return rv

}

type Area struct {
	rows []string
}

func parseArea(area []string) Area {
	rows := []string{}
	for _, row := range area {
		rows = append(rows, strings.Trim(row, "\n"))
	}
	return Area{rows}
}

func (a *Area) get(pos Position) (byte, bool) {
	if pos.x < 0 || pos.x >= len(a.rows) {
		return 0, false
	} else if pos.y < 0 || pos.y >= len(a.rows[pos.x]) {
		return 0, false
	}
	return a.rows[pos.x][pos.y], true
}

func (a *Area) next(current Position, direction Direction) Position {
	var neighbor = current.neighbour(direction)
	nValue, ok := a.get(neighbor)
	fmt.Println("Neighbour", neighbor, nValue, ok)
	if ok && nValue != ' ' {
		return neighbor
	} else {
		nValue, ok := a.get(current)
		fmt.Println("Wrapping around", current, nValue, ok, a.rows[current.x])
		if !ok || nValue == ' ' {
			panic("Can't get next of invalid location")
		}
		for nValue != ' ' && ok {
			neighbor = neighbor.neighbour(direction.reverse())
			nValue, ok = a.get(neighbor)
		}
		return neighbor.neighbour(direction)
	}
}

func (a *Area) forward(current Position, direction Direction, count int) Position {
	for i := 0; i < count; i++ {
		next := a.next(current, direction)
		rv, ok := a.get(next)
		if !ok {
			panic("Invalid next value")
		}
		if rv == '#' {
			return current
		}
		if rv != '.' {
			fmt.Println(rv, "current value")
			panic("Invalid current value")
		}
		current = next
	}
	return current
}

func parseInstructions(instructions string) []interface{} {
	digits := ""

	result := []interface{}{}

	consumeDigits := func() {
		if digits != "" {
			num, err := strconv.Atoi(strings.Trim(digits, "\n "))
			if err != nil {
				panic(err)
			}
			result = append(result, Steps(num))
			digits = ""
		}

	}
	for _, char := range instructions {
		if char == 'R' {
			consumeDigits()
			result = append(result, Turn('R'))
		} else if char == 'L' {
			consumeDigits()
			result = append(result, Turn('L'))
		} else {
			digits += string(char)
		}
	}
	consumeDigits()
	return result
}

func d22() int {
	lines := readAllInput()
	instructions := parseInstructions(lines[len(lines)-1])
	area := parseArea(lines[:len(lines)-2])
	// pos := Position{4, 2}
	// fmt.Println()
	// fmt.Println(area.next(pos, Up))
	// fmt.Println()
	// fmt.Println(area.forward(pos, Up, 7))

	direction := Right
	currentPosition := Position{0, 50}

	// currentPosition := Position{0, 8}

	for _, instruct := range instructions {
		fmt.Println(instruct, direction, currentPosition)
		switch instruct.(type) {
		case Turn:
			if instruct.(Turn) == "R" {
				direction = direction.right()
			} else if instruct.(Turn) == "L" {
				direction = direction.left()
			} else {
				panic("Invalid direction")
			}
		case Steps:
			currentPosition = area.forward(currentPosition, direction, int(instruct.(Steps)))
		default:
			panic("Unknown instruct")
		}
	}

	fmt.Println(direction, currentPosition)
	fmt.Println(1000*(currentPosition.x+1) + 4*(currentPosition.y+1) + int(direction))

	return 0

}
