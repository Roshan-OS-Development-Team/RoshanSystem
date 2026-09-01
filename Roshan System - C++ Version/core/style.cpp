//
// Created by Roshan on 31/08/2026.
//

#include "style.h"

#include <iostream>

namespace core
{
    std::map<std::string, std::string> get_qss_styles(std::string filepath)
    {
        fs::path targetPath = filepath;
        std::map<std::string, std::string> styles;

        for (const auto& entry: fs::directory_iterator(targetPath))
        {
            if (!entry.is_directory())
            {
                std::ifstream styleFile(entry.path());
                std::string fileContents;

                if (styleFile.is_open())
                {
                    std::getline(styleFile, fileContents, '\0');
                    styleFile.close();
                }

                styles[entry.path().filename().stem().string()] = fileContents;
            }
        }

        return styles;
    }
}