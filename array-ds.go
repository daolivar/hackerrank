package hackerrank

func reverseArray(a []int32) []int32 {
	j := len(a) - 1
	for i := 0; i < len(a)/2; i++ {
		temp := a[i]
		a[i] = a[j]
		a[j] = temp
		j--
	}
	return a
}

// Alternative approach
func reverseArray(a []int32) []int32 {
	i := 0
	j := len(a) - 1
	for i < j {
		temp := a[i]
		a[i] = a[j]
		a[j] = temp
		i++
		j--
	}
	return a
}
