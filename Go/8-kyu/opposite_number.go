/*
Very simple, given a number, find its opposite (additive inverse).

Examples:

1: -1
14: -14
-34: 34
*/

package main

import "fmt"

func Opposite(value int) int {
	return -value
}

func main() {
	fmt.Println(Opposite(12))
}