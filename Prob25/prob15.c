#include <stdio.h>
#include <math.h>

void main() {

  double prev = 0.0;
  double curr = 1.0;
  double result = 1.0;

  double base = pow(10,200);
  int index = 0;
  int digitShift = 0;

  while(digitShift < 5) {

    if((result / base) >= 1.0) {
      digitShift++;
      result = result / base;
    }

    prev = curr;
    curr = result;
    result = prev + curr;

    index++;
  }

  printf("%i",index);
}
