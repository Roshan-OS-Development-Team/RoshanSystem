using Avalonia.Controls;
using Avalonia.Interactivity;

namespace RoshanSystem.Views;

public partial class MainView : UserControl
{
    public MainView()
    {
        InitializeComponent();
    }
    private void OpenCalculator(object? sender, RoutedEventArgs e)
    {
        Calculator calculator = new Calculator();
        calculator.Show();
    }
    private void OpenNotepad(object? sender, RoutedEventArgs e)
    {
        
    }
}