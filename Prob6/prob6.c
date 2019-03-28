#include <stdio.h>

void main() {


int sos1 = 0;
for(int i = 1 ; i < 101 ; i++) {
  sos1 += i*i;
}

printf("Difference: %i\n",sos1 - (50 * 101)*(50 * 101));

}
