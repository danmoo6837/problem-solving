#include <stdio.h>

int main(){
	int n,cnt=0;
	scanf("%d", &n);
	int num[n];

	for(int i=0;i<n;i++) {
		scanf("%d", &num[i]);
		cnt++;
		if(num[i]==1) {
			cnt--;
			continue;
		}
		for(int j=2;j<num[i];j++) {
			if(num[i]%j==0) {
				cnt--;
				break;
			}
		}	
	}
	printf("%d", cnt);
	return 0;
}