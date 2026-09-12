using System.Runtime.InteropServices;

namespace RoshanSystemCoreLib
{
    public static class getDll
    {
        public static string getDllPath()
        {
            if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
            {
                return "RoshanSystemCoreLib.dll";
            }
            else if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
            {
                return "RoshanSystemCoreLib.dynlib";
            }
            else
            {
                return "RoshanSystemCoreLib.so";
            }
        }
    }
}