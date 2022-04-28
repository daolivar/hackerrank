package hackerrank

func hourglassSum(arr [][]int32) int32 {
	var max = int32(-63)
	for i := 0; i < 4; i++ {
		var sum int32
		for j := 0; j < 4; j++ {
			sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
			if max < sum {
				max = sum
			}
		}
	}
	return max
}
