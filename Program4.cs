using System;

namespace Project4
{
    class Program
    {
        static void Main()
        {
            int Numerator = 10;
            int Denominator = 2;
            int Result = Numerator % Denominator;
            Console.WriteLine("Result {0}", Result);
            int Number = 10;
            int AnotherNumber = 20;
            if (Number == 10 && AnotherNumber == 20)//(Number == 10 || AnotherNumber == 20)
                Console.WriteLine("Yes");
            int Numb = 10;
            bool IsNumb10;
            if(Numb == 10)
            {
                IsNumb10 = true;
            }
            else
            {
                IsNumb10 = false;
            }
            Console.WriteLine("Numb==10 is true {0}", IsNumb10);
            int N = 15;
            bool IsN10 = N == 10 ? true : false;
                Console.WriteLine("N == 10 is {0}", IsN10);
        }
    }
}
