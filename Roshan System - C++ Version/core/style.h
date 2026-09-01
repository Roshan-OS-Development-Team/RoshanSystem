//
// Created by Roshan on 31/08/2026.
//

#include <fstream>
#include <string>
#include <map>
#include <filesystem>

namespace fs = std::filesystem;

#ifndef ROSHANSYSTEM_STYLE_H
#define ROSHANSYSTEM_STYLE_H
namespace core
{
    std::map<std::string, std::string> get_qss_styles(std::string filepath);
}
#endif //ROSHANSYSTEM_STYLE_H
