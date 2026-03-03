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
    }
}
