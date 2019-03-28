
#include <stdio.h>


void main() {

  int accumulate = 0;

  int prev = 0;
  int curr = 1;
  int result = 1;

  while(result < 4000000) {
    if((result % 2) == 0) accumulate += result;

    prev = curr;
    curr = result;
    result = prev + curr;


}

  printf("Sum: %i\n", accumulate);

}
