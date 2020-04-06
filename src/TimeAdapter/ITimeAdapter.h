#pragma once

#include <iostream>
#include <vector>
#include <numeric>
#include <chrono>


namespace systelab { namespace time {

	class ITimeAdapter
	{
	public:
		virtual ~ITimeAdapter() = default;

		virtual std::chrono::system_clock::time_point getCurrentUTCTime() const = 0;
	};

}}
