#include "LoginServer.h"
#include <iostream>
#include <unistd.h>
#include "util.h"
#include "logger.h"

using namespace std;
using namespace loki;

int main(int argc, char** argv)
{
	Global::ParseCommand(argc, argv);
	if (Global::Get<bool>("Daemon"))
	{
		int ret = daemon(1,1);
	}
	InitLog(argv[0]);

	io_service_pool pool(Global::Get<uint32_t>("ThreadNum"));
	auto server(new LoginServer(pool));
	if (server->Init(Global::Get<std::string>("Script")))
		pool.run();
	return 0;
}
