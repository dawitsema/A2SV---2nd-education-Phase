func luckyNumbers (matrix [][]int) []int {
    var ans []int

    for i := 0; i < len(matrix); i++{
        for j := 0; j < len(matrix[0]); j++{
            maxx := matrix[i][j]
            minn := matrix[i][j]
            for k := 0; k < len(matrix); k++{
                if matrix[k][j] > maxx{
                    maxx = matrix[k][j]
                }
            }

            for k := 0; k < len(matrix[0]); k++{
                if matrix[i][k] < minn{
                    minn = matrix[i][k]
                }
            }

            if minn == maxx {
                ans = append(ans, minn)
            }

            
        }
    }

    return ans
}