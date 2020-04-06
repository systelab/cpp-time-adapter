#pragma once

#include "../Mocks/MockTimeAdapter.h"


using testing::_;
using testing::Invoke;


namespace systelab { namespace time { namespace test_utility {

	class StubTimeAdapter : public MockTimeAdapter
	{
	public:
		StubTimeAdapter();
		virtual ~StubTimeService();

		std::chrono::system_clock::time_point getCurrentUTCTimeStub() const;
		void addMilliseconds(int milliseconds);
		void setCurrentTime(std::chrono::system_clock::time_point);

	private:
		std::chrono::system_clock::time_point m_currentTime;
	};

}}}
