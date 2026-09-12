//
// Created by Roshan on 31/08/2026.
//

#include <fstream>
#include <string>
#include <map>
#include <filesystem>
#include <nlohmann/json.hpp>
#include <sstream>

namespace fs = std::filesystem;
using json = nlohmann::json;

#ifdef RoshanSystemCoreLib_EXPORTS
#define ROSHANSYSTEMLIB_API __declspec(dllexport)
#else
#define ROSHANSYSTEMLIB_API __declspec(dllimport)
#endif


#ifndef ROSHANSYSTEM_STYLE_H
#define ROSHANSYSTEM_STYLE_H
namespace core
{
    std::map<std::string, std::string> get_qss_styles(std::string filepath);
}

extern "C" {
ROSHANSYSTEMLIB_API const char *get_qss_styles(const char *filepath);
}
#endif //ROSHANSYSTEM_STYLE_H
