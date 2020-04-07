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

	std::chrono::system_clock::time_point StubTimeAdapter::getCurrentUTCTimeStub()
	{
		return m_currentTime;
	}

	void StubTimeAdapter::addMilliseconds(int milliseconds)
	{
		m_currentTime = m_currentTime + std::chrono::milliseconds(milliseconds);
	}

	void StubTimeAdapter::setCurrentTime(std::chrono::system_clock::time_point time)
	{
		m_currentTime = time;
	}

}}}
