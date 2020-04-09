#include "stdafx.h"
#include "StubTimeAdapter.h"


using testing::_;
using testing::Invoke;

namespace systelab { namespace time { namespace test_utility {

	StubTimeAdapter::StubTimeAdapter()
	{
		m_currentTime = std::chrono::system_clock::now();
		ON_CALL(*this, getCurrentUTCTime()).WillByDefault(Invoke(this, &StubTimeAdapter::getCurrentUTCTimeStub));
	}

	StubTimeAdapter::~StubTimeAdapter() = default;

	std::chrono::system_clock::time_point StubTimeAdapter::getCurrentUTCTimeStub() const
	{
		return m_currentTime;
	}

	void StubTimeAdapter::setCurrentTime(std::chrono::system_clock::time_point time)
	{
		m_currentTime = time;
	}

	void StubTimeAdapter::addMicroseconds(long long milliseconds)
	{
		m_currentTime = m_currentTime + std::chrono::microseconds(milliseconds);
	}

	void StubTimeAdapter::addMilliseconds(long long milliseconds)
	{
		m_currentTime = m_currentTime + std::chrono::milliseconds(milliseconds);
	}

	void StubTimeAdapter::addSeconds(long long seconds)
	{
		m_currentTime = m_currentTime + std::chrono::seconds(seconds);
	}

	void StubTimeAdapter::addMinutes(long long minutes)
	{
		m_currentTime = m_currentTime + std::chrono::minutes(minutes);
	}

	void StubTimeAdapter::addHours(long long hours)
	{
		m_currentTime = m_currentTime + std::chrono::hours(hours);
	}

}}}
