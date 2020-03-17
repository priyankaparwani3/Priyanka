

using System;



namespace Examples

{

    class Program

    {

        static void Main(string[] args)

        {

            string name = null;

            try

            {

                if (name.Length > 0) // Exception will occur

                {

                    Console.WriteLine("Name: " + name);

                }

            }

            catch (Exception ex)

            {

                Console.WriteLine("Exception: {0}", ex.Message);

            }

            finally

            {

                Console.WriteLine("Finally Block.");

            }

            Console.ReadLine();

        }

    }

}

