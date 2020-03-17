

using System;



namespace Priyanka

{

    class Program

    {

        static void Main(string[] args)

        {

            string[] names = new string[3] { "Priyanka", "Deepak", "Varsha" };

            foreach (string name in names)

            {

                Console.WriteLine(name);

            }

            Console.WriteLine("Press Enter Key to Exit..");

            Console.ReadLine();

        }

    }

}

