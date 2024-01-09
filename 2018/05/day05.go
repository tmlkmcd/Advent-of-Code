package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"unicode"
)

func main() {
	input, err := ioutil.ReadFile("./day05/input.txt")
	part := 2

	if err != nil {
		fmt.Println(err)
	}

	inputSplit := strings.Split(string(input), "")
	var inputRunes []rune

	for _, ch := range inputSplit {
		charRemove := "x"
		if part == 1 || (part == 2 && (ch != charRemove && ch != strings.ToUpper(charRemove))) {
			inputRunes = append(inputRunes, rune(ch[0]))
		}
	}

	fmt.Println(len(inputRunes))

	for true {
		stayedTheSame := true
		var newInputRunes []rune

		for i, r := range inputRunes {
			if r == '-' {
				continue
			}

			if i+1 < len(inputRunes) && isMatch(r, inputRunes[i+1]) {
				inputRunes[i] = '-'
				inputRunes[i+1] = '-'
				stayedTheSame = false
			}
		}

		for _, r := range inputRunes {
			if r != '-' {
				newInputRunes = append(newInputRunes, r)
			}
		}

		inputRunes = newInputRunes

		if stayedTheSame {
			break
		}
	}

	fmt.Println(len(inputRunes))
}

func isMatch(a rune, b rune) bool {
	if unicode.ToUpper(a) == b && unicode.ToLower(b) == a {
		return true
	}

	if unicode.ToUpper(b) == a && unicode.ToLower(a) == b {
		return true
	}

	return false
}
