package main

import (
	"fmt"
	"strconv"
	"strings"
)

var input []int
var elves map[string]int

func main() {
	part := 2
	inputStr := strings.Split("37", "")

	desiredSequence := "286051" // pt2
	numRecipesPractise := 286051

	initialLen := len(inputStr)
	targetLen := initialLen + numRecipesPractise + 20

	for _, c := range inputStr {
		d, _ := strconv.Atoi(c)
		input = append(input, d)
	}

	elves = make(map[string]int)

	elves["a"] = 0
	elves["b"] = 1

	if part == 1 {
		for len(input) < targetLen {
			// for numRecipesCreated < numRecipesIntended {
			createRecipe()
		}

		scoreLastTen := input[numRecipesPractise : numRecipesPractise+10]
		var scoreLastTenReportable string
		for _, d := range scoreLastTen {
			scoreLastTenReportable += strconv.Itoa(d)
		}

		fmt.Println(scoreLastTenReportable)
	} else {
		for true {
			createRecipe()

			sequence := ""
			if len(input) <= 50 {
				continue
			}
			for _, d := range input[len(input)-10 : len(input)-1] {
				c := strconv.Itoa(d)
				sequence += c
			}

			foundSequence := strings.Index(sequence, desiredSequence)
			if foundSequence > 0 {
				fmt.Println(len(input) - 7)
				break
			}
		}
	}

}

func createRecipe() {
	recipe1 := input[elves["a"]]
	recipe2 := input[elves["b"]]

	newRecipe := recipe1 + recipe2

	if newRecipe >= 10 {
		input = append(input, 1)
		input = append(input, newRecipe%10)
	} else {
		input = append(input, newRecipe)
	}

	elves["a"] = step(elves["a"])
	elves["b"] = step(elves["b"])

	// report()
}

func step(currentIndex int) int {
	length := len(input)
	currentScore := input[currentIndex] + 1

	return (currentIndex + currentScore) % length
}

func report() {
	var formatted []string
	for index, score := range input {
		scoreFormatted := strconv.Itoa(score)

		if index == elves["a"] {
			scoreFormatted = "(" + scoreFormatted + ")"
		} else if index == elves["b"] {
			scoreFormatted = "[" + scoreFormatted + "]"
		} else {
			scoreFormatted = " " + scoreFormatted + " "
		}

		formatted = append(formatted, scoreFormatted)
	}

	fmt.Println(strings.Join(formatted, ""))
}
