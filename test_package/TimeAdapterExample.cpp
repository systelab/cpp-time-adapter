#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <sstream>
#include <stdexcept>

#include "TimeAdapter/TimeAdapter.h"


int main(int argc, char *argv[])
{
	auto now = systelab::time::TimeAdapter().getCurrentUTCTime();
	std::cout << "Current UTC Time: " << now << std::endl;
    return 0;
}
