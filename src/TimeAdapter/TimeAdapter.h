#pragma once

#include "ITimeAdapter.h"


namespace systelab { namespace time {

	class TimeAdapter : public ITimeAdapter
	{
	public:
		TimeAdapter();
		virtual ~TimeAdapter();

		std::chrono::time_point getCurrentUTCTime() const override;
	};

}}
