using System;

namespace Project3
{
    class Program
    {
        static void Main()
        {
            string Name = "\"Priyanka\"";
            Console.WriteLine(Name);
            string FName = "\nPriyanka\n";
            Console.WriteLine(FName);
            string MName = "One\nTwo\nThree\n";
            Console.WriteLine(MName);
            string LName = "C:\\csharp\\projects\\file";
            Console.WriteLine(LName);
            string FullName = @"C:\\csharp\\projects\\file";//string FullName = @"C:\csharp\projects\file";
            Console.WriteLine(FullName);
        }
    }
}
