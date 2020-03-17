using System;
namespace Demo
{
    class Program
    {
        public static void Main()
        {
            int FN = 10;
            int SN = 20;
            //FN and LN are method arguments
            int Total = Sum(FN, SN);
            Console.WriteLine(Total);
        }
        //FirstNumber and SecondNumber are method parameters
        public static int Sum(int FirstNumber, int SecondNumber)
        {
            int Result = FirstNumber + SecondNumber;
            return Result;
        }
    }
}
