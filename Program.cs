using System;

namespace Project1
{
    class Program
    {
        static void Main()
        {
                Console.WriteLine("Enter your First name");

                string FirstName = Console.ReadLine();
                Console.WriteLine("Enter your Last name");

                string LastName = Console.ReadLine();

                Console.WriteLine("Hello {0} {1}", FirstName, LastName);

                //Console.WriteLine("Hello " + FirstName,LastName);
        }
    }
}
