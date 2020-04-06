#pragma once

#include <chrono>


namespace systelab { namespace time {

	class ITimeAdapter
	{
	public:
		virtual ~ITimeAdapter() = default;

		virtual std::chrono::time_point getCurrentUTCTime() const = 0;
	};

}}
