using System.Security.AccessControl;
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
using System.Diagnostics;
using System.Threading.Tasks;

namespace Roshan_System
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        bool startmenuopen = false;
        public MainWindow()
        {
            InitializeComponent();
        }

        Startmenu menu = new Startmenu();
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
            MessageBoxResult result = MessageBox.Show("Are you sure you want to shutdown", "Shutdown", MessageBoxButton.YesNo, MessageBoxImage.Warning);
            if (result == MessageBoxResult.Yes)
            {
                Application.Current.Shutdown();
            }
            if (result == MessageBoxResult.No)
            {
                MessageBox.Show("Shutdown Cancelled", "Shutdown", MessageBoxButton.OK, MessageBoxImage.Information);
                return;
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

        private void Open_StartMenu(object sender, RoutedEventArgs e)
        {
            if (startmenuopen)
            {
                MainFrame.Content = null;
            }
            else
            {
                MainFrame.Navigate(menu);
            }
            startmenuopen = !startmenuopen;
        }

        private void Open_Browser(object sender, RoutedEventArgs e)
        {
            Browser browser = new Browser();
            browser.Show();
        }

        private void Open_Terminal(object sender, RoutedEventArgs e)
        {
            Process.Start("wt.exe");
        }

        private void Open_Run(object sender, RoutedEventArgs e)
        {
            Run run = new Run();
            run.Show();
        }

        private void Open_Pong(object sender, RoutedEventArgs e)
        {
            Pong pong = new Pong();
            pong.Show();
        }
    }
}