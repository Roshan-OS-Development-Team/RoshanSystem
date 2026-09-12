//
// Created by Roshan on 31/08/2026.
//

#include "style.h"

namespace core
{
    std::map<std::string, std::string> get_qss_styles(std::string filepath)
    {
        fs::path settingspath = "settings.json";
        json settingsJSON;
        if (exists(settingspath) && fs::file_size(settingspath) > 0)
        {

            std::ifstream settingsFile(settingspath);
            if (settingsFile.is_open())
            {
                settingsJSON = json::parse(settingsFile);
            }
        }
        else
        {
            settingsJSON = {
                {"theme", "dark"}
            };
        }
        fs::path targetPath = filepath;

        if (!settingsJSON["theme"].get<std::string>().empty())
        {
            targetPath /= settingsJSON["theme"].get<std::string>();
        }

        std::map<std::string, std::string> styles;

        for (const auto& entry: fs::directory_iterator(targetPath))
        {
            if (entry.is_regular_file())
            {
                std::ifstream styleFile(entry.path());
                std::string fileContents;
                std::stringstream fileBuffer;

                if (styleFile.is_open())
                {
                    fileBuffer << styleFile.rdbuf();
                    fileContents = fileBuffer.str();
                    styles[entry.path().filename().stem().string()] = fileContents;
                    styleFile.close();
                }
            }
        }

        return styles;
    }
}

ROSHANSYSTEMLIB_API const char* get_qss_styles(const char* filepath)
{
    json qss_styles = core::get_qss_styles(std::string(filepath));
    static thread_local std::string buffer;
    buffer = qss_styles.dump();
    return buffer.c_str();
}
