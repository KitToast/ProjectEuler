#include <stdio.h>
#include <math.h>

void main() {

  int prev = 0;
  int curr = 1;
  double result = 1.0;

  double base = pow(10,1000);
  int index = 0;

  while(1) {
    if((result / base) >= 1.0) {
      printf("%f\n", index);
      break;
    }

    prev = curr;
    curr = result;
    result = prev + curr;
    index++;
  }
}
