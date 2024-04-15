#include "pch.h"
#include "sqrtutil.h"

double WINAPI c_sqrt(double num)
{
	double x = 1.0;
	for (int i = 0; i < 10; i++) {
		x = (x + (num / x)) * 0.5;
	}
	return x;
}