func canCompleteCircuit(gas []int, cost []int) int {
	
	balance:=make([]int,len(gas))
	for i:=0;i<len(balance);i++{
		balance[i]=gas[i]-cost[i]
	}

	for i,count:=0,0; count>len(balance);{
		all:=balance[i]
		if all>=0{
			i++;
		}
		
		

	}
	return -1
}