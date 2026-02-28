using System.Text;
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
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Open_Notepad(object sender, RoutedEventArgs e)
        {
            Notepad notepad = new Notepad();
            notepad.Show();
        }

        private void Open_Calculator(object sender, RoutedEventArgs e)
        {
            Calculator calculator = new Calculator();
            calculator.Show();
        }
        
        private void Shutdown(object sender, RoutedEventArgs e)
        {
            MessageBoxResult result = MessageBox.Show("Are you sure you want to shutdown?", "Confirm Shutdown", MessageBoxButton.YesNo);
            if (result == MessageBoxResult.Yes)
            {
                Application.Current.Shutdown();
            }
            if (result == MessageBoxResult.No)
            {
                MessageBox.Show("Shutdown cancelled.");
            }
        }

        private void Open_Chilli(object sender, RoutedEventArgs e)
        {
            Chilli chilli = new Chilli();
            chilli.Show();
        }

        private void Open_Overclocker(object sender, RoutedEventArgs e)
        {
            Overclocker overclocker = new Overclocker();
            overclocker.Show();
        }
    }
}