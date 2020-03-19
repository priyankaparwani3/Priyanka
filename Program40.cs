using System;
using System.IO;
namespace exception
{
    class ExceptionHandling
    {
        public static void Main()
        {
            StreamReader streamReader = null;
            try
            {
                streamReader = new StreamReader("C:\\Samplefiles\\Data1.txt");
                Console.WriteLine(streamReader.ReadToEnd());
     
            }
            catch(FileNotFoundException ex)
            {
                Console.WriteLine("Please check if the file {0} exists", ex.FileName);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);

            }
            finally
            {
                if (streamReader != null)
                {
                    streamReader.Close();
                }
                Console.WriteLine("Finally block");
            }
        }
    
    }
}
