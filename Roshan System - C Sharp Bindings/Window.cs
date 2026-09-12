using System.Runtime.InteropServices;
using static RoshanSystemCoreLib.getDll;

namespace RoshanSystemCoreLib
{
    public class Window
    {
        private IntPtr _nativeHandle;
        private bool _isDisposed;
        
        private delegate IntPtr CreateDelgate(
            IntPtr parent, 
            [MarshalAs(UnmanagedType.LPUTF8Str)] string name, 
            int width, 
            int height, 
            [MarshalAs(UnmanagedType.LPUTF8Str)] string icon_path
        );

        private delegate void delDelgate(IntPtr handle);
        private delegate void MoveDelgate(IntPtr handle, int x, int y);
        private delegate void ShowDelgate(IntPtr handle);
        private delegate int getWinXDelgate(IntPtr handle);
        private delegate int getWinYDelgate(IntPtr handle);

        private static readonly CreateDelgate NativeCreate;
        private static readonly delDelgate NativeDelete;
        private static readonly MoveDelgate NativeMove;
        private static readonly ShowDelgate NativeShow;
        private static readonly getWinXDelgate getWinX;
        private static readonly getWinYDelgate getWinY;

        static Window()
        {
            string dllPath = RoshanSystemCoreLib.getDll.getDllPath();
            IntPtr RoshanOSCoreLibHandle = NativeLibrary.Load(dllPath);

            NativeCreate = 
                Marshal.GetDelegateForFunctionPointer<CreateDelgate>(NativeLibrary.GetExport(RoshanOSCoreLibHandle,
                    "createWindow"));
            NativeDelete =
                Marshal.GetDelegateForFunctionPointer<delDelgate>(NativeLibrary.GetExport(RoshanOSCoreLibHandle,
                    "delWindow"));
            NativeMove =
                Marshal.GetDelegateForFunctionPointer<MoveDelgate>(NativeLibrary.GetExport(RoshanOSCoreLibHandle,
                    "moveWin"));
            NativeShow =
                Marshal.GetDelegateForFunctionPointer<ShowDelgate>(NativeLibrary.GetExport(RoshanOSCoreLibHandle,
                    "showWin"));
            getWinX = Marshal.GetDelegateForFunctionPointer<getWinXDelgate>(NativeLibrary.GetExport(RoshanOSCoreLibHandle, "" +
                "getWinX"));
            getWinY = Marshal.GetDelegateForFunctionPointer<getWinYDelgate>(NativeLibrary.GetExport(
                RoshanOSCoreLibHandle,
                "getWinY"));
        }
        public Window(IntPtr master, string title, int width, int height, string icon_path)
        {
            _nativeHandle = NativeCreate(master, title, width, height, icon_path);

            if (_nativeHandle == IntPtr.Zero)
            {
                throw new InvalidOperationException("Failed to create Internal C++ Class");
            }
        }

        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }
        
        ~Window() 
        {
            Dispose(false);    
        }

        protected virtual void Dispose(bool disposing)
        {
            if (_isDisposed) return;
            if (_nativeHandle != IntPtr.Zero)
            {
                NativeDelete(_nativeHandle);
                _nativeHandle = IntPtr.Zero;
            }

            _isDisposed = true;
        }
    }
}
