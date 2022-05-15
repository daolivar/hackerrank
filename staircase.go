package hackerrank

import "fmt"

func staircase(n int32) {
	var numHash int32 = n
	for i := int32(0); i < n; i++ {
		for j := int32(0); j < n; j++ {
			if j < numHash-i-1 {
				fmt.Print(" ")
			} else {
				fmt.Print("#")
			}
		}
		fmt.Println()
	}
}
