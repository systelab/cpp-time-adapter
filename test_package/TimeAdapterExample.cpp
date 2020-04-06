#include <iostream>
#include <iomanip>
#include <ctime>
#include <chrono>

#include "TimeAdapter/TimeAdapter.h"


int main(int argc, char *argv[])
{
    auto now = systelab::time::TimeAdapter().getCurrentUTCTime();
    auto now_time_t = std::chrono::system_clock::to_time_t(now);
    std::cout << "Current UTC Time: " << std::put_time(std::localtime(&now_time_t), "%F %T") << std::endl;

    return 0;
}
