package main

import "fmt"

func EachCons(arr []int, n int) [][]int {
	var result [][]int
	for i := 0 ; i+n <= len(arr); i++ {
		value := arr[i : i+n]

		result = append(result, value)
	}
	return result
}

func main() {
	fmt.Println(EachCons([]int{3, 5, 8, 13}, 4))
}
