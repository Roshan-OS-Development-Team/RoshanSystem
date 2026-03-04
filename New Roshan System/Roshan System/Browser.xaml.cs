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
    /// Interaction logic for Browser.xaml
    /// </summary>
    public partial class Browser : Window
    {
        public Browser()
        {
            InitializeComponent();
            WebView.Source = new Uri("https://www.google.com");
        }

        private void Goback(object sender, RoutedEventArgs e)
        {
            if (WebView.CanGoBack)
                WebView.GoBack();
        }

        private void Goforward(object sender, RoutedEventArgs e)
        {
            if (WebView.CanGoForward)
                WebView.GoForward();
        }

        private void Navigate(object sender, RoutedEventArgs e)
        {
            string url = Urlbox.Text;
            if (!url.StartsWith("http"))
                url = "https://" + url;

            WebView.NavigateToString(url);
        }
    }
}
