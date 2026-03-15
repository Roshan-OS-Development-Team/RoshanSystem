using System;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace Roshan_System
{
    public partial class Pong : Window
    {
        private DispatcherTimer gameTimer;
        private double playerSpeed = 0;
        private double ballXSpeed = 3;
        private double ballYSpeed = 3;

        private int playerScore = 0;
        private int computerScore = 0;

        private Random rnd = new Random();

        public Pong()
        {
            InitializeComponent();
            this.Loaded += Pong_Loaded;
        }

        private void Pong_Loaded(object sender, RoutedEventArgs e)
        {
            this.Focus(); // capture key input
            SetupGameLoop();
        }

        private void SetupGameLoop()
        {
            gameTimer = new DispatcherTimer();
            gameTimer.Interval = TimeSpan.FromMilliseconds(20); // ~50 FPS
            gameTimer.Tick += GameLoop;
            gameTimer.Start();
        }

        private void GameLoop(object sender, EventArgs e)
        {
            double canvasWidth = GameCanvas.ActualWidth;
            double canvasHeight = GameCanvas.ActualHeight;

            // --- Move Player Paddle ---
            double playerTop = Canvas.GetTop(PlayerPaddle) + playerSpeed;
            playerTop = Math.Max(0, Math.Min(canvasHeight - PlayerPaddle.Height, playerTop));
            Canvas.SetTop(PlayerPaddle, playerTop);

            // --- Move Computer Paddle (AI) ---
            double computerTop = Canvas.GetTop(ComputerPaddle);
            double targetY = Canvas.GetTop(Ball) + Ball.Height / 2 - ComputerPaddle.Height / 2;
            double aiSpeed = 2;

            if (computerTop < targetY)
                computerTop += aiSpeed;
            else if (computerTop > targetY)
                computerTop -= aiSpeed;

            computerTop = Math.Max(0, Math.Min(canvasHeight - ComputerPaddle.Height, computerTop));
            Canvas.SetTop(ComputerPaddle, computerTop);

            // --- Move Ball ---
            double ballLeft = Canvas.GetLeft(Ball) + ballXSpeed;
            double ballTop = Canvas.GetTop(Ball) + ballYSpeed;

            // Bounce off top/bottom walls
            if (ballTop <= 0)
            {
                ballYSpeed = Math.Abs(ballYSpeed);
                ballTop = 0;
            }
            else if (ballTop >= canvasHeight - Ball.Height)
            {
                ballYSpeed = -Math.Abs(ballYSpeed);
                ballTop = canvasHeight - Ball.Height;
            }

            // --- Paddle collisions with angle reflection ---
            if (IsCollision(PlayerPaddle, Ball))
            {
                ballXSpeed = Math.Abs(ballXSpeed); // move right
                double overlap = (Canvas.GetLeft(PlayerPaddle) + PlayerPaddle.Width) - Canvas.GetLeft(Ball);
                Canvas.SetLeft(Ball, Canvas.GetLeft(Ball) + overlap);

                double paddleCenter = Canvas.GetTop(PlayerPaddle) + PlayerPaddle.Height / 2;
                double ballCenter = Canvas.GetTop(Ball) + Ball.Height / 2;
                double offset = (ballCenter - paddleCenter) / (PlayerPaddle.Height / 2);
                ballYSpeed = 3 * offset;
            }
            else if (IsCollision(ComputerPaddle, Ball))
            {
                ballXSpeed = -Math.Abs(ballXSpeed); // move left
                double overlap = Canvas.GetLeft(Ball) + Ball.Width - Canvas.GetLeft(ComputerPaddle);
                Canvas.SetLeft(Ball, Canvas.GetLeft(Ball) - overlap);

                double paddleCenter = Canvas.GetTop(ComputerPaddle) + ComputerPaddle.Height / 2;
                double ballCenter = Canvas.GetTop(Ball) + Ball.Height / 2;
                double offset = (ballCenter - paddleCenter) / (ComputerPaddle.Height / 2);
                ballYSpeed = 3 * offset;
            }

            // --- Score checking with single increment ---
            if (ballLeft <= 0)
            {
                computerScore++;
                ComputerScoreText.Text = computerScore.ToString();
                ResetBall();
                if (computerScore >= 5)
                {
                    MessageBox.Show("You lost to an AI", "Lost", MessageBoxButton.OK, MessageBoxImage.Information);
                }    
                return; // skip rest of this tick
            }
            else if (ballLeft >= canvasWidth - Ball.Width)
            {
                playerScore++;
                PlayerScoreText.Text = playerScore.ToString();
                ResetBall();
                if (playerScore >= 5)
                {
                    MessageBox.Show("You Won", "Won", MessageBoxButton.OK, MessageBoxImage.Information);
                }
                return; // skip rest of this tick
            }

            Canvas.SetLeft(Ball, ballLeft);
            Canvas.SetTop(Ball, ballTop);
        }

        private void ResetBall()
        {
            double canvasWidth = GameCanvas.ActualWidth;
            double canvasHeight = GameCanvas.ActualHeight;

            Canvas.SetLeft(Ball, (canvasWidth - Ball.Width) / 2);
            Canvas.SetTop(Ball, (canvasHeight - Ball.Height) / 2);

            // Random starting direction
            ballXSpeed = (rnd.Next(0, 2) == 0) ? 3 : -3;
            ballYSpeed = (rnd.NextDouble() > 0.5) ? 3 : -3;
        }

        private bool IsCollision(Rectangle paddle, Ellipse ball)
        {
            Rect rPaddle = new Rect(Canvas.GetLeft(paddle), Canvas.GetTop(paddle), paddle.Width, paddle.Height);
            Rect rBall = new Rect(Canvas.GetLeft(ball), Canvas.GetTop(ball), ball.Width, ball.Height);
            return rPaddle.IntersectsWith(rBall);
        }

        private void Window_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Up)
                playerSpeed = -5;
            else if (e.Key == Key.Down)
                playerSpeed = 5;
        }

        private void Window_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Up || e.Key == Key.Down)
                playerSpeed = 0;
        }
    }
}