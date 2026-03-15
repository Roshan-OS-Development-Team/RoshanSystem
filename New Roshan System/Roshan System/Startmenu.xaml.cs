using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Diagnostics;

namespace Roshan_System
{
    /// <summary>
    /// Interaction logic for Startmenu.xaml
    /// </summary>
    public partial class Startmenu : Page
    {
        public Startmenu()
        {
            InitializeComponent();
        }

        private void OpenNotepad(object sender, RoutedEventArgs e)
        {
            Notepad notepad = new Notepad();
            notepad.Show();
        }

        private void OpenCalculator(object sender, RoutedEventArgs e)
        {
            Calculator calculator = new Calculator();
            calculator.Show();
        }

        private void OpenChilli(object sender, RoutedEventArgs e)
        {
            Chilli chilli = new Chilli();
            chilli.Show();
        }

        private void OpenOverclocker(object sender, RoutedEventArgs e)
        {
            Overclocker overclocker = new Overclocker();
            overclocker.Show();
        }

        private void Shutdown1(object sender, RoutedEventArgs e)
        {
            MessageBoxResult result = MessageBox.Show("Are you sure you want to shutdown", "Shutdown", MessageBoxButton.YesNo, MessageBoxImage.Warning);
            if (result == MessageBoxResult.Yes)
            {
                Application.Current.Shutdown();
            }
            if (result == MessageBoxResult.No)
            {
                MessageBox.Show("Shutdown Cancelled", "Shutdown", MessageBoxButton.OK, MessageBoxImage.Information);
            }    
        }

        private void OpenBrowser(object sender, RoutedEventArgs e)
        {
            Browser browser = new Browser();
            browser.Show();
        }

        private void OpenTerminal(object sender, RoutedEventArgs e)
        {
            Process.Start("wt.exe");
        }

        private void OpenRun(object sender, RoutedEventArgs e)
        {
            Run run = new Run();
            run.Show();
        }

        private void OpenPong(object sender, RoutedEventArgs e)
        {
            Pong pong = new Pong();
            pong.Show();
        }

        private void OpenModList(object sender, RoutedEventArgs e)
        {
            ModList modList = new ModList();
            modList.Show();
        }
    }
}
