package main

import (
	"errors"
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

var Directions = [4]Direction{Up, Down, Left, Right}

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

// In which direction should we look to face other
func detectDirectionOfOther(us Position, other Position) (Direction, error) {
	var d Direction
	if us.x == other.x && us.y == other.y {
		return d, errors.New("Same position")
	}
	if us.x == other.x {
		if us.y < other.y {
			return Right, nil
		} else {
			return Left, nil
		}
	} else if us.y == other.y {
		if us.x < other.x {
			return Down, nil
		} else {
			return Up, nil
		}
	} else {
		return d, errors.New("Not in same row or column")
	}
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
	var cords = direction.deltaCord()
	rv.x += cords.x
	rv.y += cords.y
	return rv
}
func (d Direction) deltaCord() Position {
	switch d {
	case Up:
		return Position{-1, 0}
	case Down:
		return Position{1, 0}
	case Left:
		return Position{0, -1}
	case Right:
		return Position{0, 1}
	default:
		panic("Unexpected direction")
	}

}

type CubeFace struct {
	cord   Position
	rows   []string
	left   *CubeFace
	right  *CubeFace
	top    *CubeFace
	bottom *CubeFace
}

func extractCubeRows(rows []string, start Position, size int) []string {
	rv := []string{}
	fmt.Println("Extra cbue", start, size, rows)
	for i := 0; i < size; i++ {
		rv = append(rv, rows[start.x+i][start.y:start.y+size])
	}
	return rv
}

func parseCube(area []string, cubeSize int) CubeFace {
	rows := []string{}
	for _, row := range area {
		rows = append(rows, strings.Trim(row, "\n"))
	}
	var faceStart Position
loop:
	for i, row := range rows {
		for j, val := range row {
			if val != ' ' {
				faceStart = Position{i, j}
				break loop
			}
		}
	}

	var visited = make(map[Position]CubeFace)
	var toVisit = []Position{faceStart}
	// var cube CubeFace
	// cube.rows = extractCubeRows(rows, faceStart, cubeSize)

	for len(toVisit) > 0 {
		current := toVisit[len(toVisit)-1]
		toVisit = toVisit[:len(toVisit)-1]

		var currentCube CubeFace
		currentCube.cord = current
		currentCube.rows = extractCubeRows(rows, current, cubeSize)
		visited[current] = currentCube
		for _, direction := range Directions {
			var next = current
			var cords = direction.deltaCord()
			next.x += cords.x * cubeSize
			next.y += cords.y * cubeSize
			if _, exists := visited[next]; !exists && next.x >= 0 && next.x < len(rows) && next.y >= 0 && next.y < len(rows[next.x]) && rows[next.x][next.y] != ' ' {
				toVisit = append(toVisit, next)
			}
		}
	}

	var visitedCopy = make(map[Position]CubeFace)

	for _, cube := range visited {
		for _, otherCube := range visited {
			for _, direction := range Directions {
				var usCord = cube.cord
				var otherCord = otherCube.cord
				// fmt.Println("Checking", usCord, otherCord, direction)
				usCord.x += direction.deltaCord().x * cubeSize
				usCord.y += direction.deltaCord().y * cubeSize
				if usCord == otherCord {
					fmt.Println("Checking Passssed", cube.cord, otherCord, direction)
					switch direction {
					case Up:
						cube.top = &otherCube
						otherCube.bottom = &cube
					case Down:
						cube.bottom = &otherCube
						otherCube.top = &cube
					case Left:
						cube.left = &otherCube
						otherCube.right = &cube
					case Right:
						cube.right = &otherCube
						otherCube.left = &cube
					}
					// usCord.x -= direction.deltaCord().x * cubeSize
					// usCord.y -= direction.deltaCord().y * cubeSize
					visitedCopy[cube.cord] = cube
					visitedCopy[otherCube.cord] = otherCube
				}
			}
		}
		for _, cube := range visitedCopy {
			fmt.Println("---- =============== ", cube.cord)
			if cube.right != nil {
				fmt.Println("---- Right", cube.right.cord)
			}
			if cube.left != nil {
				fmt.Println("---- Left", cube.left.cord)
			}
			if cube.top != nil {
				fmt.Println("---- Top", cube.top.cord)
			}
			if cube.bottom != nil {
				fmt.Println("---- Bottom", cube.bottom.cord)
			}
		}
	}
	for _, cube := range visitedCopy {
		fmt.Println("=============== ", cube.cord)
		if cube.right != nil {
			fmt.Println("Right", cube.right.cord)
		}
		if cube.left != nil {
			fmt.Println("Left", cube.left.cord)
		}
		if cube.top != nil {
			fmt.Println("Top", cube.top.cord)
		}
		if cube.bottom != nil {
			fmt.Println("Bottom", cube.bottom.cord)
		}
	}
	panic("adf")
}

func (c *CubeFace) getVal(pos Position) (byte, bool) {
	if pos.x < 0 || pos.x >= len(c.rows) {
		return 0, false
	}
	if pos.y < 0 || pos.y >= len(c.rows[pos.x]) {
		return 0, false
	}
	return c.rows[pos.x][pos.y], true
}

func (c *CubeFace) rotated_position(pos Position, clockWiseRotationCount int) byte {
	clockWiseRotationCount %= 4

	if pos.x < 0 || pos.x >= len(c.rows) {
		panic(fmt.Sprintf("Invalid position %v", pos))
	}
	if pos.y < 0 || pos.y >= len(c.rows[pos.x]) {
		panic(fmt.Sprintf("Invalid position %v", pos))
	}
	for i := 0; i < clockWiseRotationCount; i++ {
		pos = Position{pos.y, len(c.rows) - 1 - pos.x}
	}
	return c.rows[pos.x][pos.y]
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

// func (a *Area) cubeTransport(current Position) Position {

// }
/*
 x
 xx
 x
 x
xx


*/

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
	// pos := Position{4, 2}
	// fmt.Println()
	// fmt.Println(area.next(pos, Up))
	// fmt.Println()
	// fmt.Println(area.forward(pos, Up, 7))

	direction := Right
	// currentPosition := Position{0, 50}

	currentPosition := Position{0, 8}
	parseCube(lines[:len(lines)-2], 4)

	area := parseArea(lines[:len(lines)-2])
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
