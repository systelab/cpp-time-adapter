#pragma once

#include "TimeAdapter/ITimeAdapter.h"


namespace systelab { namespace time { namespace test_utility {

	class MockTimeAdapter : public ITimeAdapter
	{
	public:
		MockTimeAdapter();
		virtual ~MockTimeAdapter();

		MOCK_CONST_METHOD0(getCurrentUTCTime, std::chrono::system_clock::time_point());
	};

}}}

