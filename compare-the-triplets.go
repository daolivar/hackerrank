package hackerrank

func compareTriplets(a []int32, b []int32) []int32 {
	var aPts int32 = 0
	var bPts int32 = 0
	for i := 0; i < len(a); i += 3 {
		updateScores(a[i], b[i], &aPts, &bPts)
		updateScores(a[i+1], b[i+1], &aPts, &bPts)
		updateScores(a[i+2], b[i+2], &aPts, &bPts)
	}
	return []int32{aPts, bPts}
}

func updateScores(aRating int32, bRating int32, aPoints *int32, bPoints *int32) {
	if aRating != bRating {
		if aRating > bRating {
			*aPoints++
		} else {
			*bPoints++
		}
	}
}
