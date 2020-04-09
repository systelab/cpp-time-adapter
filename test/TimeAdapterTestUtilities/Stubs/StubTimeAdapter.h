#pragma once

#include "../Mocks/MockTimeAdapter.h"


using testing::_;
using testing::Invoke;


namespace systelab { namespace time { namespace test_utility {

	class StubTimeAdapter : public MockTimeAdapter
	{
	public:
		StubTimeAdapter();
		virtual ~StubTimeAdapter();

		std::chrono::system_clock::time_point getCurrentUTCTimeStub() const;
		void setCurrentTime(std::chrono::system_clock::time_point);

		void addMicroseconds(long long microseconds);
		void addMilliseconds(long long milliseconds);
		void addSeconds(long long seconds);
		void addMinutes(long long minutes);
		void addHours(long long hours);

	private:
		std::chrono::system_clock::time_point m_currentTime;
	};

}}}
