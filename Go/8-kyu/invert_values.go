/*
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
You can assume that all values are integers. Do not mutate the input array.
*/

package main

import "fmt"

func Invert(arr []int) [] int {
	var result []int

	for i := 0; i < len(arr); i++ {
		value := -arr[i]

		result = append(result, value)
	}

	return result
}

func main() {
	fmt.Println(Invert([]int{1,2,3,4,5}))
}