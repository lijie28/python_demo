def final_coin(n):
    if (n==1):
        return 'finish'
    else:
    	if (n%2==0):
        	print '2'
            x = (n-2)/2
            final_coin(x)
    	else:
        	print '1'
            x = (n-1)/2
            final_coin(x)