package hackerrank

func simpleArraySum(ar []int32) int32 {
	var result int32
	for _, num := range ar {
		result += num
	}
	return result
}
