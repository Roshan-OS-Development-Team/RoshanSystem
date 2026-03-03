using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Effects;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using Microsoft.Win32;

namespace Roshan_System
{
    /// <summary>
    /// Interaction logic for Notepad.xaml
    /// </summary>
    public partial class Notepad : Window
    {
        public Notepad()
        {
            InitializeComponent();
        }

        private void Savefile()
        {
            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "Text file (*.txt)|*.txt|All files (*.*)|*.*";
            saveFileDialog.Title = "Save Notepad Content";
            if (saveFileDialog.ShowDialog() == true)
            {
                string text = NotepadTextBox.Text;
                File.WriteAllText(saveFileDialog.FileName, text );
                MessageBox.Show($"File saved to {saveFileDialog.FileName}", "Saved");
            }
            else
            {
                return;
            }
        }
        private void Save_File(object sender, RoutedEventArgs e)
        {
          Savefile();
        }

        private void SaveFileKey(object sender, KeyEventArgs s)
        {
            if (Keyboard.IsKeyDown(Key.LeftCtrl) && s.Key == Key.S)
            {
                Savefile();
            }
        }

        private void loadfile()
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.Filter = "Text file (*.txt)|*.txt|All files (*.*)|*.*";
            openFileDialog.Title = "Open Notepad Content";
            if (openFileDialog.ShowDialog() == true)
            {
                string text = File.ReadAllText(openFileDialog.FileName);
                NotepadTextBox.Text = text;
            }
            else
            { 
                return;
            }    
        }
        private void Load_File(object sender, RoutedEventArgs e)
        {
            loadfile();
        }
        private void LoadFileKey(object sender, KeyEventArgs o)
        {
            if (Keyboard.IsKeyDown(Key.LeftCtrl) && o.Key == Key.O)
            {
                loadfile();
            }
        }
    }
}
