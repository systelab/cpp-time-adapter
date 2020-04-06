#include "StdAfx.h"
#include "TimeAdapter.h"

namespace systelab { namespace time {

	TimeAdapter::TimeAdapter() = default;
	TimeAdapter::~TimeAdapter() = default;

	std::chrono::time_point TimeAdapter::getCurrentUTCTime() const
	{
		return std::chrono::system_clock::now();
	}

}}
