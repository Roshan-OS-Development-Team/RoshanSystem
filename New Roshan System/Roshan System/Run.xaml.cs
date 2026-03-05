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
using System.Windows.Shapes;
using System.Diagnostics;

namespace Roshan_System
{
    /// <summary>
    /// Interaction logic for Run.xaml
    /// </summary>
    public partial class Run : Window
    {
        public Run()
        {
            InitializeComponent();
        }

        private void RunApp(object sender, RoutedEventArgs e)
        {
            if (Appname.Text == "winver")
            {
                winver winver = new winver();
                winver.Show();
            }
            else
            {
                Process.Start($"{Appname.Text}.exe");
            }
        }

        private void CloseApp(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
    }
}
