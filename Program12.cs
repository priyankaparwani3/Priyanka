

using System;



namespace Tutlane

{

    class Program

    {

        static void Main(string[] args)

        {

            int x = 10, y = 5;

            switch (x)

            {

                case 10:

                    Console.WriteLine("X Value: 10");

                    switch (y)
                    {

                        case 5:

                            Console.WriteLine("Nested Switch Value: 5");

                            switch (y - 2)
                            {

                                case 3:

                                    Console.WriteLine("Another Nested Switch Value: 3");

                                    break;

                            }

                            break;

                    }

                    break;

                case 15:

                    Console.WriteLine("X Value: 15");

                    break;

                case 20:

                    Console.WriteLine("X Value: 20");

                    break;

                default:

                    Console.WriteLine("Not Known");

                    break;

            }

            Console.WriteLine("Press Enter Key to Exit..");

            Console.ReadLine();

        }

    }

}
