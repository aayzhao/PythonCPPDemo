#pragma once
#include "pch.h"
#ifdef SQRTUTIL_EXPORTS
#define SQRTUTIL_API __declspec(dllexport)
#else
#define SQRTUTIL_API __declspec(dllimport)
#endif


extern "C" 
{
	SQRTUTIL_API double c_sqrt(double num);
}