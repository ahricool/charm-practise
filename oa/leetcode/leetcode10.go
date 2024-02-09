package main

func isMatch(s string, p string) bool {
	
	// init the dp array
	dp:=make([][]bool,len(s)+1)
	for i:=0;i<len(s);i++{
		dp[i]=make([]bool,len(p)+1)
	}

	for i:=0;i<len(dp);i++{
		dp[i][0]=true
	}

	for j:=0;j<len(dp[0]);j++{
		dp[j][0]=true
	}

	for i:=1;i<len(dp);i++{
		for j:=1;j<len(dp[0]);j++{
			if (dp[j])


			if p[j-1]=="."{
				dp[i][j]=true
			}
		}
	}
	
	return dp[len(dp)-1][len(dp[0])-1]



}