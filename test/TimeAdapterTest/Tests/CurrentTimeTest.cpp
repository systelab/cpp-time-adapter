#include "stdafx.h"
#include "TimeAdapter/TimeAdapter.h"

#include <chrono>
#include <thread>


using namespace testing;

namespace systelab { namespace time { namespace unit_test {

	class CurrentTimeTest : public Test
	{
	protected:
		TimeAdapter m_timeAdapter;
	};


	TEST_F(CurrentTimeTest, testGetCurrentUTCTimeReturnsGreaterOrEqualTimeOnSecondCall)
	{
		auto currentTime1 = m_timeAdapter.getCurrentUTCTime();
		auto currentTime2 = m_timeAdapter.getCurrentUTCTime();
		ASSERT_GE(currentTime2, currentTime1);
	}

	TEST_F(CurrentTimeTest, testGetCurrentTimeEpochReturnsTime2SecondsGreaterAfterWaiting2Seconds)
	{
		auto currentTime1 = m_timeAdapter.getCurrentUTCTime();
		std::this_thread::sleep_for(std::chrono::seconds(2));
		auto currentTime2 = m_timeAdapter.getCurrentUTCTime();

		auto diffTime = currentTime2 - currentTime1;
		ASSERT_GE(diffTime, std::chrono::seconds(2));
	}

}}}
