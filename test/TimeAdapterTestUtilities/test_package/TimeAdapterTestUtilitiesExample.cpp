#define _SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING  1

#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include <iostream>

#include "TimeAdapterTestUtilities/Mocks/MockTimeAdapter.h"


int main(int argc, char *argv[])
{
	systelab::time::test_utility::MockTimeAdapter timeAdapter;
    std::cout << "TimeAdapter test utilities work as expected" << std::endl;

    return 0;
}
