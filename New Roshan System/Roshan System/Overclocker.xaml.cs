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

namespace Roshan_System
{
    /// <summary>
    /// Interaction logic for Overclocker.xaml
    /// </summary>
    public partial class Overclocker : Window
    {
        public double cs = 1;
        public Overclocker()
        {
            InitializeComponent();
            cslabel.Content = cs;
        }

        private void Add(object sender, RoutedEventArgs e)
        {
            cs += 0.1;
            cslabel.Content = cs;
            if (cs >= 2)
            {
                MessageBoxResult message = MessageBox.Show("Your PC crashed", "Crashed", MessageBoxButton.OK);
                if (message != MessageBoxResult.OK)
                {
                    Application.Current.Shutdown();
                }
                else
                {
                    Application.Current.Shutdown();
                }
            }
        }

        private void Subtract(object sender, RoutedEventArgs e)
        {
            cs -= 0.1;
            cslabel.Content = cs;
            if (cs <= 0.5)
            {
                MessageBoxResult message = MessageBox.Show("Your PC crashed", "Crashed");
                if (message != MessageBoxResult.OK)
                {
                    Application.Current.Shutdown();
                }
                else
                {
                    Application.Current.Shutdown();
                }
            }
        }
    }
}
