package hackerrank

func aVeryBigSum(ar []int64) int64 {
	var result int64
	for _, val := range ar {
		result += val
	}
	return result
}
