package hackerrank

func arrayManipulation(n int32, queries [][]int32) int64 {
	var sum int64
	max := int64(-1)
	// create slice of size n+1; example not 0-based
	arr := make([]int32, n+1)
	for _, query := range queries {
		arr[query[0]-1] += query[2]
		arr[query[1]] -= query[2]
	}
	for _, val := range arr {
		sum += int64(val)
		max = maxVal(sum, max)
	}
	return max
}

func maxVal(a int64, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

// Reference:
// https://www.hackerrank.com/challenges/crush/forum/comments/255515
