#include "TimeAdapter.h"


namespace systelab { namespace time {

	TimeAdapter::TimeAdapter() = default;
	TimeAdapter::~TimeAdapter() = default;

	std::chrono::system_clock::time_point TimeAdapter::getCurrentUTCTime() const
	{
		return std::chrono::system_clock::now();
	}

}}
