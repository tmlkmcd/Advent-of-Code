package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {

	input, err := ioutil.ReadFile("./day12/input.txt")
	part := 2

	if err != nil {
		fmt.Println(err)
	}

	inputSplit := strings.Split(string(input), "\n")

	initial := strings.Split(inputSplit[0], " ")[2]
	currentState := strings.Split(initial, "")

	instructionsString := inputSplit[2:]
	var instructions [][]string

	for _, s := range instructionsString {
		instructions = append(instructions, strings.Split(s, " => "))
	}

	currentState = append([]string{".", ".", ".", ".", ".", ".", ".", ".", ".", "."}, currentState...)
	currentState = append(currentState, []string{".", ".", ".", ".", "."}...)

	fmt.Println(currentState)

	iterations := 1
	if part == 1 {
		iterations = 20
	}

	var combinationSeen []string

	for iterations > 0 {
		var newState []string
		for i, char := range currentState {
			if i < 2 {
				newState = append(newState, char)
				continue
			}

			ll := currentState[i-2]
			l := currentState[i-1]
			n := char
			var r, rr string

			if i+1 >= len(currentState) {
				r = "."
			} else {
				r = currentState[i+1]
			}

			if i+2 >= len(currentState) {
				rr = "."
			} else {
				rr = currentState[i+2]
			}

			sequence := ll + l + n + r + rr
			newChar := getResult(sequence, instructions)

			newState = append(newState, newChar)
		}

		lenState := len(currentState)
		if currentState[lenState-1] == "#" ||
			currentState[lenState-2] == "#" ||
			currentState[lenState-3] == "#" ||
			currentState[lenState-4] == "#" ||
			currentState[lenState-5] == "#" ||
			currentState[lenState-6] == "#" ||
			currentState[lenState-7] == "#" ||
			currentState[lenState-8] == "#" ||
			currentState[lenState-9] == "#" ||
			currentState[lenState-10] == "#" {
			newState = append(newState, ".")
		}

		newStateJoined := strings.Join(newState, "")

		// this approach does not work
		if part == 2 && contains(combinationSeen, newStateJoined) {
			fmt.Println("Took", iterations, "iterations to see a repeat")
			break
		} else {
			fmt.Println("Have not yet seen", newStateJoined)
			combinationSeen = append(combinationSeen, newStateJoined)
		}

		currentState = newState
		if part == 1 {
			iterations--
		} else {
			// pt 2 we count upward iterations
			iterations++
		}

		if iterations > 150 {
			break
		}

		total := 0

		for index, hasPlant := range currentState {
			if hasPlant == "#" {
				total += (index - 10)
			}
		}

		// part 2 answer - score is simply going up by 5 each iteration. so the answer is just to multiply it up.
		fmt.Println(total)
	}
}

func getResult(sequence string, instructions [][]string) string {
	for _, i := range instructions {
		if i[0] == sequence {
			return i[1]
		}
	}

	return "."
}

func contains(combinations []string, newCombo string) bool {
	for _, combo := range combinations {
		findSequence := trimPots(combo)

		if strings.Index(newCombo, findSequence) != strings.Index(newCombo, findSequence) {
			return true
		}
	}

	return false
}

func trimPots(combo string) string {
	trimmed := strings.Trim(combo, ".")
	return trimmed
}
