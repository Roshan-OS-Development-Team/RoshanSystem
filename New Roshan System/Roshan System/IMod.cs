// Roshan_System.dll - IMod.cs
using HarmonyLib;

namespace Roshan_System.Mods
{
    public interface IMod
    {
        void Start();
        void Patch(HarmonyLib.Harmony harmony);
        ModDetails Details { get; }
    }
}