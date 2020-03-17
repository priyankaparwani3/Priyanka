using System;

    class Program
    {
        static void Main(string[] args)
        {
        Console.WriteLine("Enter a number");
        int UserNumber = int.Parse(Console.ReadLine());

        switch (UserNumber)
        {
            case 10:
                Console.WriteLine("your number is 10");
                break;
            case 20:
                Console.WriteLine("your number is 20");
                break;
            case 30:
                Console.WriteLine("your number is 30");
                break;
            default:
                Console.WriteLine("your number is not 10, 20 & 30");
                break;

        }
        }
    }

