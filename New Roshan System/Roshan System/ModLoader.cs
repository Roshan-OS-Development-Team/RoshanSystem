using System;
using System.IO;
using System.Reflection;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows;
using HarmonyLib;

namespace Roshan_System.Mods
{
    public static class ModLoader
    {
        private static Harmony harmony;

        public static void LoadMods(StackPanel modListPanel)
        {
            harmony = new Harmony("Roshan_System.Mods.Harmony");

            string modFolder = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Mods");
            if (!Directory.Exists(modFolder))
                Directory.CreateDirectory(modFolder);

            foreach (string dllFile in Directory.GetFiles(modFolder, "*.dll"))
            {
                try
                {
                    Assembly assembly = Assembly.LoadFrom(dllFile);

                    foreach (Type type in assembly.GetTypes())
                    {
                        if (typeof(IMod).IsAssignableFrom(type) && !type.IsInterface)
                        {
                            IMod mod = (IMod)Activator.CreateInstance(type);

                            // Apply Harmony patches if available
                            mod.Patch(harmony);

                            // Run the mod
                            mod.Start();

                            // Display mod info in UI
                            DisplayModInfo(modListPanel, mod);
                        }
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Failed to load mod DLL: {dllFile}\n{ex.Message}");
                }
            }
        }

        private static void DisplayModInfo(StackPanel panel, IMod mod)
        {
            if (mod.Details == null) return;

            TextBlock textBlock = new TextBlock
            {
                Text = $"Name: {mod.Details.Name}\n" +
                       $"Author: {mod.Details.Author}\n" +
                       $"Version: {mod.Details.Version}\n" +
                       $"Description: {mod.Details.Description}",
                Foreground = Brushes.White,
                FontSize = 14,
                TextWrapping = TextWrapping.Wrap,
                Margin = new Thickness(5),
                Padding = new Thickness(5)
            };

            Border border = new Border
            {
                CornerRadius = new CornerRadius(5),
                Background = new SolidColorBrush(Color.FromRgb(35, 35, 35)),
                BorderBrush = Brushes.Gray,
                BorderThickness = new Thickness(1),
                Padding = new Thickness(5),
                Margin = new Thickness(3),
                Child = textBlock
            };

            panel.Children.Add(border);
        }
    }
}