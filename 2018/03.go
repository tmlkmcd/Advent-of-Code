package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	input, err := ioutil.ReadFile("./day03/input.txt")
	part := 2

	if err != nil {
		fmt.Println(err)
	}

	squares := strings.Split(string(input), "\n")

	var sqInchesUsed, sqInchesUsedMultiple []string

	var store = make(map[int][]string)
	var store2 = make(map[int]bool)

	for _, sq := range squares {
		id, inchesTaken := parseSquare(sq)

		fmt.Println("Processing ID", id)

		if part == 1 {
			for _, inc := range inchesTaken {
				if contains(sqInchesUsed, inc) && !contains(sqInchesUsedMultiple, inc) {
					sqInchesUsedMultiple = append(sqInchesUsedMultiple, inc)
				} else {
					sqInchesUsed = append(sqInchesUsed, inc)
				}
			}
		} else {
			store[id] = inchesTaken
			store2[id] = false

			for iid, icT := range store {
				for _, pixel := range inchesTaken {
					if iid == id {
						break
					}

					if contains(icT, pixel) {
						store2[iid] = true
						store2[id] = true
					}
				}
			}
		}

	}

	if part == 1 {
		fmt.Println(len(sqInchesUsedMultiple), "square inches used multiple times.")
	} else {
		fmt.Println(store2)
	}
}

func parseSquare(square string) (int, []string) {
	var coordsUsed []string

	stats := strings.Split(square, " ")
	id, _ := strconv.Atoi(strings.Replace(stats[0], "#", "", -1))
	startingCoords := strings.Split(strings.Replace(stats[2], ":", "", -1), ",")
	dim := strings.Split(stats[3], "x")

	x, _ := strconv.Atoi(startingCoords[0])
	y, _ := strconv.Atoi(startingCoords[1])
	w, _ := strconv.Atoi(dim[0])
	h, _ := strconv.Atoi(dim[1])

	for i := y; i <= y+h-1; i++ {
		for j := x; j <= x+w-1; j++ {
			coordsUsed = append(coordsUsed, formatCoord(i, j))
		}
	}

	return id, coordsUsed
}

func contains(list []string, item string) bool {
	for _, i := range list {
		if i == item {
			return true
		}
	}

	return false
}

func formatCoord(x int, y int) string {
	xS := strconv.Itoa(x)
	yS := strconv.Itoa(y)

	if len(xS) == 1 {
		xS = "00" + xS
	} else if len(xS) == 2 {
		xS = "0" + xS
	}

	if len(yS) == 1 {
		yS = "00" + yS
	} else if len(yS) == 2 {
		yS = "0" + yS
	}

	return xS + yS
}
